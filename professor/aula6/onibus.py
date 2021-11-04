class Onibus():
  capacidadeTotal = 45
  def __init__(self, cAtual, velocidade, placa, modelo):
    self.__cAtual = cAtual
    self.__velocidade = velocidade
    self.__placa = placa
    self.__modelo = modelo

  def __repr__(self):
    if not self.__cAtual > self.capacidadeTotal:
      return repr(f'Total passageiros: {self.__cAtual}  Capacidade maxima: {self.capacidadeTotal}')
    else:
      return repr('Capacidade atual maior que o capacidade maxima')

  def acelerar():
    pass

  def frear():  
    pass

  def embarcar():
    pass
  
  def desembarcar():
    pass

def main():
  varPassageiro = int(input('Digite a quantidade de passageiros atual: '))
  varVelocidade = int(input('Digite a velocidade atual: '))
  varPlaca = input('Digite a placa: ')
  varModelo = input('Digite o modelo do Veiculo: ')

  busao = Onibus(varPassageiro, varVelocidade,varPlaca,varModelo)
  print (busao)

if __name__ == '__main__':
  main()