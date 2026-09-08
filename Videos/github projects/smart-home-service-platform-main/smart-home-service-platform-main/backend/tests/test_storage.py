import io
import os
import tempfile
import pytest
from app.core.storage import LocalStorageProvider, get_storage_provider


def test_local_storage_provider():
    with tempfile.TemporaryDirectory() as temp_dir:
        provider = LocalStorageProvider(base_dir=temp_dir)
        
        # Test saving file
        file_content = b"Sample document content for smart home service."
        file_obj = io.BytesIO(file_content)
        
        saved_rel_path = provider.save_file(file_obj, filename="test_doc.txt", folder="docs")
        assert saved_rel_path == "docs/test_doc.txt"
        
        # Verify file exists on disk
        full_path = os.path.join(temp_dir, "docs", "test_doc.txt")
        assert os.path.exists(full_path)
        with open(full_path, "rb") as f:
            assert f.read() == file_content
            
        # Test URL generation
        url = provider.get_file_url(saved_rel_path)
        assert url == "/static/uploads/docs/test_doc.txt"
        
        # Test file deletion
        deleted = provider.delete_file(saved_rel_path)
        assert deleted is True
        assert not os.path.exists(full_path)


def test_storage_provider_factory():
    provider = get_storage_provider()
    assert isinstance(provider, LocalStorageProvider)
