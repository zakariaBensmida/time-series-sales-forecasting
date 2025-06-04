"""Utilities for AWS S3 upload."""

import boto3
import logging
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
logger = logging.getLogger(__name__)

def upload_to_s3(file_path: Path, bucket: str, key: str) -> bool:
    """Upload file to S3 bucket.

    Args:
        file_path: Local file path
        bucket: S3 bucket name
        key: S3 object key

    Returns:
        True if successful, False otherwise
    """
    try:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION"),
        )
        s3_client.upload_file(str(file_path), bucket, key)
        logger.info(f"Uploaded {file_path} to s3://{bucket}/{key}")
        return True
    except Exception as e:
        logger.error(f"S3 upload failed: {e}")
        return False