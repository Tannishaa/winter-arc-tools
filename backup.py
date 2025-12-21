import boto3
import os

#CONFIGURATION 
bucket_name = "tanisha-winter-arc-v1"  
file_to_upload = "journal.txt"
file_name_in_s3 = "day-1-journal.txt"


s3 = boto3.client('s3')

#check if the file exists locally first
if not os.path.exists(file_to_upload):
    print(f"❌ ERROR: I can't find {file_to_upload}. Did you create it?")
else:
    print(f"🚀 Uploading {file_to_upload} to {bucket_name}...")

    try:
        s3.upload_file(file_to_upload, bucket_name, file_name_in_s3)
        print("✅ SUCCESS! File uploaded.")
        print(f"☁️  Saved as: {file_name_in_s3}")
        
    except Exception as e:
        print("❌ ERROR:", e)