'''
Exemplo simples de criação de um iterator. Usa uma estratégia parecida muito similar a `comprehension`
'''

z = (x for x in range(10))

print(type(z))

print(next(z))
print(next(z))
print(list(z))