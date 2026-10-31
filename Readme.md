# ☁ CloudVault

**A Python-based AWS S3 File Management Application**

CloudVault is a command-line application built using Python and AWS Boto3 SDK to interact with Amazon Simple Storage Service (Amazon S3).

The project demonstrates how to integrate Python applications with AWS cloud storage and perform essential file management operations programmatically.

##  Features

- **List Files:** Retrieve and display objects stored in an S3 bucket.
- **Upload Files:** Upload local files to an S3 bucket.
- **Download Files:** Download objects from S3 to the local system.
- **Delete Files:** Delete objects from an S3 bucket.
- **Interactive CLI:** Perform operations through a simple menu-driven interface.
- **Error Handling:** Handle common AWS and local file-system errors.

##  Tech Stack

- **Language:** Python
- **Cloud Platform:** Amazon Web Services (AWS)
- **Storage:** Amazon S3
- **SDK:** Boto3
- **AWS CLI:** AWS Command Line Interface

##  Project Structure

```text
CloudVault/
│
├── config.py
├── s3_operations.py
├── main.py
├── .gitignore
└── README.md
```

### File Responsibilities

| File | Description |
|---|---|
| `config.py` | Stores AWS region, bucket configuration, and initializes the S3 client. |
| `s3_operations.py` | Contains functions for listing, uploading, downloading, and deleting S3 objects. |
| `main.py` | Provides the interactive command-line menu and application entry point. |
| `.gitignore` | Excludes local environments, generated files, and sensitive configuration files. |

##  Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cloudvault-s3-manager.git
```

### 2. Navigate to the project directory

```bash
cd cloudvault-s3-manager
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install boto3
```

### 5. Configure AWS credentials

Install and configure the AWS CLI:

```bash
aws configure
```

Provide your AWS Access Key ID, Secret Access Key, default region, and output format when prompted.

**Security note:** Never hardcode AWS credentials in your Python files or commit them to GitHub. Use an IAM user or role with only the permissions required for this application.

### 6. Configure the S3 bucket

Update the bucket name and AWS region in `config.py`:

```python
AWS_REGION = "your-aws-region"
BUCKET_NAME = "your-s3-bucket-name"
```

### 7. Run the application

```bash
python main.py
```

##  Application Menu

```text
========== CLOUDVAULT ==========

1. List
2. Upload
3. Download
4. Delete
5. Exit
```

Select an operation from the menu and follow the prompts.

## AWS Permissions

The application requires appropriate S3 permissions for its operations:

- `s3:ListBucket`
- `s3:GetObject`
- `s3:PutObject`
- `s3:DeleteObject`

For production use, permissions should be restricted to the specific S3 bucket and its objects.

## Learning Objectives

This project is part of my hands-on learning journey with Python and AWS. It explores:

- Working with AWS SDKs using Boto3.
- Understanding Amazon S3 buckets and objects.
- Managing cloud storage through Python.
- Using IAM permissions and AWS CLI credentials.
- Structuring Python applications into reusable modules.
- Implementing exception handling and modular programming.

## Future Improvements

- Input validation and improved error handling.
- Logging instead of relying entirely on print statements.
- S3 pagination for handling large numbers of objects.
- Object metadata and file information.
- Unit testing with pytest.
- Improved command-line interface.

## Author

**Nishant Kalane**

[GitHub](https://github.com/nishantkalane) · [LinkedIn](https://www.linkedin.com/in/nishantnk/)

---

*CloudVault is an educational project developed to explore Python programming and AWS cloud storage integration.*