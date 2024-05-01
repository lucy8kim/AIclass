class comx:
    def __init__(self, x, y):
        self.real = x 
        self.imag = y
    def __add__(self, o):
        return comx(self.real+o.real, self.imag+o.imag)
    def __sub__(self, o):
        return comx(self.real-o.real, self.imag-o.imag)
    def __mul__(self, o):
        return comx(self.real*o.real-self.imag*o.imag, self.imag*o.real+self.real*o.imag)
    def __truediv__(self, o):
        return comx((self.real*o.real+self.imag*o.imag) // (o.real*o.real + o.imag*o.imag), (self.imag*o.real-self.real*o.imag) // (o.real*o.real+o.imag*o.imag))
    def __str__(self):
        return '{} + {}j'.format(self.real, self.imag)


a = comx(4, 2)
b = comx(2, 1)
c = a + b
print('a + b =', c)
d = a - b
print('a - b =', d)
e =a * b
print('a * b =', e)
f = a / b
print('a / b =', f)
