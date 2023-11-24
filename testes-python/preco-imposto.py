# List Comprehensions - uma maneira de construir listas no Python de forma mais rápida em uma linha de código

precos = [1000, 2000, 500, 400, 1500]

novos_precos = [preco * 2 for preco in precos] # utilização de list comprehensions para dobrar os preços
print(novos_precos)

imposto = [preco / 2 for preco in precos if preco > 1000] # utilização de list comprehensions com if para 50%  de redução sobre produtos acima de 1000 reais
print(imposto)