# server/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello from Flask backend!'})

if __name__ == '__main__':
    app.run(debug=True)
