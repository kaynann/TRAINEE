# Fazer 10 questões em um codigo e dizer se esta correto ou errado
q1 = 6
q2 = 2
q3 = 3
q4 = 4
q5 = 5
q6 = 6
q7 = 7
q8 = 8
q9 = 9
q10 = 10
questoes = q1, q2, q3, q4, q5, q6, q7, q8, q9, q10

for i in questoes:
    response = int(input('Digite o valor: '))
    if response == i:
        print('Você acertou!')
    else:
        print('Você errou.')