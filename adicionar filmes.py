contador=1
qt_filmes=int(input('digite a quantidade de filmes:'))
filmes = []
while contador<=qt_filmes:
    nome_filme=input(f'digite o nome do filme {contador}: ')
    contador=contador+1
    filmes.append(nome_filme)

print(filmes)





