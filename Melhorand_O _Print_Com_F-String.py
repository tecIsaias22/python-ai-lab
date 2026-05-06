Nome = input("Digite seu nome: ")
Idade = input("Digite sua idade: ")
fruta_favorita = input("Digite sua fruta favorita: ")

# Usando f-strings para formatar a mensagem
print(f"1 Olá, {Nome}! Você tem {Idade} anos e sua fruta favorita é {fruta_favorita}.")

#Sem f-strings
print("2 Olá, " + Nome + "! Você tem " + str(Idade) + " anos e sua fruta favorita é " + fruta_favorita + ".")

# Usando f-strings
print(f"3 Olá {Nome}! Daqui a 5 anos, você terá {int(Idade) + 5} anos.")