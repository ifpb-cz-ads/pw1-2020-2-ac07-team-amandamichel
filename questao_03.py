'''3) Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para baixo, além do mínimo, ela vá para o canal máximo.
Se mudarmos para cima, além do canal máximo, que volte ao canal mínimo.'''

class Televisão:
  def __init__(self, min, max): #parametros no construtor
    self.ligada = False
    self.canal = 2
    self.cmin = min
    self.cmax = max

  def muda_canal_para_baixo(self):
    if(self.canal-1 >= self.cmin):
      self.canal -= 1
    else:
      self.canal = self.cmax

  def muda_canal_para_cima(self):
    if(self.canal+1 <= self.cmax):
      self.canal += 1
    else:
      self.canal = self.cmin


tv=Televisão(1,10)


tv=Televisão(1,10)
for x in range(0,20):
  tv.muda_canal_para_baixo()
  print(tv.canal)

for x in range(0,20):
  tv.muda_canal_para_cima()
  print(tv.canal)