import subprocess
import sys

# 强制安装 requests
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return {"status": "success", "message": "Hello from Coze Plugin!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)