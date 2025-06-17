from flask import Flask, request, jsonify
import os

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "MCP File Server is running!"

    @app.route('/read_file', methods=['POST'])
    def read_file():
        data = request.get_json()
        file_path = data.get('path')

        if not file_path or not os.path.isfile(file_path):
            return jsonify({"error": "Invalid file path"}), 400

        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return jsonify({"content": content}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
