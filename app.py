from flask import Flask, request, jsonify
from agent_upload import invia_form
import requests
import tempfile
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    email = data.get("email")
    file_url = data.get("file_url")

    if not email or not file_url:
        return jsonify({"error": "email e file_url sono obbligatori"}), 400

    response = requests.get(file_url)
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(response.content)
    tmp.close()

    success, error = invia_form(email, tmp.name)
    os.remove(tmp.name)

    if success:
        return jsonify({"status": "successo"}), 200
    else:
        return jsonify({"error": error}), 500

if __name__ == "__main__":
    app.run(debug=True)
