from flask import Flask, request, jsonify

app = Flask(__name__)

# ساختار جدید: دیکشنری اصلی برای ذخیره اطلاعات
messages = {}

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    user = data.get("user")       # مثلاً: "parham"
    content = data.get("api") # مثلاً: "salam"

    if user:
        # اگر این کاربر قبلاً نبود، اضافه کن
        if user not in messages:
            messages[user] = []

        # پیام جدید را به لیست پیام‌های آن کاربر اضافه کن
        messages[user].append(content)

        return jsonify({"status": "received", "user": user})
    else:
        return jsonify({"status": "error", "message": "user not specified"}), 400

@app.route('/rece', methods=['GET'])
def get_messages():
    return jsonify(messages)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)