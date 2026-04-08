from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY  = os.getenv("STORAGE_ACCOUNT_KEY")

connection_string = (
    f"DefaultEndpointsProtocol=https;"
    f"AccountName={STORAGE_ACCOUNT_NAME};"
    f"AccountKey={STORAGE_ACCOUNT_KEY};"
    f"EndpointSuffix=core.windows.net"
)

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

print("=" * 55)
print("   BRONZE LAYER — INGESTION SUMMARY REPORT")
print("=" * 55)
print(f"   Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 55)

total_size = 0
total_files = 0

for container in ["bronze", "silver", "gold"]:
    container_client = blob_service_client.get_container_client(container)
    blobs = [b for b in container_client.list_blobs() if b.size > 0]
    size  = sum(b.size for b in blobs) / (1024 * 1024)
    total_size  += size
    total_files += len(blobs)
    print(f"\n📁 {container.upper()} LAYER:")
    if blobs:
        for blob in blobs:
            print(f"   ✅ {blob.name}")
            print(f"      Size: {blob.size/(1024*1024):.2f} MB")
            print(f"      Last Modified: {blob.last_modified.strftime('%Y-%m-%d %H:%M')}")
    else:
        print("   ⏳ Empty — data will be added in later phases")

print("\n" + "=" * 55)
print(f"   TOTAL FILES : {total_files}")
print(f"   TOTAL SIZE  : {total_size:.2f} MB")
print("=" * 55)