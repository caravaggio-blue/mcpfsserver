from flask import Flask, request, jsonify
import os
import subprocess

VOLUME_PATH = '/app/data'

def get_full_path(relative_path):
    return os.path.join(VOLUME_PATH, relative_path)

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "MCP File Server is running!"

    @app.route('/read_file', methods=['POST'])
    def read_file():
        data = request.get_json()
        file_path = get_full_path(data.get('path'))

        if not file_path or not os.path.isfile(file_path):
            return jsonify({"error": "Invalid file path"}), 400

        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return jsonify({"content": content}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @app.route('/write_file', methods=['POST'])
    def write_file():
        data = request.get_json()
        file_path = get_full_path(data.get('path'))
        content = data.get('content')

        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return jsonify({"status": "success", "message": f"Content written to {file_path}"}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @app.route('/append_file', methods=['POST'])
    def append_file():
        data = request.get_json()
        file_path = get_full_path(data.get('path'))
        content = data.get('content')

        try:
            with open(file_path, 'a') as file:
                file.write(content)
            return jsonify({"status": "success", "message": f"Content appended to {file_path}"}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
        
    @app.route('/execute_script', methods=['POST'])
    def execute_script():
        data = request.get_json()
        script_content = data.get('script')

        try:
            result = subprocess.run(script_content, shell=True, capture_output=True, text=True)
            return jsonify({
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_status": result.returncode
            }), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
        
    @app.route('/extract_zip', methods=['POST'])
    def extract_zip():
        data = request.get_json()
        zip_path = get_full_path(data.get('zip_path'))
        extract_to = get_full_path(data.get('extract_to'))

        if not zip_path or not os.path.isfile(zip_path):
            return jsonify({"error": "Invalid ZIP file path"}), 400

        # Create the extraction directory if it doesn't exist
        if not os.path.isdir(extract_to):
            os.makedirs(extract_to)

        try:
            import zipfile
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            return jsonify({"status": "success", "message": f"ZIP extracted to {extract_to}"}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
