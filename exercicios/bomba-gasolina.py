class BombaGasolina:
  def __init__(self,  quantidade_combustivel):
    self.quantidade_combustivel = quantidade_combustivel
    self.tipo_combustivel = None
    self.valor_combustivel = 0
    self.valor_pagar = 0

  def set_tipo_combustivel(self):
    print('SEJA BEM VINDO AO POSTO ELVIS VALLEY!!!')

    self.tipo_combustivel = input('Digite o tipo de combustivel, "Alcool ou Gasolina": ').lower()

    if self.tipo_combustivel == 'alcool':
      self.valor_combustivel = 4.50

    elif self.tipo_combustivel == 'gasolina':
      self.valor_combustivel = 6.30

  def escolha_cliente(self):
    escolha = input('Você deseja abastecer em litros ou dinheiro? ')

    if escolha == 'litros':
      self.abastecer_litro()
      
    elif escolha == 'dinheiro':
      self.abastecer_dinheiro()

  def abastecer_litro(self):
    litro = float(input('Digite a quantidade de litros: '))
    self.valor_pagar = litro * self.valor_combustivel

    if litro > self.quantidade_combustivel:
      print(f'Quantidade de litros insuficiente. A quantidade de litros do bomba é {self.quantidade_combustivel} litros')    
      self.abastecer_litro()

    elif self.quantidade_combustivel >= litro:
        print(f'Você vai pagar R${ self.valor_pagar } em { litro } litros')
        self.quantidade_combustivel -= litro
        print(f'A quantidade de litros atuais da bomba é { self.quantidade_combustivel } litros')
    
  def abastecer_dinheiro(self):
    dinheiro = float(input(f'Digite o valor que você quer de { self.tipo_combustivel }: '))
    litros_abastecidos = dinheiro / self.valor_combustivel
    print(f'Você vai pagar R${ dinheiro } em {litros_abastecidos:.2f} litros')    


posto = BombaGasolina(100)
posto.set_tipo_combustivel()
posto.escolha_cliente()