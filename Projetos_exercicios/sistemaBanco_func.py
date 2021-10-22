def credita(saldo):
    cred = float(input("Digite o valor a ser creditado: R$"))
    saldo += cred
    return saldo


def debita(saldo):
    deb = float(input('Digite o valor a ser debitado: R$'))
    saldo -= deb
    return saldo


def emprestimo(saldo):
    print('Olá nossa taxa de porcentagem hoje é de 10%')
    valor = float(input('Qual valor está querendo pedir? R$'))
    juros = 0.1
    valorFinal = valor+(valor*juros)
    print(f'Seu emprestimo de R${valor} ao final custará R${valorFinal}')
    while True:
        aceita = input('Aceita a proposta?(Digite sim ou não): ').lower()
        if aceita.startswith('s'):
            saldo -= valorFinal
            return saldo
        elif aceita.startswith('n'):
            print('Proposta negada')
            return saldo
        else:
            print('Valor incorreto')
            continue
