from flask import Flask, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # सबै origin बाट request आउन अनुमति दिन्छ

DATA_FILE = "../data/events.json"

@app.route('/event', methods=['POST'])
def collect_event():
    event = request.json
    print("Received Event:", event)
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'a') as f:
        f.write(json.dumps(event) + "\n")
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(port=5000)
