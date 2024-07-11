from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://frontend-react-wc.vercel.app"])  # Allow only specific origin

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
