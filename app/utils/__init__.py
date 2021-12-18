from .upload import upload_data_with_zip, upload_data_with_streaming, storage

client = storage.Client.from_service_account_json('/secrets/cloudsql/prod.json')
# client = storage.Client.from_service_account_info(info=prod_json)
