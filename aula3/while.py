valor = 11

while True:
    valor -= 1
    if valor % 2 != 0:
        continue  # Volta o loop para o começo
    if valor == 0:
        break

    print(f"Valor: {valor}")

print("Ufa! fora do loop")
