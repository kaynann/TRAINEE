class BombaGasolina:
  def __init__(self,  quantidade_combustivel):
    self.quantidade_combustivel = quantidade_combustivel
    self.tipo_combustivel = None
    self.valor_combustivel = 0
    self.valor_pagar = 0

  def set_tipo_combustivel(self):
    print('>>>>> SEJA BEM VINDO AO POSTO ELVIS VALLEY <<<<<')

    self.tipo_combustivel = input('Digite o tipo de combustivel, "Alcool-> [A] ou Gasolina-> [G]": ').lower()

    if self.tipo_combustivel != 'a' and self.tipo_combustivel != 'g':
      print()
      print('O valor inserido está inválido. Por favor digite novamente.\n')
      self.set_tipo_combustivel()

    elif self.tipo_combustivel == 'a':
      self.valor_combustivel = 4.50
      self.tipo_combustivel = 'alcool'

    elif self.tipo_combustivel == 'g':
      self.valor_combustivel = 6.30
      self.tipo_combustivel = 'gasolina'

  def escolha_cliente(self):
    escolha = input('Você deseja abastecer em Litros-> [L] ou Dinheiro-> [D]?: ')

    if escolha != 'l' and escolha != 'd':
      print()
      print('O valor inserido está inválido. Por favor digite novamente.')
      self.escolha_cliente()

    elif escolha == 'l':
      print()
      print(f'O valor do litro é { self.valor_combustivel }')
      self.abastecer_litro()

    elif escolha == 'd':
      print()
      print(f'O valor do litro é { self.valor_combustivel }')
      self.abastecer_dinheiro()

  def abastecer_litro(self):
    litro = float(input('Digite a quantidade de litros: '))
    self.valor_pagar = litro * self.valor_combustivel

    if litro > self.quantidade_combustivel:
      print(f'Quantidade de litros insuficiente. A quantidade de litros da bomba é {self.quantidade_combustivel} litros. Digite novamente.')    
      self.abastecer_litro()

    else: 
        if self.quantidade_combustivel >= litro:
          print(f'Você vai pagar R${self.valor_pagar:.2f} em { litro } litros\n')
          self.quantidade_combustivel -= litro
          print(f'A quantidade de litros restantes da bomba é { self.quantidade_combustivel } litros\n')

        print('Automovel abastecido. Volte sempre. Obrigado!!!')
    
  def abastecer_dinheiro(self):
    dinheiro = float(input(f'Digite o valor que você quer de { self.tipo_combustivel }: '))
    litros_abastecidos = dinheiro / self.valor_combustivel

    if litros_abastecidos > self.quantidade_combustivel:
       print(f'Quantidade de litros insuficiente pro valor inserido. A quantidade de litros do bomba é {self.quantidade_combustivel} litros. Digite novamente.')  
       self.abastecer_dinheiro()

    else:
       if self.quantidade_combustivel >= litros_abastecidos:
         self.quantidade_combustivel -= litros_abastecidos
         print(f'Você vai pagar R${ dinheiro } em {litros_abastecidos:.2f} litros\n')  
         print(f'A quantidade de litros restantes da bomba é {self.quantidade_combustivel:.2f} litros\n')

    print('Automovel abastecido. Volte sempre. Obrigado!!!')  


posto = BombaGasolina(100)
posto.set_tipo_combustivel()
posto.escolha_cliente()