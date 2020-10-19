import time
def dec1(function):
    def wrapper(file1):
        n=time.time()
        v=function(file1)
        m=time.time()
        with open(file1,'w') as filem:
            if v==None:
                filem.write('-'+'\n')
            else:
                filem.write(str(v)+'\n')
            filem.write(str(n)+'\n')
            filem.write(str(m)+'\n')
            filem.write(str(m-n)+'\n')
    return wrapper
@dec1
def filem(file1):
    file = open(file1)
    text = file.read()
    file.close()
file1 = "/Users/Имя/python3sem/лаба3/text.txt"
filem(file1)


