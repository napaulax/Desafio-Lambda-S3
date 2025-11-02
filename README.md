# Desafio DIO - Executando Tarefas Automatizadas com Lambda Function e S3

## 🎯 Objetivo
Este projeto demonstra a automação de tarefas utilizando **AWS Lambda**, **Amazon S3** e **DynamoDB**.
Fluxo: envio de arquivo JSON para um bucket S3 (`notas-fiscais-upload`) -> S3 aciona Lambda (`ProcessarNotasFiscais`) -> Lambda grava dados na tabela DynamoDB (`NotasFiscais`).

> Observação: Este repositório é uma **simulação/documentação** do fluxo. As imagens na pasta `/images` são mockups realistas do console AWS para fins ilustrativos.

## Estrutura do repositório
```
desafio-lambda-s3/
├── README.md
├── lambda/
│   └── lambda_function.py
├── scripts/
│   ├── gerar_dados.py
│   ├── notification_roles.json
│   └── comandos_aws.txt
└── images/
    ├── s3_console.png
    ├── lambda_console.png
    └── apigateway_console.png
```

## Como testar (local, opcional)
Se quiser reproduzir localmente, use LocalStack via Docker e os comandos em `scripts/comandos_aws.txt`.

## Recursos criados (nomes usados nesta documentação)
- Bucket S3: `notas-fiscais-upload`
- Lambda: `ProcessarNotasFiscais`
- DynamoDB: `NotasFiscais`
- API Gateway: `NotasFiscaisAPI`

## Instruções básicas (resumo)
1. Gerar arquivo de testes: `python scripts/gerar_dados.py`
2. (LocalStack) Criar recursos usando os comandos em `scripts/comandos_aws.txt`
3. Enviar arquivo de teste para o bucket S3 e verificar DynamoDB
4. Verificar logs e confirmações no console (simulado nas imagens)

---
Este material foi preparado como entrega de exercício prático para fins educacionais.
