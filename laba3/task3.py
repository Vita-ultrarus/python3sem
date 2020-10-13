import shutil
import os
def write_array(array, file_name):
    for line in range(len(array)):
        file_name.write(array[line])
        file_name.write('\n')
    return
shutil.unpack_archive('C:/Users/Имя/python3sem/лаба3/main.zip','C:/Users/Имя/python3sem/лаба3','zip')
a=[]
for dirpath, dirnames, filenames in os.walk('C:/Users/Имя/python3sem/лаба3/main'):
    for dirname in dirnames:
        for filename in filenames:
            if filename.endswith('.py'):
                a.append(dirname)
a.sort()
with open("/Users/Имя/python3sem/лаба3/input.txt",'w') as input:
    write_array(a,input)


