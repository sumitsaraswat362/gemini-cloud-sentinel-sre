from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "Cloud Sentinel Active",
        "agent": "Gemini-3-Flash-Live",
        "deployment": "Google Cloud Run"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))