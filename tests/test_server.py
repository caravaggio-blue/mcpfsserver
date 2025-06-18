import pytest
from flask import Flask
from mcpfsserver.server import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_extract_zip(client, mocker):
    # Mock the file system and subprocess
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('os.makedirs')
    mocker.patch('zipfile.ZipFile.extractall')

    response = client.post('/extract_zip', json={
        'zip_path': 'test.zip',
        'extract_to': 'output'
    })
    assert response.status_code == 200
    assert response.json['status'] == 'success'