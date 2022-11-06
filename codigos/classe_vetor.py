'''
Outro exemplo de uma classe usando constructors e sobrecarga
'''

class Vector:
    
    def __init__(self, components):
        self._c = components
    
    def __iter__(self):
        return iter(self._c)
    
    def __add__(self1, self2):
        result = [a + b for a, b in zip(self1, self2)]
        return Vector(result)
    
    def __neg__(self):
        return Vector([-x for x in self])
    
    def __sub__(self1, self2):
        return self1 + self2.__neg__()
    
    def __mul__(self1, self2):
        if isinstance(self2, Vector):  
            # produto escalar de dois vetores
            return sum(a * b for a, b in zip(self1, self2))
        else: 
            # produto de vetor por escalar
            return Vector([self2 * x for x in self1])
    
    __rmul__ = __mul__  # produto de escalar por vetor
    
    def __matmul__(self1, self2):
        # produto vetorial - só para vetores 3d
        x = self1._c[1] * self2._c[2] - self1._c[2] * self2._c[1]
        y = self1._c[2] * self2._c[0] - self1._c[0] * self2._c[2]
        z = self1._c[0] * self2._c[1] - self1._c[1] * self2._c[0]
        return Vector([x, y, z])
    
    def __len__(self):
        return len(self._c)
    
    def __str__(self):
        return f'{tuple(self)}'

if __name__ == '__main__':
    u = Vector([1, 2, 0])
    v = Vector([0, 1, 1])
    print(u @ v)
