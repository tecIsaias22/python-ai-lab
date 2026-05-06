Nome = input("Digite seu nome: ")
Idade = int(input("Digite sua idade: "))

print(type(Nome))
print(type(Idade))
# Usando f-strings
print(f"3 Olá {Nome}! Daqui a 5 anos, você terá {Idade + 5} anos.")
# ou 
# Usando f-strings
print(f"4 Olá {Nome}! Daqui a 5 anos, você terá {int(Idade) + 5} anos.")

Numero1 = 10
Numero2 = 2
Novo_Preco = Numero1 - (Numero1 * Numero2 / 100)

print(Numero1 + Numero2)  # Soma
print(Numero1 - Numero2)  # Subtração 
print(Numero1 * Numero2)  # Multiplicação
print(Numero1 / Numero2)  # Divisão
print(Numero1 // Numero2) # Divisão inteira
print(Numero1 % Numero2)  # Resto da divisão
print(Numero1 ** Numero2) # Potenciação

print(f"Novo_Preco_Com_Desconto: {Novo_Preco}") 

Num1 = int(input("Digite O Valor: "))
Num2 = int(input("Digite O desconto (%): "))

Desconto = Num1 * (Num2 / 100)
Valor_Com_Desconto = Num1 - Desconto
print(f"Valor_Com_Desconto: {Valor_Com_Desconto}")

Quantidade_Total = int(input("Digite a quantidade total de porções: "))
Porcoes_Por_Dia = int(input("Digite quantas porções são usadas por dia: "))

Dias_De_Duracao = Quantidade_Total / Porcoes_Por_Dia

print(f"O produto vai durar {Dias_De_Duracao} dias")
