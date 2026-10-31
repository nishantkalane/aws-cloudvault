from config import s3_client, bucket_name
from botocore.exceptions import ClientError

def list_files():
    try:
        #listing objects : sending an api request  to s3 asking for objects inside bucket

        response = s3_client.list_objects_v2(Bucket =  bucket_name)

        #extracting the objects
        objects = response.get("Contents", [])


        #get() gets the contents filed from response dictionary containing the aws response.

        if not objects: # if objects are not there
            print("The S3 bucket is empty!")
            return
        # iterate and print the required attribute
        for obj in objects:
            print(obj["Key"],obj["Size"])

    except ClientError as e:
        print("AWS Error: ", e)

def upload(local_file, s3_object_name):
    try:
        s3_client.upload_file( #upload_file is boto3 high level transfer method
            local_file, #file on your computer
            bucket_name, # Destination S3 Bucket
            s3_object_name #name of the object in S3
        )

        print("File uploaded successfully!")
    except ClientError as e:
        print("AWS Error:", e)
    except FileNotFoundError:
        print("Error: THe local file does not exist!")

def download(s3_object_name, local_file):
    try:
        s3_client.download_file(
            bucket_name, # AWS s3 bucket
            s3_object_name, # File's name (S3 Key) in the bucket
            local_file # Where to save the downloaded file on your computer
        )
        print("File downloaded successfully!")
    except ClientError as e:
        print("AWS Error:",e)
    except OSError as e:
        print("Local file error:", e)



def delete(s3_object_name):
    try:
        s3_client.delete_object(
            Bucket = bucket_name,
            Key = s3_object_name
        )
        print("File deleted Successfully")
    except ClientError as e:
        error_code = e.response["Error"]["Code"]

        if error_code in ["404", "NoSuchKey", "NotFound"]:
            print("Error: File does not exist in S3!")

        else:
            print("AWS Error:", e)
