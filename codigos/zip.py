'''
Um exemplo de como usar a função `zip()` tanto para entrelaçar como desentrelaçar diferentes iteráveis. 
'''

n, l = [1, 2, 3], ['a', 'b', 'c']
pairs = list(zip(n, l))
print(pairs)

n, l = zip(*pairs)
print(n, l)