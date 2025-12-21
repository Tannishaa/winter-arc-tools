import boto3
import os

# --- CONFIGURATION ---
BUCKET_NAME = "tanisha-winter-arc-v1"
RESTORE_DIR = "restored_files"
# ---------------------

def download_files(bucket, destination):
    """
    Downloads all objects from the specified S3 bucket to a local directory,
    recreating the folder structure found in the cloud.
    """
    s3 = boto3.client('s3')

    # Ensure the destination directory exists
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"Created restore directory: '{destination}'")

    print(f"Starting restoration from bucket '{bucket}'...")

    try:
        # List all objects within the bucket
        response = s3.list_objects_v2(Bucket=bucket)

        if 'Contents' not in response:
            print("Bucket is empty. Nothing to restore.")
            return

        for obj in response['Contents']:
            file_key = obj['Key']
            
            # Construct local path
            local_path = os.path.join(destination, file_key)
            
            # Ensure local subdirectories exist
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            try:
                print(f"Downloading: {file_key}")
                s3.download_file(bucket, file_key, local_path)
            except Exception as e:
                print(f"Failed to download {file_key}: {e}")

        print("Restore operation completed successfully.")

    except Exception as e:
        print(f"Critical error accessing bucket: {e}")

if __name__ == "__main__":
    download_files(BUCKET_NAME, RESTORE_DIR)