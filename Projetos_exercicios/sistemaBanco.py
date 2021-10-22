# Projeto consiste em simular um caixa eletronico
import sistemaBanco_func as sysFunc

saldo = 0
print("Bem vindo ao sistema de caixa eletronico")
while True:
    print("1 - Creditar saldo\n2 - Debitar saldo\n3 - Pedir emprestimo\n4 - Sair")
    print(f'Seu saldo é de R${saldo}')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        saldo = sysFunc.credita(saldo)
        continue
    elif opcao == 2:
        saldo = sysFunc.debita(saldo)
        continue
    elif opcao == 3:
        saldo = sysFunc.emprestimo(saldo)
        continue
    elif opcao == 4:
        print('Obrigado por utilizar nossos serviços')
        break
    else:
        print('Nao existe esta opção\n')
        continue
