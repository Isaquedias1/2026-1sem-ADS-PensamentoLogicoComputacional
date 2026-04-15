variavel_dicionario_lido = {}

with open("exemplo2-dicionario.txt", "r", encoding="utf-8") as variavel_arquivo:
    for linha in variavel_arquivo:
        chave, valor = linha.strip().split(":")
        if valor.isdigit():
            valor = int(valor)        
        variavel_dicionario_lido[chave] = valor

print(variavel_dicionario_lido)
