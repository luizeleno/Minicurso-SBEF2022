'''
Dois exemplos de decoradores de funções

O primeiro é mais simples e não aceita argumentos

O segundo é só um pouco mais complicado e aceita um parâmetro.
'''

# decorator simples

def decorate(func):
    def ação(*args, **kwargs):
        a = func(*args)
        print('função retorna', a)
        return a
    return ação

@decorate
def f1(a=5):
    return 2 * a

f1(3)

# decorator com argumentos

def decorador(n=1):
    def def_func(func):
        def def_args(*args, **kwargs):
            a = func(*args, **kwargs)
            print(f'função retorna {a}; decorador com opção {n}')
            return a
        return def_args
    return def_func

@decorador()
def f1(a=5):
    return 2 * a

z = f1(4)
print(z)