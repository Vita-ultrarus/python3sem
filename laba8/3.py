from itertools import combinations

def get_combinations(s, n):
    a=[]
    s=sorted(s)
    for i in range(1,n+1):
        b=list(combinations(s,i))
        for j in b:
            a.append(''.join(j))
    return a



print(*get_combinations("list", 3))


