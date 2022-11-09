'''
Uma classe que implementa números complexos 
(sei que isso é desnecessário, já que `complex` está implementado na biblioteca padrão) e algumas operações básicas usando constructors e sobrecarga de operadores (overload). 
'''

import numpy

class Complex:
    
    def __init__(self, a, b):
        self.a, self.b = a, b
        
    def __str__(self):
        return f'{self.a}{self.b:+}i'

    def conjugate(self):
        return Complex(self.a, -self.b)
    
    def Re(self):
        return self.a
    
    def Im(self):
        return self.b

    def __add__(self1, self2):
        if isinstance(self2, Complex):
            # soma de dois complexos
            return Complex(self1.a + self2.a, self1.b + self2.b)
        else: 
            # soma de complexo e real
            return self1 + Complex(self2, 0)  # recursão disfarçada aqui!        
    
    __radd__ = __add__  # soma de real e complexo
    
    # TODO: implementar __iadd__, __imul__, __isub__, __ipow__

    def __neg__(self):
        return Complex(-self.a, -self.b)
    
    def __sub__(self1, self2):
        return self1 + self2.__neg__()
    
    def __mul__(self1, self2):
        if isinstance(self2, Complex):  
            # produto de dois complexos
            re = self1.a * self2.a - self1.b * self2.b
            im = self1.a * self2.b + self1.b * self2.a
            return Complex(re, im)
        else: 
            # produto de complexo por real
            return self1 * Complex(self2, 0)  # recursão disfarçada aqui!
    
    __rmul__ = __mul__  # produto de escalar por complexo
        
    def modulus(self):
        return numpy.sqrt((self * self.conjugate()).Re())
    
    def argument(self):
        return numpy.arctan2(self.b, self.a)

    def __pow__(self, n):
        # potência principal
        mz = self.modulus() ** n
        argz = n * self.argument()
        return mz * Complex(numpy.cos(argz), numpy.sin(argz))

if __name__ == '__main__':
    u = Complex(0, 1)
    v = Complex(1, -3)
    print(u**(1/3))
