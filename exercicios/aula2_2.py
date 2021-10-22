# Escreva um script em python que represente uma quitanda.
# O seu programa deverá apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta deverá ser adicionada a uma cesta de compras.
quitanda = {'Banana': 3.50,
            'Melancia': 7.50,
            'Morango': 5.00}

cesta = {}

print("Quitanda:\n1:Ver cesta\n2:Adicionar fruta\n3:Sair")
opcMenu = int(input('Digite a opção desejada:'))

while True:
    if opcMenu == 3:
        print('Até breve')
        break
    elif opcMenu == 1:
        print(cesta.count())

    elif opcMenu == 2:
        print(
            'Menu de frutas:\nEscolha uma fruta desejada:\n1 - Banana\n2 - Melancia\n3 - Morango')
        addFruta = int(input('Digite a opção desejada:'))
        if addFruta == 1:
            cesta.append("Banana", 3.50)
            print('Banana adicionada com sucesso')
        elif addFruta == 2:
            cesta.append("Melancia", 3.50)
            print('Melancia adicionada com sucesso')
        elif addFruta == 3:
            cesta.append("Morango", 3.50)
            print('Morango adicionada com sucesso')
        else:
            print('Opção incorreta')
