from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Step 1: Set up your Azure storage connection string
connection_string = 'DefaultEndpointsProtocol=https;AccountName=teststoragehha504;AccountKey=EVzjHy0f5NvFksYT3yfhbTHKHmtg7pKm14tRj7SMrhvEoy/1s8bTn52YuRb411gj3iI7FXSswR0Z+ASt5O4N0A==;EndpointSuffix=core.windows.net'  # Replace with your Azure Storage connection string

# Step 2: Create a BlobServiceClient object using the connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Step 3: Specify your container name (make sure this exists in your storage account)
container_name = 'sample-container'  # Replace with your container name
container_client = blob_service_client.get_container_client(container_name)

# Step 4: Use full paths for the specific files you want to upload
files_upload = [
    r'C:\Users\shvet\OneDrive\Desktop\SBU Fall2024\HHA504_Assignments\module 6\Viral Pneumonia-1.png',
    r'C:\Users\shvet\OneDrive\Desktop\SBU Fall2024\HHA504_Assignments\module 6\Viral Pneumonia-1020.png'
]

# Step 5: Upload the specific PNG files
for file in files_upload:
    print(f"Working on {file}")
    
    with open(file, 'rb') as f:
        file_byte_array = f.read()

    file_name = file.split("\\")[-1]  # Extract just the file name
    print('New file name:', file_name)

    # Upload the file to Azure Blob Storage
    try:
        blob_client = container_client.get_blob_client(file_name)
        blob_client.upload_blob(file_byte_array, overwrite=True)
        print(f"Image {file_name} uploaded successfully to Azure Blob Storage!")
    except Exception as e:
        print(f"Error: {e}")

print("All files uploaded successfully to Azure Blob Storage!")
