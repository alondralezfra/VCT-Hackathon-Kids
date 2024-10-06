import boto3
import json
brt = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

body = json.dumps({
    "prompt": "\n\nHuman: explain black holes to 8th graders\n\nAssistant:",
    "max_tokens_to_sample": 1000,
    "temperature": 0.1,
    "top_p": 0.9,
})

modelId = 'mistral.mistral-7b-instruct-v0:2'
accept = 'application/json'
contentType = 'application/json'

response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())


print(response_body.get('completion'))