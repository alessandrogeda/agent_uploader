from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    email = data.get('email')
    file_url = data.get('file_url')

    if not email or not file_url:
        return jsonify({'error': 'Missing email or file_url'}), 400

    # Scarica il file da file_url
    file_response = requests.get(file_url)
    if file_response.status_code != 200:
        return jsonify({'error': 'Unable to download file'}), 400

    files = {
        'upload-field-1_pcfmuf': ('file.pdf', file_response.content, 'application/pdf')
    }

    form_data = {
        'email': email,
        'upload-field-1[]': '22',
        'action': 'pcud_custom_form_submit',
        'pcud_fid': 'ykTN3YDMwETM'  # <-- Assicurati che questo rimanga valido
    }

    target_url = 'https://gaatorg222org.preload.site/wp-admin/admin-ajax.php'

    # POST al form WordPress
    try:
        response = requests.post(target_url, data=form_data, files=files)
        return jsonify({
            'status': 'sent',
            'form_response_code': response.status_code,
            'form_response_text': response.text
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
