from cloudUtils import create_bucket, list_buckets

bucket = "demo-bucket"

print(f"Creando bucket: {bucket}")
create_bucket(bucket)

print("Buckets existentes:")
print(list_buckets())
