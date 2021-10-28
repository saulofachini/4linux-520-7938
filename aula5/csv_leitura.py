import csv

def main():
    nome_arq = 'aula5/dados.csv'

    with open(nome_arq) as a:
        leitor = csv.reader(a, delimiter=';')

        print(leitor)

        for linha in leitor:
            print(linha)


if __name__ == '__main__':
    main()