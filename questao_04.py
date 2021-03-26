'''

Utilizando o que aprendemos com funções, modifique o construtor da classe Televisão de forma que min e max
sejam parâmetros opcionais, onde min vale 2 e max vale 14, caso outro valor não seja passado.

'''


class Televisão:
    def __init__(self, min=2, max=14):  # parametros no construtor
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

tv = Televisão()
print(tv.cmin)
print(tv.cmax)
for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)
for x in range(0, 120):
    tv.muda_canal_para_baixo()
print(tv.canal)