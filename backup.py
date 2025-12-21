import boto3
import os

# --- CONFIGURATION ---
SOURCE_FOLDER = "my-data"
BUCKET_NAME = "tanisha-winter-arc-v1"
# ---------------------

def upload_files(source, bucket):
    """
    Scans a local directory and uploads all files to S3, 
    preserving the folder structure.
    """
    s3 = boto3.client('s3')

    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' not found.")
        return

    print(f"Starting backup from '{source}' to bucket '{bucket}'...")

    for root, dirs, files in os.walk(source):
        for filename in files:
            local_path = os.path.join(root, filename)
            
            # Create S3 key (path) ensuring standard forward slashes
            s3_key = os.path.relpath(local_path, source).replace("\\", "/")

            try:
                print(f"Uploading: {s3_key}")
                s3.upload_file(local_path, bucket, s3_key)
            except Exception as e:
                print(f"Failed to upload {filename}: {e}")

    print("Backup operation completed.")

if __name__ == "__main__":
    upload_files(SOURCE_FOLDER, BUCKET_NAME)