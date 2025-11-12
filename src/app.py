from aws_utils import create_bucket, list_buckets
from azure_utils import create_container, list_containers

if __name__ == "__main__":
    print("=== AWS (LocalStack) ===")
    create_bucket("test-bucket")
    list_buckets()

    print("\n=== Azure (Azurite) ===")
    create_container("test-container")
    list_containers()
