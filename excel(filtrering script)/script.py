import pandas as pd

def swap_tick(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a.upper(), b.upper())
    return s 

name = []
#read archive:
with open('students_read.txt', 'r') as readfile:
    for line in readfile:
        #detect name:
        if line[0] != '#':
            num = int(line[0])
            tmp = swap_tick(line.upper()).split()           
            
            if 0 <= num and num <= 9:
                del tmp[0]
            
            name.append(tmp)

#load excel:
df = pd.read_excel('students_input.xlsx')


idx = []
for _name in name:
    if len(_name) == 2:
        idx = idx + df[df['First Name'].str.contains(_name[0]) & (df['Last Name'].str.contains(_name[1]))].index.tolist()
    elif len(_name) == 3:
        idx = idx + df[df['First Name'].str.contains(_name[0]) & (df['Last Name'].str.contains(_name[1]) | df['Last Name'].str.contains(_name[2]))].index.tolist()
    else:
        idx = idx + df[df['First Name'].str.contains(_name[0]) & (df['Middle Name'].str.contains(_name[1])) & (df['Last Name'].str.contains(_name[2]) | df['Last Name'].str.contains(_name[3]))].index.tolist()
 
df_output = pd.DataFrame()
df_output = df.iloc[idx]        
df_output.to_excel('students_output.xlsx')


        

                  
         



    
