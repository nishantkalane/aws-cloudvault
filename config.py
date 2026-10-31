import boto3
from botocore.exceptions import ClientError

#Create a s3 client
AWS_REGION = "ap-southeast-2"

bucket_name = "cloudvalut-zeocephus-290181458576-ap-southeast-2-an"  # s3 bucket name


s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION
)