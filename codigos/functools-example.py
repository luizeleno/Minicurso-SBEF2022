'''
Exemplos de recursos do módulo functools

partial(): "congela" argumentos selecionados 

@cache: função para a técnica de memoização (https://en.wikipedia.org/wiki/Memoization)

'''

import functools
import time

# decorador simples para cronometrar tempo de execução de funções
def cronometro(func):
    def cronometrar(*args, **kwargs):
        t1 = time.time()
        a = func(*args, **kwargs)
        t2 = time.time()
        print(f'tempo de execução de {func}: {t2-t1}')
        return a
    return cronometrar

# exemplo de functools.partial

def f(a, b, c):
    return [a, b, c]

fb1c2 = functools.partial(f, b=1, c=2)

print(fb1c2(10))

# exemplo de @functools.cache

@cronometro
@functools.cache
def fatorial(n):  # retorna n!
    return n * fatorial(n-1) if n > 1 else 1

print(fatorial(10))

print(fatorial(11))
