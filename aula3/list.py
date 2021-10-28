nomes = [
    'Italo',
    'Vinicius',
    'Saulo',
    'Edilson',
    'Edson',
    'Dalton',
    'Paulo Roberto'
]

nomes_copia = nomes.copy()
nomes_copia.clear()

print('nomes copia:', nomes_copia)
print('index of Edson: ', nomes.index('Edson'))
nomes.insert(3, 'Fabio Silva')
print('pós insert', nomes)
print('list popada', nomes.pop())
print('pós pop', nomes)
print('pós popada (index 2):', nomes.pop(2))
print('pós pop index 2:', nomes)
nomes.remove('Italo')
print('pós remove Italo', nomes)
nomes.reverse()
print('pós reverse:', nomes)
nomes.sort(reverse=True)
print("Pós sort reversed: ", nomes)

print("sobreviventes:")
for i in nomes:
    print(i)
