class pessoa:
    
    def __init__(self, nome, data_nasc, local_nasc):
        self.nome = nome
        self.data_nasc = data_nasc
        self.local_nasc = local_nasc
        self.pais = 'Brasil'

    def idade(self):
        # TODO: implementar o código
        return 'não está implementado'
    
    def confirma_data_nasc(self):
        self.data_nasc = self.data_nasc + ': confirmado'
        print(self.data_nasc)
        #return self.data_nasc
    
    def altera_local_nasc(self, novo_local):
        self.local_nasc = novo_local
    
    def altera_data_nasc(self, nova_data, altera_local=False, novo_local=''):
        self.data_nasc = nova_data
        if altera_local == True:
            self.altera_local_nasc(novo_local)
            
    def __str__(self):
        s = f'Nome: {self.nome}\n'
        s += f'Curso: {self.curso}\n'
        s += f'Matricula: {self.matricula}'
        return s
            
class aluno(pessoa):
    
    def __init__(self, nome, data, local, curso, matricula):
        super().__init__(nome, data, local)
        self.curso = curso
        self.matricula = matricula
        
mario = aluno('Mario Bros.', '05/06/07', 'Cascavel-PR', 'EF', '465')

print(mario)
