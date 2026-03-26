# POC26_EventDrivenAutomation_with_S3_n_Lambda

# Architecture Flow (What you are building)

Upload File → S3 Bucket → Event Notification → Lambda → CloudWatch Logs
  - S3 detects file upload
  - Triggers Lambda
  - Lambda logs metadata
  - You verify in CloudWatch

# Step 1: Create S3 Bucket
Using AWS Console
Go to S3
Click Create bucket
Bucket name: poc-s3-lambda-trigger-<unique>
Region: same as Lambda (important)
Keep defaults → Create

# Step 2: Create IAM Role for Lambda
Lambda needs permission to write logs to CloudWatch
Steps:
Go to IAM → Roles → Create Role
Select:
Trusted entity: AWS Service
Use case: Lambda
Attach policies:
  - AWSLambdaBasicExecutionRole
  - (Optional) AmazonS3ReadOnlyAccess
Role name: lambda-s3-execution-role

# Step 3: Create Lambda Function
Option 1: Console (easy)
Go to Lambda → Create function
Select:
Author from scratch
Fill:
Function name: s3-event-logger
Runtime: Python 3.12
Execution role: Use existing → select your role

Note: Lambda Code (IMPORTANT) Paste this: lambda_function.py
This logs:
  - Full event (for learning)
  - File name
  - Bucket name
  - File size
Click Deploy

# Step 4: Configure S3 Trigger
Go to your S3 bucket
Properties tab
Scroll → Event notifications
Click Create event notification

Fill:
Name: s3-put-event
Event types: PUT (Object Created)
Destination: Lambda function → select s3-event-logger
Save

# Step 5: Test the Flow
Upload file:
Open S3 bucket
Click Upload
Upload any file (txt, jpg, etc.)

# Step 6: Verify in CloudWatch Logs
Go to CloudWatch → Logs
Log group: /aws/lambda/s3-event-logger
Open latest log stream
Expected Output
You will see logs like:
Full Event:
{
  "Records": [
    {
      "eventName": "ObjectCreated:Put",
      ...
    }
  ]
}    

And:
Bucket: poc-s3-lambda-trigger
File: test.txt
Size: 123 bytes


# Final Outcome
 - Upload file to S3
 - Lambda triggers automatically
 - Metadata logged in CloudWatch

