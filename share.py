import boto3
from botocore.exceptions import ClientError

# --- CONFIGURATION ---
BUCKET_NAME = "tanisha-winter-arc-v1"
URL_EXPIRATION_SECONDS = 3600  # 1 Hour
# ---------------------

def create_presigned_url(bucket_name, object_name, expiration=URL_EXPIRATION_SECONDS):
    """
    Generate a presigned URL to share an S3 object.

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
        return response
    except ClientError as e:
        print(f"Error generating presigned URL: {e}")
        return None

if __name__ == "__main__":
    print("--- AWS S3 Secure Sharing Utility ---")
    
    file_name = input("Enter the object key (filename) to share: ").strip()

    if not file_name:
        print("Error: Filename cannot be empty.")
        exit()

    print(f"Generating access link for '{file_name}'...")
    
    url = create_presigned_url(BUCKET_NAME, file_name)
    
    if url:
        print("\nSUCCESS. Secure link generated (Valid for 1 hour):")
        print("-" * 80)
        print(url)
        print("-" * 80)
    else:
        print("\nFAILED. Could not generate link.")