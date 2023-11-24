precos = [1000, 2000, 500, 400, 1500]
novos_precos = [preco * 2 for preco in precos]
print(novos_precos)

imposto = [preco / 2 for preco in precos if preco > 1000]
print(imposto)