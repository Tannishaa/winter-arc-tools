import time
import os
import logging
import boto3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
WATCH_FOLDER = "my-data"
BUCKET_NAME = "tanisha-winter-arc-v1"
SYNC_INTERVAL = 1  # Seconds
# ---------------------

# Configure logging to look like a real system service
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class S3SyncHandler(FileSystemEventHandler):
    """
    Handles file system events and triggers S3 uploads for modified or created files.
    """
    def __init__(self, bucket, root_folder):
        self.bucket = bucket
        self.root_folder = root_folder
        self.s3_client = boto3.client('s3')

    def on_modified(self, event):
        if not event.is_directory:
            self._upload_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self._upload_file(event.src_path)

    def _upload_file(self, filepath):
        """Helper method to upload a file to S3."""
        # Calculate relative path for S3 key
        relative_path = os.path.relpath(filepath, self.root_folder)
        s3_key = relative_path.replace("\\", "/")

        try:
            logging.info(f"Syncing: {s3_key}")
            self.s3_client.upload_file(filepath, self.bucket, s3_key)
            logging.info(f"Success: {s3_key} uploaded.")
        except Exception as e:
            logging.error(f"Failed to upload {s3_key}: {e}")

def start_watcher(path, bucket):
    """Initializes and starts the directory observer."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created watch directory: {path}")

    event_handler = S3SyncHandler(bucket, path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    logging.info(f"Service active. Watching directory: '{path}'")
    logging.info("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(SYNC_INTERVAL)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Service stopping...")
    
    observer.join()

if __name__ == "__main__":
    start_watcher(WATCH_FOLDER, BUCKET_NAME)