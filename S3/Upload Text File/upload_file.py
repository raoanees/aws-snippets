import boto3
import sys


#Usage: python upload_file.py sample_file.txt presize-landing-dev sample_file_on_s3.txt
Key = sys.argv[1]
bucketName = sys.argv[2]
outPutname = sys.argv[3]

s3_client = boto3.client('s3')
s3_client.upload_file(Key,bucketName,outPutname)
