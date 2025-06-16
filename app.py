from flask import Flask, request, jsonify
from agent_upload import invia_form
import requests
import tempfile
import os

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Se arriva come lista (array JSON), prendiamo il primo elemento
    if isinstance(data, list):
        data = data[0]

    email = data.get("email")
    file_url = data.get("file_url")

    # ... procedi con Selenium o altro ...
    return jsonify({"status": "ok", "email": email}), 200

