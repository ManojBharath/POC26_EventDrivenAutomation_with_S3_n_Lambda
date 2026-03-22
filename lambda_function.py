import json

def lambda_handler(event, context):
    print("Full Event:")
    print(json.dumps(event, indent=2))
    
    # Extract useful info
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']
        
        print(f"Bucket: {bucket}")
        print(f"File: {key}")
        print(f"Size: {size} bytes")

    return {
        'statusCode': 200,
        'body': 'Success'
    }
