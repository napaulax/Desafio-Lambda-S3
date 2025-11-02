import json
from datetime import date

dados = {
    "id": "NF-001",
    "cliente": "Cliente Exemplo",
    "valor": 150.0,
    "data_emissao": str(date.today())
}

with open('notas_fiscais_2025.json', 'w') as f:
    json.dump(dados, f, indent=4)

print('Arquivo notas_fiscais_2025.json gerado!')
