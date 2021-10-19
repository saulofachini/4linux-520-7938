habilitado = input("Você é habilitado?").lower().strip()

if habilitado.startswith('s'):
    print("Voce esta autorizado a dirigir")
elif habilitado.startswith('n'):
    print("Voce não deve dirigir")
else:
    print("Não entendi... kkk")
