# 2) Escreva um programa em python que realize um cadastro. Deverão ser coletadas as seguintes informações:
# • CPF
# • Nome
# • Idade
# • Sexo
# • Endereço

import json

def cadastrar():
  lista = {}

  for campo in ('cpf','nome','idade', 'sexo', 'endereco'):
    lista[campo] = input(f'Insira o {campo.upper()}:').strip()
  return lista

def salvar(dados, arquivo):
    json.dump(dados, arquivo, indent=4)

def carregar(arquivo):
    return json.load(arquivo)

def main():
  nome_arquivo = 'exercicios/registro.json'

  with open(nome_arquivo) as arq:
    registro = carregar(arq)
  
  registrar = cadastrar()

  registro['registros'].append(registrar)

  with (nome_arquivo, 'w') as escrever:
    salvar(registro,escrever)

if __name__ == '__main__':
  main()