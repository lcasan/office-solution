import os
import docx
import errno

root = os.getcwd()
wfind = input('word to search: ')

#filtered out:
def read_word(path, inputs):
    doc = docx.Document(path)    
    for paragraph in doc.paragraphs:
        wlist = paragraph.text.split()
        for word in wlist:
            if word == wfind:
                doc.save(root +'/output_doc/'+ inputs.name)

#scan directory entries
def read_dirs(path):
    with os.scandir(path) as _dir:
        for inputs in _dir:
            if inputs.is_dir():
                read_dirs(path + '/' + inputs.name)
            else:
                n = len(inputs.name)
                if inputs.name[n-4 : n] == 'docx':
                    _path = path + '/' + inputs.name
                    read_word(_path, inputs) 
                    
                #if inputs.name[n-3 : n] == 'doc':
                    #convert to docx
                    
try:
    os.mkdir('output_doc')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

read_dirs(root)
    
