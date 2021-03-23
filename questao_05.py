'''5) Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias (objetos), especificando o valor de min e max por nome.'''


class Televisão:
    def __init__(self, nome, min=2, max=14):
        self.nome = nome
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if (self.canal - 1 >= self.cmin):
            self.canal -= 1

    def muda_canal_para_cima(self):
        if (self.canal + 1 <= self.cmax):
            self.canal += 1

tv1 = Televisão('TV 1', 2, 4)
tv2 = Televisão('TV 2', 4, 20)

print(f'Nome: {tv1.nome} | Canal min: {tv1.cmin} | Canal max: {tv1.cmax} | Canal atual: {tv1.canal} \n')

print(f'Nome: {tv2.nome} | Canal min: {tv2.cmin} | Canal max: {tv2.cmax} | Canal atual: {tv2.canal} \n')