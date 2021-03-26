'''
Crie classes para representar estados e cidades. Cada estado tem um nome, sigla e cidades. Cada cidade tem
nome e população. Escreva um programa de testes que crie três estados com algumas cidades em cada um. Exiba
a população de cada estado como a soma da população de suas cidades.
'''

class Estado:

    def __init__(self, nome, sigla, cidade):
        self.nome = nome;
        self.sigla = sigla;
        self.cidade = cidade

    def populacao(self):
        resultado = 0
        for c in self.cidade:
            resultado += c.populacao
        return resultado

class Cidade:

    def __init__(self, nome, populacao):
        self.nome = nome;
        self.populacao = populacao;

c1 = Cidade('Cajazeiras', 58446)
c2 = Cidade('Santa Helena', 5871)
c3 = Cidade('Patos', 108192)

e1 = Estado('Paraiba', 'pb', [c1,c2,c3])

print("A populacao da ", e1.nome, " eh de ", e1.populacao())