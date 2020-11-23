def print_map(function, iterable):
    iterator=iter(iterable)
    while True:
        print(function(next(iterator)))