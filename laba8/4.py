from itertools import combinations_with_replacement
def get_combinations_with_r(s, n):
    a=[]
    c = list(combinations_with_replacement(s, n))
    c=sorted(c)
    for i in range(len(c)):
        a.append(''.join(c[i]))
    return a
print(get_combinations_with_r("cat", 2))