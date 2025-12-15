import subprocess
import sys
from flask import Flask, request, jsonify
import requests

# 强制安装 requests（临时方案）
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

app = Flask(__name__)

@app.route('/get-access-token', methods=['POST'])
def get_access_token():
    try:
        data = request.get_json()
        appid = data.get('appid')
        secret = data.get('secret')

        if not appid or not secret:
            return jsonify({"error": "Missing appid or secret"}), 400

        # 调用微信官方接口
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
        response = requests.get(url)
        result = response.json()

        if 'access_token' in result:
            return jsonify({
                "success": True,
                "access_token": result["access_token"],
                "expires_in": result["expires_in"]
            })
        else:
            return jsonify({
                "success": False,
                "error": result.get("errmsg", "Unknown error")
            }), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)