import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('dolar-raw-3003')
    obj = bucket.Object('dollar_timestamp.txt')
    body = obj.get()['Body'].read()
    todo_item = json.loads(body)

    resu = "fechahora, valor\n"
    for i in todo_item:
        dt = datetime.fromtimestamp((int(i[0])/1000))
        resu += "{}, {}\n".format(dt, i[1])
    
    client = boto3.client("s3")
    client.put_object(Body=resu, Bucket="dolar-final-3003",Key="dollar_timestamp.csv")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
