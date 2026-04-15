variavel_lista_1 = ['fulano', 'ciclano', 'beltrano']

with open("exemplo1-lista.txt", "w") as variavel_arquivo:
    for indice in variavel_lista_1:
        variavel_arquivo.write(str(indice) + "\n")
