# 1) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’ tem em sua letra. 
# Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.

def contar_vogais():
  vogais = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
  }

  return vogais

def main(arquivo):
  with open(arquivo, 'r') as arq:
        contador = arq.read()
        # contador = arq.readlines()
        print(contador)


if __name__ == '__main__':
    main("musica.txt")