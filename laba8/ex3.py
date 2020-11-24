def my_map(function, iterable):
    for i in iterable:
        yield function(i)
#

def my_zip(*values):
    n = len(values[0])
    for i in range(n):
        a = []
        for j in values:
            a.append(j[i])
        yield list(a)

def my_enumerate(iterable):
    for i in iterable:
        yield tuple(i,iterable[i])