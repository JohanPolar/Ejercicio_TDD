import json
import boto3
from urllib.request import urlopen

def lambda_handler(event, context):
    # TODO implement
    url = "https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario"
    with urlopen(url) as response:
        body = response.read()
    client = boto3.client("s3")
    client.put_object(Body=body, Bucket="dolar-raw-3003",Key="dollar_timestamp.txt")
    
    return {
        'statusCode': 202,
        'body': json.dumps('Hello from Lambda!')
    }
