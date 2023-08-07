
class Complex:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f'{self.a}{self.b:+}i'
    
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        z = Complex(a, b)
        return z
    
    def __neg__(self):
        return Complex(-self.a, -self.b)
    
    def __sub__(self, other):
        return self + other.__neg__()
        #alternativa: return self + (-other)
        
    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.a * other.a - self.b * other.b
            im = self.a * other.b + self.b * other.a
            return Complex(re, im)
        else:
            return Complex(self.a * other, self.b * other)
    
    __rmul__ = __mul__ 
    
z1 = Complex(4, 5)
r = 5

z2 = r * z1
