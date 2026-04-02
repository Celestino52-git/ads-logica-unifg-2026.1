
valor_hora = float(input("Digite o valor cobrado por hora: "))
horas_estimadas = float(input("Digite a estimativa de horas do projeto: "))


valor_bruto = horas_estimadas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos


print("-" * 30)
print(f"Valor Bruto: R$ {valor_bruto:.2f}")
print(f"Impostos (15%): R$ {impostos:.2f}")
print(f"Valor Líquido: R$ {valor_liquido:.2f}")
print("-" * 30)
