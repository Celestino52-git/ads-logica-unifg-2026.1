idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite seus anos de experiência profissional: "))
acesso_liberado = (idade >= 18) and (experiencia > 2)
print("Acesso Liberado:", acesso_liberado)