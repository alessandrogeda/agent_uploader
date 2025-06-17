from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)

        # Gestione caso anomalo: payload è una stringa JSON dentro una chiave vuota
        if isinstance(data, dict) and "" in data:
            data = json.loads(data[""])

        email = data.get("email")
        file_url = data.get("file_url")

        print(f"Payload ricevuto: {data}")
        print(f"Email: {email}, File URL: {file_url}")

        # Qui puoi fare quello che ti serve con email e file_url
        return jsonify({"status": "success", "email": email, "file_url": file_url}), 200

    except Exception as e:
        print(f"Errore nel webhook: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400
