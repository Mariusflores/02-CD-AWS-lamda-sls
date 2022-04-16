import json
import boto3

def handler(event, context):

    client = boto3.client('comprehend')
    print("Received event: " + json.dumps(event, indent=2))
    body = event["body"]
    print ("Sentiment analysis on text", body)
    sentiment = client.detect_sentiment(LanguageCode = "en", Text = body)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "sentiment ": json.dumps(sentiment)
        })
    }