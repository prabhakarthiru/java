
import boto3


# Create ACM client
acm = boto3.client('acm')

# Describe the specified certificate.
response = acm.describe_certificate
print(response)
