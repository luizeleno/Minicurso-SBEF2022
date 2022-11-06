'''
O exemplo mostra uma classe filha (aluno) que herda as propriedades e métodos de uma classe mãe (pessoa). 

O __init__ da classe filha chama a função super(), para aproveitar o __init__ da classe mãe.
'''

import datetime

class pessoa:
    def __init__(self, nome, data_nasc, loc_nasc):
        self.dados = {}
        self.dados['Nome'] = nome
        self.dados['Data de nascimento'] = datetime.datetime.strptime(data_nasc, '%d/%m/%Y')
        self.dados['Local de nascimento'] = loc_nasc
    
    def idade(self):
        today = datetime.date.today()
        nasc = self.dados['Data de nascimento']
        age = today.year - nasc.year - ((today.month, today.day) < (nasc.month, nasc.day))
        return age

    def __str__(self):
        dados_str = ''
        for key, value in self.dados.items():
            dados_str += f'{key}: {value}\n'
        return dados_str

class aluno(pessoa):

    def __init__(self, nome, data_nasc, loc_nasc, NUSP, curso):
        super().__init__(nome, data_nasc, loc_nasc)
        self.dados['NUSP'] = NUSP
        self.dados['Curso'] = curso

luiz = pessoa('Luiz Eleno', '01/10/1976', 'São Paulo-SP')
print(luiz)

luiz = aluno('Luiz Eleno', '01/10/1976', 'São Paulo-SP', 1176388, 'Engenharia Física')
print(luiz)