users_dados = []
while True:
  user_name = input("Digite seu nome: ")
  user_cpf = input("Digite seu CPF: ")

  list_tuple = (user_name, user_cpf)

  if list_tuple not in users_dados:
    users_dados.append(list_tuple)
  elif user_name in users_dados:
    print("Esse usuário já existe")

  if list_tuple not in users_dados:
    users_dados.append(list_tuple)
  elif user_cpf in users_dados:
    print("Este CPF já existe")
  
  contador = int(input("Digite [-1] para inserir outro usuário ou [-2 para finalizar]: "))
  if contador == -1:
    continue
  elif contador == -2:
    break
  print("Sessão finalizada")
print(users_dados)


'''users_dados = []
while True:
    
    user_name = input("Digite seu nome: ")
    user_cpf = input("Digite seu CPF: ")

    user_tuple = (user_name, user_cpf)

    if user_tuple in users_dados:
        print("Essa combinação de nome e CPF já existe.")
    else:
        users_dados.append(user_tuple)

    contador = int(input("Digite [-1] para inserir outro usuário ou [-2 para finalizar]: "))

    if contador == -1:
        continue
    elif contador == -2:
        break

print("Sessão finalizada")
print("Dados cadastrados:", users_dados)
print(type(user_tuple))'''