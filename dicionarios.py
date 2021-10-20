telefones = {
    'Saulo': '1234567890',
    'Diego': '98765431',
    'Fabricio': '748574835'
}

atualizacao = {'Valeria': '393939393', 'Chupim': '666666666'}
telefones.update(atualizacao)

print(telefones.items())

numeroDiego = telefones.pop('Diego')
print(numeroDiego)

print(telefones.keys())

print(telefones.get('Fabricio'))
