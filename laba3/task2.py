def write_array(array, file_name):
    file_name.writelines(array)
    return
a=[]
with open("/Users/Имя/python3sem/лаба3/text.txt",'r') as file:
    for line in file:
        a.append(line)
with open("/Users/Имя/python3sem/лаба3/input.txt",'w') as input:
    write_array(a,input)
