from os import truncate


operacoes = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'divisao': lambda a, b: a / b,
    'multiplicacao': lambda a, b: a * b,
}

print(f'Escolha a operacao')
operacoes_ks = list(operacoes.keys())
for (i, opc) in enumerate(operacoes_ks):
    print(f'{i}: {opc}')

# entrada = int(input('Escolha uma operaçao:'))
# valor1 = int(input('Digite o valor 1:'))
# valor2 = int(input('Digite o valor 2:'))

calcula = map(operacoes.keys['soma'], 10, 10)
print(list(calcula))
