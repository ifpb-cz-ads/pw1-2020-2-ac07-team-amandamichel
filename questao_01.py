'''1) Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos Televisão e atribua tamanhos e marcas diferentes.
Depois, imprima o valor desses atributos de forma a confirmar a independência dos valores de cada instância (objeto).'''

  
class Televisão: 
  def __init__(self, tamanho, marca):
    self.tamanho = tamanho
    self.marca = marca
    self.ligada = False
    self.canal = 2

  def muda_canal_para_baixo(self):
    self.canal -= 1

  def muda_canal_para_cima(self):
    self.canal += 1

tv1 = Televisão(32,'Samsung')
tv2 = Televisão(65, 'LG')

print(f'Tamanho: {tv1.tamanho} polegadas | Marca: {tv1.marca} \n')

print(f'Tamanho: {tv2.tamanho} polegadas | Marca: {tv2.marca} \n')