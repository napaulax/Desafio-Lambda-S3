import json
import boto3

# Ao rodar em LocalStack, configure boto3 para apontar para http://localhost:4566

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
table = dynamodb.Table('NotasFiscais')


def lambda_handler(event, context):
    # Suporta eventos do API Gateway (proxy) com httpMethod e body
    if 'httpMethod' in event:
        method = event['httpMethod']
        if method == 'POST':
            body = json.loads(event.get('body', '{}'))
            table.put_item(Item=body)
            return {'statusCode': 200, 'body': json.dumps({'message': 'Nota adicionada', 'item': body})}
        elif method == 'GET':
            resp = table.scan()
            return {'statusCode': 200, 'body': json.dumps({'items': resp.get('Items', [])})}

    # Suporta eventos do S3 (quando um arquivo é enviado)
    if 'Records' in event:
        for record in event['Records']:
            # caso o evento venha via SQS/SNS ou diretamente do S3, adaptar conforme necessário
            body = record
            # simplificação: assume que o corpo já é o JSON desejado
            try:
                data = json.loads(record.get('body', '{}'))
            except Exception:
                data = record
            if isinstance(data, dict) and 'id' in data:
                table.put_item(Item=data)
        return {'statusCode': 200, 'body': json.dumps('Processado com sucesso')}

    return {'statusCode': 400, 'body': json.dumps('Evento não reconhecido')}
