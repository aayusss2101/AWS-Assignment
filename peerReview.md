# Peer Review

## Pankaj Kumar Singh
- In Task 1, the code successfully creates an IAM role, attaches a policy, creates an S3 bucket, and launches an EC2 instance. The code is concise and uses appropriate method calls to achieve the desired actions. 
- In Task 2, the code imports the necessary libraries, generates a JSON object with transaction details, uploads the JSON file to an S3 bucket, and publishes a log message to CloudWatch Logs. The code appropriately handles exceptions and includes log group and log stream creation if they don't exist. The naming conventions for the S3 bucket, key name, log group, and log stream are clear and meaningful.
- In Task 3, the code imports the necessary libraries, parses input data, generates a timestamp, uploads a JSON file to an S3 bucket, and prints a log message. The exception handling is well-implemented, and the code returns an appropriate response dictionary based on the execution status. The use of timestamps in the key name and JSON data ensures uniqueness and organization.

## Jasveen Singh Kohli
- In Task 1, the IAM role with S3 full access is created accurately by following the specified steps in the AWS CLI. The process is well-documented and enables the user to easily create the required IAM role for subsequent use.
- Task 2 demonstrates proficient usage of necessary libraries, such as json, boto3, and datetime. The code successfully generates a current timestamp, constructs a JSON-formatted string from transaction details, and uploads it to the specified S3 bucket. The naming conventions for variables and objects are meaningful and contribute to the code's readability.
- Task 3 showcases the effective utilization of libraries, including json, boto3, and datetime. The lambda_handler function appropriately handles the event data, adds a timestamp to the JSON body, and uploads the data to the specified S3 bucket. The use of unique file names for each upload ensures data integrity and avoids overwriting existing files.
