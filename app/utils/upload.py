import io
from urllib.parse import quote
from zipfile import ZipFile, ZipInfo

from google.cloud import storage

from app.utils.gcs_stream import GCSObjectStreamUpload


def upload_data_with_streaming(client: storage.Client, bucket_name: str, blob_name: str, data: bytes) -> str:
    with GCSObjectStreamUpload(client=client, bucket_name='udif_data_bkt', blob_name='test-blob.txt') as s:
        s.write(data)
    return f"https://storage.googleapis.com/{bucket_name}/{blob_name}"


def upload_data_with_zip(client: storage.Client, bucket_name: str, blob_name: str, file_name: str, data: str) -> str:
    archive = io.BytesIO()
    with ZipFile(archive, 'w') as zip_archive:
        zip_file = ZipInfo(file_name)
        zip_archive.writestr(zip_file, data)

    archive.seek(0)

    bucket = client.bucket(bucket_name)

    blob = storage.Blob(blob_name, bucket)
    blob.upload_from_file(archive, content_type='application/zip')
    return f"https://storage.googleapis.com/{quote(bucket_name)}/{quote(blob_name)}"
