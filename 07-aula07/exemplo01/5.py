import json

variavel_dicionario = [ 
    { "nome": "Ana",   "idade": 25,"cidade": "São Paulo" },
    { "nome": "Pedro", "idade": 11,"cidade": "São Paulo" }
]

with open("exemplo5.json", "w", encoding="utf-8") as variavel_arquivo:
    json.dump(variavel_dicionario, variavel_arquivo, ensure_ascii=False, indent=4)

