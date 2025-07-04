
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Angel One Auth Server is Running!"

@app.route('/callback')
def callback():
    auth_code = request.args.get("auth_code")
    if auth_code:
        print("✅ AUTH CODE RECEIVED:", auth_code)
        return f"Auth Code received: {auth_code}<br><br>Copy it and paste into your trading script."
    return "❌ No auth_code found."
