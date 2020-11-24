from itertools import combinations

def get_combinations(s, n):
    for i in range(1,n):
        combinations(s,i)


print(get_combinations("cat", 2))


