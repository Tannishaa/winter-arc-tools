# AWS Cloud Backup Automation Tool ☁️

A Python-based CLI utility that automates secure file backups to AWS S3. Designed to bridge local development environments with enterprise-grade cloud storage.

## Features
* **Recursive Backup:** Automatically scans directory trees and uploads files while preserving folder structure.
* **Disaster Recovery:** Includes a restoration script (`restore.py`) to download and rebuild local data from the cloud.
* **Security:** Uses AWS IAM programmatic access keys for secure authentication.
* **Efficiency:** Implements `boto3` for direct API interaction, bypassing manual GUI uploads.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Cloud Services:** AWS S3 (Simple Storage Service)
* **SDK:** AWS Boto3
* **Version Control:** Git & GitHub

## 📂 Project Structure
``` text
.
├── backup.py        # Scans local folder and uploads to S3
├── restore.py       # Downloads from S3 to local machine
├── sync.py          # Real-time file watcher service
├── requirements.txt # Project dependencies
├── my-data/         # The directory target for backups
└── .gitignore       # Protects virtual environments and secrets
```

## ⚡ How to Run

### 1. Configure AWS Credentials
Ensure you have the AWS CLI configured with your IAM user keys:
```bash
aws configure
2. Run Backup
To backup the my-data directory:

Bash

python backup.py
3. Run Restore
To recover files from the cloud:

Bash

python restore.py

