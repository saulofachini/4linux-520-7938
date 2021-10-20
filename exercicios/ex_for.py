string = input('insira um texto:')

for i in string:
    if i.isupper():
        print(i, "- é maisculo")
    elif i.islower():
        print(i, "- é minusculo")
    elif i.isnumeric():
        print(i, "- é numerico")
    else:
        print(i, "- é alguma outra coisa")
