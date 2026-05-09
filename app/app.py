from flask import Flask
import os

app = Flask(__name__)

# Hardcoded secret (BAD!)
DATABASE_URL = "postgresql://admin:SuperSecret123@db:5432/mydb"
API_KEY = "sk_live_abc123xyz789"

@app.route('/')
def hello():
    return f"Hello! Running as user: {os.getuid()}"

@app.route('/config')
def config():
    return {
        "database": DATABASE_URL,
        "api_key": API_KEY
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
