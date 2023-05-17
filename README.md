# AWS Assignment

## Task 1

### Create an IAM role with S3 full access.
- Open your terminal and type aws configure.
- Type your access key ID and password and type your region name.
- Create a file policy.json and add the AssumeRolePolicyDocument.
  
  ```{
		"Version": "2012-10-17",
		"Statement": {
			"Effect": "Allow",
				"Principal": {
					"Service": “s3.amazonaws.com”
					“AWS” : “arn:aws:iam::0039*****9674:user/pajji”
					},
			"Action": "sts:AssumeRole"
			}
		}
- Create an IAM role 
  
  ```aws iam create-role --role-name put-object-role --assume-role-policy-document file://path/to/file/policy.json```
- Add permission to the role 
  
  ```aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --role-name put-object-role```

### Create an EC2 instance with the above role.
- Open your terminal and type aws configure.
- Type your access key ID and password and type your region name.
- Use the role created above by typing
  
  ```aws sts assume-role --role-arn arn:aws:iam::0039*****9674:role/put-object-role --role-session-name my-session --duration-seconds 3600```
- Create an EC2 instance
  
  ```aws ec2 run-instances --image-id ami-0889a44b331db0194 --instance-type t2.micro --key-name secret-key --subnet-id subnet-0953ec6e2de22279d --security-group-ids sg-046ffd1222db8a6f3 --region us-east-1``` 

### Create a bucket from AWS CLI
- Open your terminal and type aws configure.
- Type your access key ID and password and type your region name.
- Type the following command and mention your unique bucket name and your region.

  ```aws s3api create-bucket --bucket aayusss2101-aws-assignment --region us-east-1```

## Task 2

### Create custom role for Lambda Function
- Search IAM in AWS Console.
- Under the Access Management section click on the Roles section.
- Click on Create Role and select AWS Service and Lambda.
- Search CloudWatchLogsFullAccess under the policies section and select it.
- Add your role name and click on create role.

### Lambda Function
- Open the AWS Lambda console and create a new Lambda function.
- Set the runtime to Python 3.x and choose a role with write access to S3.
- Copy and paste the code into the inline code editor.
- Save the function.
- Configure a test event with any event data to test the function.
- Code Explanation
  - Import necessary libraries.
  - Define the name of the S3 bucket and current timestamp as variables.
  - Create a dictionary object with some data to be written to S3.
  - Create an S3 client object using the Boto3 library.
  - Generate a filename with the current timestamp.
  - Convert the data dictionary to a JSON string.
  - Write the JSON string to an S3 object with the specified filename and bucket name.

## Task 3
- Open the AWS Lambda console and create a new Lambda function.
- Set the runtime to Python 3.x and choose a role with write access to S3.
- Copy and paste the code into the inline code editor.
- Save the function.
- Configure a test event with any event data to test the function.
- Code Explanation
  - The code imports the required modules: boto3 for AWS SDK, json for JSON manipulation, and datetime for timestamp generation.
  - The lambda_handler function is the entry point for the AWS Lambda function.
  - The BUCKET_NAME variable stores the name of the S3 bucket where the JSON file will be stored. Change this to your desired bucket name.
  - The current timestamp is generated using datetime.now() and converted to a string using str(datetime.now()).
  - The event parameter represents the event data passed to the Lambda function. The data variable is created as a copy of the event data.
  - A new key-value pair is added to the data dictionary, where the key is 'timestamp' and the value is the current timestamp.
  - The data dictionary is converted to a JSON string using json.dumps(data) and stored in the json_text variable.
  - An S3 client is created using boto3.client('s3').
  - A file name is generated by concatenating the current timestamp with the '.json' extension.
  - The JSON data is uploaded to the S3 bucket using s3_client.put_object(Body=json_text, Bucket=BUCKET_NAME, Key=file_name).
  - Finally, the function returns a dictionary containing the "file_name" key with the value of the generated file name.
