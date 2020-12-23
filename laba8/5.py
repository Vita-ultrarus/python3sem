from itertools import groupby
def compress_string(s):
    a=[]
    b=groupby(s)
    for i,j in b:
        key=list(j)
        val=len(key)
        c=[val,key[0]]
        a.append(tuple(c))
    return a


print(*compress_string('1222311'))