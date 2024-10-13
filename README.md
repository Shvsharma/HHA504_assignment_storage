# HHA504_assignment_storage

## Overview
The goal of this assignment was to work with cloud storage services on both **Google Cloud Platform (GCP)** and **Azure Blob Storage**. The assignment involved uploading files to cloud storage using both the graphical user interface (GUI) and Python scripts. I also explored various management and security features, such as access policies, storage tiers, and lifecycle management for optimizing data storage and securing access.

### Steps:
1. Created a **Cloud Storage bucket** on GCP
   
![Screenshot 2024-10-13 085827](https://github.com/user-attachments/assets/a5600d2f-7fb7-4135-a7e4-b9d44b07056b)

2. Uploaded `.png` files using the **GCP Console** (GUI).
   
3. Used Python to upload the `.png` files programmatically using the `google-cloud-storage` library.

### Python Code:
```
from google.cloud import storage
from PIL import Image
import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"'C:\path_to_your_gcp_credentials'"


client = storage.Client()


bucket_name = 'sharma-ahi-dummy-demo'
bucket = client.bucket(bucket_name)


files_upload = []
for root, dirs, files in os.walk("images"):
    for file in files:
        files_upload.append(os.path.join(root, file))

for file in files_upload:
    print(f"Working on {file}")
    with open(file, 'rb') as f:
        file_byte_array = f.read()
    
    file_name = file.split("/")[-1]  
    print('New file name:', file_name)

    
    try:
        blob = bucket.blob(file_name)
        blob.upload_from_string(file_byte_array, content_type='image/png')
        print(f"Image {file_name} uploaded successfully to Google Cloud Storage!")
    except Exception as e:
        print(f"Error: {e}")


image = Image.new('RGB', (100, 100), color = (73, 109, 137))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')


blob = bucket.blob('Viral Pneumonia-1.png')
blob.upload_from_string(image_byte_array.getvalue(), content_type='image/png')

print("Image uploaded successfully to Google Cloud Storage!")
```
![Screenshot 2024-10-13 110628](https://github.com/user-attachments/assets/2d540ce5-3b67-418d-bee7-93bd41ed73b3)


## Azure Blob Storage

### Steps:
1. Created a **Storage Account** and **Blob container** on Azure.
![Screenshot 2024-10-13 112700](https://github.com/user-attachments/assets/af2c9b35-ce7e-4616-8d53-cd7a99e00541)


2. Uploaded `.png` files using the **Azure Portal** (GUI).

3. Used Python to upload the `.png` files programmatically using the `azure-storage-blob` library.

### Python Code:
```
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os


connection_string = your_azure_storage_connection_string


blob_service_client = BlobServiceClient.from_connection_string(connection_string)


container_client = blob_service_client.get_container_client(container_name)


files_upload = [
    r'C:\Users\shvet\OneDrive\Desktop\SBU Fall2024\HHA504_Assignments\module 6\Viral Pneumonia-1.png',
    r'C:\Users\shvet\OneDrive\Desktop\SBU Fall2024\HHA504_Assignments\module 6\Viral Pneumonia-1020.png'
]


for file in files_upload:
    print(f"Working on {file}")
    
    with open(file, 'rb') as f:
        file_byte_array = f.read()

    file_name = file.split("\\")[-1]  
    print('New file name:', file_name)

   
    try:
        blob_client = container_client.get_blob_client(file_name)
        blob_client.upload_blob(file_byte_array, overwrite=True)
        print(f"Image {file_name} uploaded successfully to Azure Blob Storage!")
    except Exception as e:
        print(f"Error: {e}")

print("All files uploaded successfully to Azure Blob Storage!")
```
![Screenshot 2024-10-13 114612](https://github.com/user-attachments/assets/2703a14e-5e73-4c4d-9283-ec27606bcaa1)

## Storage Management and Security Features

### Azure Blob Storage:

1. **Access Policies**:
   - Managed **private** and **public access** levels for the blob container.

2. **Storage Tiers**:
   - Utilized **Hot**, **Cool**, and **Archive** tiers to manage storage costs based on the frequency of access.

3. **Security**:
   - Configured **network restrictions** using IP-based firewall rules.

---

### GCP Cloud Storage:

1. **IAM Permissions**:
   - Assigned specific **IAM roles** like **Storage Admin** and **Editor** to manage access control at the bucket level.

2. **Lifecycle Rules**:
   - Created **lifecycle rules** to automatically transition files to cheaper storage classes (e.g., **Nearline** or **Coldline**) based on their age.





