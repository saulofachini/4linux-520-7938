listaCursos = {}
listaTurma = []

class Curso:
  def __init__(self):
    self.__curso = {}

  def adicionarCurso(self, idCurso, nomeCurso):
    self.__curso.values(idCurso, nomeCurso)


  def __repr__(self):
    return repr(f'{self.__curso}')


class Turma:
  def __init__(self):
    self.__turma = {}

  def adicionaTurma(self, idTurma,nomeTurma):
    self.__curso[idTurma] = nomeTurma


  def __repr__(self):
    return repr(f'{self.__turma}')

def main():
  menu_principal = '1 - Adicionar Curso\n2 - Adicionar Turma\n3 - Adicionar Aluno\n4 - Listar Cursos\n5 - Listar Turmas\n6 - Sair\nDigite a opção: '
  varCursos = Curso()
  varTurma = Turma()

  while True:
    entrada = int(input(menu_principal))

    if entrada == 1:
      idCurso = int(input('Insira o id do Curso: '))
      nomeCurso = input('Insira o nome do Curso: ')
      varCursos.adicionarCurso(idCurso,nomeCurso)

    elif entrada == 2:
      idTurma = int(input('Insira o id da Turma: '))
      nomeTurma = input('Escolha um Curso: ')
      varTurma.adicionaTurma(idTurma,nomeTurma)

    elif entrada == 3:
      continue

    elif entrada == 4:
      print(varCursos)

    elif entrada == 5:
      print(varTurma)

    elif entrada == 6:
      break

    else:
      print('Digite uma opção válida')


if __name__ == '__main__':
  main()