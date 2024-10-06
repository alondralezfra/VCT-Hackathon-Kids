import boto3
import os

#change the keys to yours
os.environ["AWS_ACCESS_KEY_ID"] = "Access Key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "Secret Key"


client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "mistral.mistral-large-2402-v1:0"

user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]



response = client.converse(
    modelId=model_id,
    messages=conversation,
    inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
)


response_text = response["output"]["message"]["content"][0]["text"]
print(response_text)
