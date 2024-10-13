from google.cloud import storage
from PIL import Image
import io
import os
# Set up Google credentials path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\shvet\OneDrive\Desktop\SBU Fall2024\HHA504_Assignments\module 6\shveta-sharma-hha504-fe3cfe0e6981.json"

# Create a Google Cloud Storage client
client = storage.Client()

# Set the bucket name
bucket_name = 'sharma-ahi-dummy-demo'
bucket = client.bucket(bucket_name)

# Assuming the images are in an 'images' folder
files_upload = []
for root, dirs, files in os.walk("images"):
    for file in files:
        files_upload.append(os.path.join(root, file))

for file in files_upload:
    print(f"Working on {file}")
    with open(file, 'rb') as f:
        file_byte_array = f.read()
    
    file_name = file.split("/")[-1]  # Just keep the file name
    print('New file name:', file_name)

    # Upload the file to Google Cloud Storage
    try:
        blob = bucket.blob(file_name)
        blob.upload_from_string(file_byte_array, content_type='image/png')
        print(f"Image {file_name} uploaded successfully to Google Cloud Storage!")
    except Exception as e:
        print(f"Error: {e}")

# Step 4: Create a fake image using Pillow
image = Image.new('RGB', (100, 100), color = (73, 109, 137))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')

# Step 5: Upload the fake image to Google Cloud Storage
blob = bucket.blob('Viral Pneumonia-1.png')
blob.upload_from_string(image_byte_array.getvalue(), content_type='image/png')

print("Image uploaded successfully to Google Cloud Storage!")