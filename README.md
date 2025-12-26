# Cloud Vault: Automated Backup Daemon

A Python-based **System Administration Utility** that automates real-time, secure file backups to AWS S3. Engineered to bridge local development environments with enterprise-grade cloud storage, ensuring **Data Integrity** and **Disaster Recovery (DR)** readiness.

## Key Features

* **Real-Time Daemon:** Implements a `watchdog` observer to monitor file system events (Create/Modify) and trigger instant sync, minimizing the Recovery Point Objective (RPO).
* **Disaster Recovery (DR):** Automated `restore.py` CLI to reconstruct the local file system from S3 archives, ensuring business continuity during system failure.
* **Multi-Threaded Performance:** Uses `threading` to handle concurrent file uploads without blocking the main process loop.
* **Security First:** Leverages AWS IAM programmatic access and `.gitignore` policies to ensure zero credential leakage.

##  Tech Stack
* **Core:** Python 3.x, Boto3 (AWS SDK)
* **Automation:** Watchdog (File System Events), Threading
* **Cloud:** AWS S3 (Simple Storage Service), IAM
* **Infrastructure:** Git, AWS CLI

##  Project Structure
```text
.
├── backup.py        # Snapshot Engine: Scans and uploads directory trees
├── restore.py       # DR Tool: Rebuilds local data from Cloud Archive
├── sync.py          # Daemon: Real-time file watcher service (Background Process)
├── requirements.txt # Dependencies (boto3, watchdog)
├── my-data/         # The target directory for backup monitoring
└── .gitignore       # Security rules for credentials
```
## Installation
Clone the repository:

```Bash
git clone https://github.com/Tanisha17016/cloud-vault.git
```
Install Dependencies:

```Bash
pip install -r requirements.txt
```
## How to Run
1. Configure Credentials
Ensure your environment is authenticated with AWS IAM keys:

```Bash

aws configure
```
2. Start the Backup Daemon
To start real-time monitoring of the my-data directory:

```Bash

python sync.py
```
3. Disaster Recovery (Restore)
To download and rebuild lost data from the cloud:

```Bash

python restore.py
```