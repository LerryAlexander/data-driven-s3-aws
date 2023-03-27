import pytest
import requests
import time
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from utils import upload_file, delete_file

CATALOG_ENDPOINT = 'https://63e18a5565b57fe6065a0fe6.mockapi.io/input'
PRODUCT_ENDPOINT = 'https://63e18a5565b57fe6065a0fe6.mockapi.io/product'

bucket_name = 'lerrysawsbucket'
data_folder = 'data'
file_list = os.listdir(data_folder) # Get a list of all files in the "data" folder

catalogs = []
products = []

remaining_tries = 15 # each attempt last 10 seconds
input_id = None

def test_upload_files():
    # Loop through each file and upload it to S3
    for file_name in file_list:
        if file_name.endswith('.csv'):
            file_path = os.path.join(data_folder, file_name)
            result = upload_file(file_path, bucket_name)
            # assertions to verify the result
            assert result is True, f"Failed to upload file {file_name}"

def test_catalog_output():
    # simulate processing time (30s)
    print("waiting ~30s for process to complete...")
    time.sleep(30)
    response = requests.get(CATALOG_ENDPOINT)
    assert response.status_code == 200
    if len(response.json()) > 0:
        record = response.json()[0]
        if record['status'] != 'failed':
            global remaining_tries
            global input_id
            while remaining_tries > 0:
                if record['status'] == 'complete':
                    break
                else:
                    remaining_tries -= 1
                    time.sleep(10)
                    print("remaining time... " + str(remaining_tries*10)+' seconds')
            else:
                assert False, 'Catalog output not completed within 3 minutes'
            input_id = record['id']
            assert len(record['assets']) > 0
            for asset in record['assets'] :
                catalogs.append(asset)
        else:
            assert False, 'Catalog output failed to complete'

def test_download_catalog():
    if len(catalogs) > 0:
        for catalog in catalogs:
            response = requests.get(catalog)
            assert response.status_code == 200
            assert 'Content-Type' in response.headers
            assert 'application/json' in response.headers['Content-Type'] or 'image/png' in response.headers['Content-Type']
            assert 'Content-Length' in response.headers
            assert int(response.headers['Content-Length']) > 0
            assert len(response.content) > 0
    else:
        pytest.skip("Test condition is not met")

def test_product_output():
    # wait for catalog output to complete
    global remaining_tries
    global input_id
    remaining_time = remaining_tries*10
    if len(catalogs) > 0:
        if remaining_tries > 0:
            while remaining_tries > 0:
                response = requests.get(PRODUCT_ENDPOINT)
                record = response.json()[0]
                if record['status'] != 'failed':
                    if record['status'] == 'complete':
                        break
                    remaining_tries -= 1
                    time.sleep(10)
                    print("remaining time... " + str(remaining_tries*10)+' seconds')
                else:
                    assert False, 'Product output failed to complete'
            else:
                assert False, 'Product output not completed within the remaining time of '+str(remaining_time)+' seconds'
        else:
            assert False, 'No remaining time left to complete the product'
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert record['input_id'] == input_id
        assert len(record['assets']) > 0
        for asset in record['assets'] :
            products.append(asset)
    else:
        pytest.skip("Test condition is not met")

def test_download_product():
    if len(products) > 0:
        for product in products:
            response = requests.get(product)
            assert response.status_code == 200
            assert 'Content-Type' in response.headers
            assert 'application/json' in response.headers['Content-Type'] or 'image/png' in response.headers['Content-Type']
            assert 'Content-Length' in response.headers
            assert int(response.headers['Content-Length']) > 0
            assert len(response.content) > 0
    else:
        pytest.skip("Test condition is not met")

def test_delete_files():
    # clean up
    for file_name in file_list:
        if file_name.endswith('.csv'):
            result = delete_file(bucket_name, file_name)
            # assertions to verify the result
            assert result is True