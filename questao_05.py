'''5) Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias (objetos), especificando o valor de min e max por nome.'''


class Televisão:
    def __init__(self, nome, min=2, max=14):
        self.nome = nome
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    
    def __repr__(self):
        return f'Nome: {self.nome} | Canal min: {self.cmin} | Canal max: {self.cmax} | Canal atual: {self.canal} \n'

    def muda_canal_para_baixo(self):
        if (self.canal - 1 >= self.cmin):
            self.canal -= 1

    def muda_canal_para_cima(self):
        if (self.canal + 1 <= self.cmax):
            self.canal += 1

tv1 = Televisão('TV 1', 2, 4)
tv2 = Televisão('TV 2', 4, 20)

print(tv1)

print(tv2)