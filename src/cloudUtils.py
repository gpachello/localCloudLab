import boto3

def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url="http://localstack:4566",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1",
    )

def create_bucket(bucket_name: str):
    s3 = get_s3_client()
    s3.create_bucket(Bucket=bucket_name)

def list_buckets():
    s3 = get_s3_client()
    resp = s3.list_buckets()
    return [b["Name"] for b in resp.get("Buckets", [])]
