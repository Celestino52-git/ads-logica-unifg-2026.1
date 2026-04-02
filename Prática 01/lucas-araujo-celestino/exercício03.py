numero_fatias = int(input("digite o número de pizzas"))
numero_programadores = int(input("digite o número de programadores"))
total_fatias = numero_fatias - numero_programadores
sobras = total_fatias %  numero_programadores
print(f"você dividiu as pizzas em {sobras} para {numero_programadores} programadores!")