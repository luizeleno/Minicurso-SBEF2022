'''

Um exemplo mostrando o que é um decorator, na forma mais simples possível

'''

#####################################
# Definição da função my/-decorator #
#####################################
def my_decorator(func):
    def funcao_de_decoracao(x):
        a = func(x)
        return f'a função {func.__name__} de {x} retorna {a}'
    return funcao_de_decoracao

####################################################
# criando uma função F() qualquer e redefinindo-a, #
# passando-a como argumento à função my_decorador  #
####################################################

def F(x):
    return x**2

print(F(5))

F = my_decorator(F)

print(F(5))

######################################################
# agora a mesma coisa usando a sintaxe de decorator: #
######################################################

@my_decorator
def F(x):
    return x**2

print(F(5))
