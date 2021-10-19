anoNascimento = int(input("Digite o seu ano de nascimento: "))
if anoNascimento <= 1964:
    print("Geração Baby boomer")
elif anoNascimento >= 1965 and anoNascimento <= 1979:
    print("Geração X")
elif anoNascimento >= 1980 and anoNascimento <= 1994:
    print("Geração Y")
else:
    print("Geração Z")
