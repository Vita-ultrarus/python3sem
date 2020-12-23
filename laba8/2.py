from itertools import permutations

def get_permutations(s, n):
    a=sorted(list(permutations(s,n)))
    return a


print(*get_permutations("cat", 2))


