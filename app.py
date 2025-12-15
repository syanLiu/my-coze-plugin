from flask import Flask, request, jsonify

app = Flask(__name__)

# 这里放你允许使用的密钥（你可以随时添加新密钥）
VALID_KEYS = {"abc123xyz", "demo789", "premium2025"}

@app.route('/generate-image', methods=['POST'])
def generate_image():
    # 获取用户发送的 JSON 数据
    data = request.get_json()
    
    # 检查有没有传 api_key
    if not data or 'api_key' not in data:
        return jsonify({"error": "Missing api_key"}), 400
    
    api_key = data['api_key']
    
    # 验证密钥是否有效
    if api_key not in VALID_KEYS:
        return jsonify({"error": "Invalid API key"}), 403
    
    # 获取提示词（prompt）
    prompt = data.get("prompt", "a default image")
    
    # 模拟生成图片（实际可调用 AI 模型）
    fake_image_url = f"https://fake-image.com/generated/{prompt.replace(' ', '_')}.jpg"
    
    # 返回成功结果
    return jsonify({
        "success": True,
        "image_url": fake_image_url
    })

if __name__ == '__main__':
    # 让服务能被外部访问（部署时需要）
    app.run(host='0.0.0.0', port=5000, debug=True)