string = input('insira um texto:')

for i in string:
    if i == i.lower():
        print(i, "- é minisculo")
    elif i == i.upper():
        print(i, "- é maisculo")
    else:
        print(i, "- é numero ou outra coisa")
