# a função pesquisa_binaria recebe uma lista ordenada e um item a ser pesquisado
# se o item estiver no array, a função retorna o índice do item

def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) - 1

	while baixo <= alto:
		meio = int((baixo + alto)/2)
		chute = int(lista[meio])
		if chute == item:
			return meio
		elif chute > item:
			alto = meio - 1
		else:
			baixo = meio + 1
	return None

lista = [1, 3, 4, 6, 7, 8, 9]
item = 9

print(pesquisa_binaria(lista, item))

