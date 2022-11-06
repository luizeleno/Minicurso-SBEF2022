'''
    O código abaixo compara duas maneiras de produzir uma ferramenta para automaticamente adicionar valores a uma sequência e recalcular a média dos seus valores.

    A primeira estratégia usa o conceito de *closure* e funções de funções, com variáveis livres e não-locais.

    A segunda estratégia é mais direta e inteligível, através do uso de uma classe e o *construtor* `__call()__`.
'''

def make_averager():    
    total = 0
    number = 0
    def averager(new_value):
        nonlocal total, number
        total += new_value
        number += 1
        return total / number
    return averager

avg = make_averager()
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)

class averager:
    def __init__(self):
        self.total, self.number = 0, 0
    def __call__(self, new_value):
        self.total += new_value
        self.number += 1
        return self.total / self.number

avg = averager()

print(avg(10))
print(avg(11))
print(avg(10))

print(dir(avg))