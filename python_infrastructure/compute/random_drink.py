import json

def lambda_handler(event, context):
    print("this is the event {}".format(event))
    print("this come from upload code")
    
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "success", "drink": "coke"})
    }