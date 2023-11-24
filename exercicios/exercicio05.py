# Faça um programa que declara uma varável chamada continua e execte um laço while, enquanto a variávle for igual a 's' dentro o usuário deve digitar um número e o progrma deve imprimir o dobro do número, e após isso perguntar se quer continuar ou não

continua = 's'
while continua == 's' or continua == 'S':
  number_user = int(input('Digite um número: '))

  print(f'O dobro do número { number_user } é {number_user * 2}')
  
  saida = input('Digite [n] para sair ou [s] para continuar: ')
  if saida == 'n' or saida == 'N':
    continua = saida 