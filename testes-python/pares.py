# Utilizando list comprehensions para encontrar números pares

inteiros = [1, 3, 4, 5, 6, 8, 10, 13, 14, 15]
pares = [numero for numero in inteiros if numero % 2 == 0] # o if depois do for define a condição
print(f'Os números pares são { pares }')

#Encontrando números pares usando for da forma tradicional
pares2 = []
for numero in inteiros:
  if numero % 2 == 0:
    pares2.append(numero)
print(pares2)