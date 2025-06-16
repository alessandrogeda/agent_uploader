from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    print("Payload ricevuto:", data)

    # FIX: Se Zapier invia una lista, usiamo il primo elemento
    if isinstance(data, list):
        data = data[0]

    email = data.get("email")
    file_url = data.get("file_url")

    print(f"Email: {email}, File URL: {file_url}")

    # Qui puoi lanciare il codice selenium / scraping ecc...
    return jsonify({"status": "ok", "email": email, "file_url": file_url}), 200
