import os
from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    now = datetime.datetime.now().isoformat()
    with open("logs.txt", "a") as f:
        f.write(f"{now} - IP: {ip}, UA: {ua}\n")
    return redirect("https://www.google.com")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # 🟢 THIS IS REQUIRED
    app.run(host='0.0.0.0', port=port)
