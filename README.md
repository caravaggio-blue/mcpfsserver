# MCP File Server

This project is a local MCP (Model Context Protocol) server that allows an LLM to perform tasks on the local filesystem.

## Building the Docker Image

To build the Docker image, navigate to the `mcpfsserver` directory and run the following command:

```bash
docker stop my-mcpfsserver
docker rm my-mcpfsserver

docker rmi mcpfsserver

docker build -t mcpfsserver .
```

## Running the Docker Container

To run the Docker container and map port 5000 to your host, use the following command:

```bash
docker run -v /home/alan/mcp-fs-test-folder:/app/data -p 5000:5000 --name my-mcpfsserver mcpfsserver
```

## Accessing the Application

Once the container is running, you can access the application by navigating to `http://localhost:5000` in your web browser.

```
curl -s  -X POST http://localhost:5000/extract_zip      -H "Content-Type: application/json"      -d '{"zip_path": "alan.zip", "extract_to": "out-folder"}' | jq

curl -s  -X POST http://localhost:5000/read_file      -H "Content-Type: application/json"      -d '{"path": "out-folder/gradle.properties"}' | jq


$ curl -s  -X POST http://localhost:5000/read_file      -H "Content-Type: application/json"      -d '{"path": "requirements.txt"}' | jq

{
  "content": "blinker==1.8.2\nclick==8.1.8\nFlask==3.0.3\nimportlib_metadata==8.5.0\nitsdangerous==2.2.0\nJinja2==3.1.6\nMarkupSafe==2.1.5\nWerkzeug==3.0.6\nzipp==3.20.2\n"
}
$
```

## Project Structure

- `src/mcpfsserver`: Contains the source code for the server.
- `requirements.txt`: Lists the Python dependencies for the project.
- `Dockerfile`: Defines the Docker image configuration.
- `.dockerignore`: Specifies files and directories to exclude from the Docker image.

## Environment Variables

- `FLASK_APP`: Set to `server.py` to specify the entry point for the Flask application.

## Additional Information

For more details on how to use and extend this project, please refer to the source code and comments within the files.

## Current Progress

- Successfully tested the functionality of `server.py` running in Docker.
- Implemented basic file reading functionality via the `/read_file` endpoint.
- Next steps include expanding the server's capabilities to handle additional tasks such as writing to files, appending content, and executing shell scripts.

## MCP Server Development

### Current Functionality
- **Read File**: Reads the contents of a specified file and returns it as JSON.
- **Write File**: Writes content to a specified file, overwriting existing content.
- **Append File**: Appends content to a specified file.
- **Execute Script**: Executes a given script using `subprocess.run` and returns the stdout, stderr, and exit status.

### Next Steps
1. **Extract ZIP File**: Implement a route to extract ZIP files to a specified directory.
2. **List Directory Contents**: Implement a route to list the contents of a directory.
3. **Security Enhancements**: Implement security measures to prevent code injection, path traversal, and other risks.

### Proposed Implementation for ZIP Extraction
```python
@app.route('/extract_zip', methods=['POST'])
def extract_zip():
    data = request.get_json()
    zip_path = data.get('zip_path')
    extract_to = data.get('extract_to')

    if not zip_path or not os.path.isfile(zip_path):
        return jsonify({"error": "Invalid ZIP file path"}), 400

    if not extract_to or not os.path.isdir(extract_to):
        return jsonify({"error": "Invalid extraction directory"}), 400

    try:
        import zipfile
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return jsonify({"status": "success", "message": f"ZIP extracted to {extract_to}"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
```

## Automated Testing

### Setting Up Tests
1. **Install Pytest**: Ensure `pytest` is installed in your environment.
   ```bash
   pip install pytest
   ```

2. **Create Test Files**: Add test cases in the `tests` directory.

3. **Run Tests**: Execute the tests using `pytest`.
   ```bash
   pytest tests/
   ```

### Example Test Case
Here's an example test case for the `/extract_zip` route:

```python
import pytest
from flask import Flask
from src.mcpfsserver.server import create_app

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
```
