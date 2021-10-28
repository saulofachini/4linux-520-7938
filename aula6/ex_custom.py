class curso:
  def __init__(self):
    self.__curso = {}

  def adicionarCurso(self, idCurso, nomeCurso):
    self.__curso[idCurso] = nomeCurso

  def __repr__(self):
    return repr(f'{self.__curso}')
  
  def listarCursos():
      pass


class turma:
  def __init__(self):
    pass


def main():
  menu_principal = '1 - Adicionar Curso\n2 - Adicionar Turma\n3 - Adicionar Aluno\n4 - Sair\nDigite a opção: '
  cursos = curso()

  while True:
    entrada = int(input(menu_principal))

    if entrada == 1:
      idCurso = int(input('Insira o id do Curso: '))
      nomeCurso = input('Insira o nome do Curso: ')
      cursos = cursos.adicionarCurso(idCurso,nomeCurso)
      print(cursos)

    elif entrada == 2:
      continue
      # input('Qual turma ele pertence?')

    elif entrada == 3:
      continue

    elif entrada == 4:
      break

    else:
      print('Digite uma opção válida')


if __name__ == '__main__':
  main()