import subprocess

import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

@app.route('/jsonip', methods=['GET'])
def ip():
	command = "curl ifconfig.me"

	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	output, error = process.communicate()

	if output:
		return jsonify({'ip': output.decode('utf-8')})

	if error:
		return jsonify({'error': error.decode('utf-8')})
  

@app.route('/ip')
def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text	

if __name__ == '__main__':
    app.run()