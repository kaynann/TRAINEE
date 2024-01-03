'''
Faça um sistema de controle de estoque que atenda as seguintes regras.
  1. cadastro de produtos
  2. controle de validade
  3. controle de quantidade
'''
from datetime import datetime

class ControleDeEstoque:

  def __init__(self, marca, validade, quantidade):
    self.marca = marca
    self.validade = validade
    self.quantidade = quantidade
    self.data_atual = '01/02/2024'

  def __str__(self):
    return f'>> STATUS PRODUTO << \nMarca: { self.marca }\nValidade { self.validade }\nQuantidade: { self.quantidade }'
  
  def get_marca(self):
        return self.marca

  def get_validade(self):
    data_atual_convert = datetime.strptime(self.data_atual, '%m/%d/%Y')
    validade_convert = datetime.strptime(self.validade, '%m/%d/%Y')

    quantidade_dias = (validade_convert - data_atual_convert).days
    
    if quantidade_dias <= 0:
      print(f'O produto venceu a validade. O produto venceu há { abs(quantidade_dias) } dias')
    elif quantidade_dias <=30:
      print(f'O produto está perto de vencer a validade. Validade: { quantidade_dias }  dias restantes')
    else:
      if quantidade_dias > 30:
        print(f'O produto está dentro do prazo de validade. Validade: { quantidade_dias } dias restantes')
 
  def get_quantidade(self):
    if self.quantidade == 0:
      return 'O estoque do produto esgotou'
    elif self.quantidade <= 10:
      return 'O estoque do produto está acabando'
    else:
      return self.quantidade

  def set_marca(self, nova_marca):
        self.marca = nova_marca
        return self.marca
   
  def set_quantidade(self, nova_quantidade):
      self.quantidade = nova_quantidade
      return self.quantidade

leite = ControleDeEstoque('Itambé', '08/08/2024', 20)
print(leite)
leite.get_validade()
print(leite.get_quantidade())
