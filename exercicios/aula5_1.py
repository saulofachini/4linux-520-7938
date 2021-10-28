# 1) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’ tem em sua letra. 
# Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.
vogais = {
  'a':0,
  'e':0,
  'i':0,
  'o':0,
  'u':0
}

def read_vogal(arquivo):
  with open(arquivo) as arq:
    contador = arq.read().lower()
    vogais['a'] = contador.count('a')
    vogais['e'] = contador.count('e')
    vogais['i'] = contador.count('i')
    vogais['o'] = contador.count('o')
    vogais['u'] = contador.count('u')
    print(vogais)

if __name__ == '__main__':
  read_vogal("musica.txt")