## Desafio DIO – Executando Tarefas Automatizadas com Lambda Function e S3

## Descrição
Projeto que demonstra automação de tarefas na AWS utilizando **AWS Lambda**, **Amazon S3**, **Amazon DynamoDB** e **API Gateway**.  
Fluxo: ao enviar um arquivo JSON para um bucket S3 (`notas-fiscais-upload`), um evento aciona a função Lambda (`ProcessarNotasFiscais`) que processa o arquivo e persiste os dados na tabela DynamoDB (`NotasFiscais`).

---

## Objetivos
- Demonstrar integração entre S3, Lambda e DynamoDB.
- Documentar o passo a passo de criação e teste dos recursos.
- Fornecer código e comandos para reprodução do fluxo.

---

## Recursos criados (nomes usados)
- Bucket S3: `notas-fiscais-upload`  
- Função Lambda: `ProcessarNotasFiscais`  
- Tabela DynamoDB: `NotasFiscais` (chave primária `id`)  
- API Gateway: `NotasFiscaisAPI` (endpoints POST e GET para interação via HTTP)


