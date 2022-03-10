import json

def lambda_handler(envet, context):
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
  }
