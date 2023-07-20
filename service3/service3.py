from flask import Flask, request, jsonify
from logging_module import log_to_elasticsearch
import json

with open('config.json') as f:
    config = json.load(f)

app = Flask(__name__)

@app.route('/method1', methods=['POST'])
def method1():
    data = request.get_json()
    try:
        decision1 = "decision1"
        log_to_elasticsearch("service3", "method1", decision1, data)
        return jsonify({'decision': decision1})
    except Exception as e:
        log_to_elasticsearch("service3", "method1", "error", str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/method2', methods=['POST'])
def method2():
    data = request.get_json()
    try:
        decision2 = "decision2"
        log_to_elasticsearch("service3", "method2", decision2, data)
        return jsonify({'decision': decision2})
    except Exception as e:
        log_to_elasticsearch("service3", "method2", "error", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
