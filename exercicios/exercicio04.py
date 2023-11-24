# receba dois números e some e dê a opção de parar caso ela queira

while True:
  number1 = int(input('Digite um número: '))
  number2 = int(input('Digite um número: '))

  soma = number1 + number2
  print(f'A soma dos dois números é { soma }')

  para = input("Digite [S] para sair ou [C] para continuar: ")

  if para == 's' or para == 'S':
    break