class Average(Exception):
    pass

class Dispersion(Exception):
    pass

class Number(Exception):
    pass

def _coroutine():
    s = 0
    n = 0
    d = 0
    while True:
        x = yield
        n += 1
        s += x
        d += x ** 2
        print(' Number of the values: {}.'.format(n))
        print(' Average value: {}.'.format(s / n))
        print(' Dispersion of the values: {}. \n'.format(d / n - (s / n) ** 2))


def ex_coroutine():
    print("Starting coroutine")
    s = 0
    n = 0
    d = 0
    try:
        while True:
            try:
                x = yield
                s += x
                n += 1
                d += x**2
            except Dispersion:
                yield ' Dispersion of the values: {}. \n'.format(d / n - (s / n) ** 2)
            except Number:
                yield ' Number of the values: {}.'.format(n)
            except Average:
                yield ' Average value: {}.'.format(s / n)
    finally:
        print("Stop coroutine")

coroutine1 = _coroutine()
next(coroutine1)

for i in range(3):
    coroutine1.send(i)
coroutine1.close()

coroutine = ex_coroutine()
next(coroutine)

for i in range(3):
    coroutine.send(i)
    while True:

        print()
        print(coroutine.throw(Number))
        next(coroutine)

        print(coroutine.throw(Average))
        next(coroutine)

        print(coroutine.throw(Dispersion))
        next(coroutine)

coroutine.close()