import csv

variavel_dicionario = [
    {
        "nome": "Ana",
        "idade": 25,
        "cidade": "São Paulo"
    },
    {
        "nome": "Pedro",
        "idade": 11,
        "cidade": "São Paulo"
    }
]

with open("exemplo2.csv", "w", newline="", encoding="utf-8") as variavel_arquivo:
    formatador_csv = csv.writer(variavel_arquivo)
    
    # escrevendo a primeira linha: cabeçalho (colunas)
    formatador_csv.writerow(variavel_dicionario[0].keys())
    
    # escrevendo a segunda linha: valores (linha)
    formatador_csv.writerow(variavel_dicionario[0].values())
    
    # escrevendo a segunda linha: valores (linha)
    formatador_csv.writerow(variavel_dicionario[1].values())

