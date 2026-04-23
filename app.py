from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Healthcare Patient Dashboard v1.0</h1><p>Status: All Systems Secure.</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
