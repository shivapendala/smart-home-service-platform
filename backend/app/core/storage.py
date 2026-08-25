import os
import shutil
from abc import ABC, abstractmethod
from typing import BinaryIO
from app.core.config import settings


class StorageProvider(ABC):
    """Abstract Storage Provider interface for file upload/retrieval operations."""

    @abstractmethod
    def save_file(self, file_obj: BinaryIO, filename: str, folder: str = "general") -> str:
        """Save file and return the access URL or relative file path."""
        pass

    @abstractmethod
    def delete_file(self, filepath_or_key: str) -> bool:
        """Delete file from storage backend."""
        pass

    @abstractmethod
    def get_file_url(self, filepath_or_key: str) -> str:
        """Return publicly accessible or relative URL for stored file."""
        pass


class LocalStorageProvider(StorageProvider):
    """Local File System Storage Provider implementation."""

    def __init__(self, base_dir: str = None):
        self.base_dir = base_dir or settings.LOCAL_STORAGE_DIR
        os.makedirs(self.base_dir, exist_ok=True)

    def save_file(self, file_obj: BinaryIO, filename: str, folder: str = "general") -> str:
        target_dir = os.path.join(self.base_dir, folder)
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file_obj, buffer)

        relative_path = os.path.join(folder, filename).replace("\\", "/")
        return relative_path

    def delete_file(self, filepath_or_key: str) -> bool:
        full_path = os.path.join(self.base_dir, filepath_or_key)
        if os.path.exists(full_path):
            os.remove(full_path)
            return True
        return False

    def get_file_url(self, filepath_or_key: str) -> str:
        return f"/static/uploads/{filepath_or_key}"


class S3StorageProvider(StorageProvider):
    """AWS S3 Storage Provider stub ready for S3 configuration."""

    def __init__(self, bucket_name: str = None, region: str = None):
        self.bucket_name = bucket_name or settings.S3_BUCKET_NAME
        self.region = region or settings.AWS_REGION

    def save_file(self, file_obj: BinaryIO, filename: str, folder: str = "general") -> str:
        # S3 boto3 upload logic will be added when S3 credentials are provided
        s3_key = f"{folder}/{filename}"
        raise NotImplementedError("S3 storage integration requires boto3 credentials.")

    def delete_file(self, filepath_or_key: str) -> bool:
        raise NotImplementedError("S3 storage integration requires boto3 credentials.")

    def get_file_url(self, filepath_or_key: str) -> str:
        return f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{filepath_or_key}"


def get_storage_provider() -> StorageProvider:
    """Factory function returning the configured StorageProvider instance."""
    if settings.STORAGE_TYPE.lower() == "s3":
        return S3StorageProvider()
    return LocalStorageProvider()
