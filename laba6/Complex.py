class Complex:

    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __div__(self, other):
        return Complex((self.re * other.re - self.im * other.im) / (other.re ** 2 + other.im ** 2),
                       (other.re * self.im - self.re * other.im) / (self.im ** 2 + other.im ** 2))


    def __oppos__(self):
        return Complex(self.re, - self.im)

    def __abs__(self):
        module = (self.re ** 2 + self.im ** 2) ** (1 / 2)
        return module
