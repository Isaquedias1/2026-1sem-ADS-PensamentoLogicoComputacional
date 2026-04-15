variavel_dicionario = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

with open("exemplo2-dicionario.txt", "w") as variavel_arquivo:

    for chave, valor in variavel_dicionario.items():
        variavel_arquivo.write(f"{chave}:{valor}\n")
