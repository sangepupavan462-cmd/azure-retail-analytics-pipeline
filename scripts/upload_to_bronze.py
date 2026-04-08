import pandas as pd
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY  = os.getenv("STORAGE_ACCOUNT_KEY")
CONTAINER_NAME       = "bronze"
LOCAL_FILE           = "data/retail_raw.csv"
BLOB_PATH            = "retail/2010-2011/retail_raw.csv"

print("🔌 Connecting to Azure Data Lake...")
connection_string = (
    f"DefaultEndpointsProtocol=https;"
    f"AccountName={STORAGE_ACCOUNT_NAME};"
    f"AccountKey={STORAGE_ACCOUNT_KEY};"
    f"EndpointSuffix=core.windows.net"
)

blob_service_client = BlobServiceClient.fr