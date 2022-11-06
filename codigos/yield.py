'''
Alguns exemplos simples do uso da declaração (*statement*) `yield` para a criação de funções geradoras (*generator functions*) 
'''

# exemplo 1: geração dos números naturais 

def inteiros():
    # gera sob demanda os números naturais
    n = 0
    while True:
        yield n
        n += 1

z = inteiros()

for i in range(50):
    print(next(z))

# exemplo 2: percorrer repetidamente os valores de uma lista

colors = ['blue', 'red', 'green', 'yellow', 'black']

def select_color():
    n = 0
    while True:
        yield colors[n]
        n = (n + 1) % len(colors)

cor = select_color()

for i in range(12):
    print(next(cor))
