# MCP File Server

This project is a local MCP (Model Context Protocol) server that allows an LLM to perform tasks on the local filesystem.

## Building the Docker Image

To build the Docker image, navigate to the `mcpfsserver` directory and run the following command:

```bash
docker build -t mcpfsserver .
```

## Running the Docker Container

To run the Docker container and map port 5000 to your host, use the following command:

```bash
docker run -p 5000:5000 mcpfsserver
```

## Accessing the Application

Once the container is running, you can access the application by navigating to `http://localhost:5000` in your web browser.

```
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


