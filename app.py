from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("Headers:", request.headers)
        print("Raw data:", request.data)
        print("JSON:", request.get_json())

        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON received'}), 400

        email = data.get('email')
        file_url = data.get('file_url')

        if not email or not file_url:
            return jsonify({'error': 'Missing email or file_url'}), 400

        # Download file from file_url
        file_response = requests.get(file_url)
        if file_response.status_code != 200:
            return jsonify({
                'error': 'Unable to download file',
                'status_code': file_response.status_code,
                'headers': dict(file_response.headers),
                'text': file_response.text[:200]  # max 200 char preview
            }), 400

        files = {
            'upload-field-1_pcfmuf': ('file.pdf', file_response.content, 'application/pdf')
        }

        form_data = {
            'email': email,
            'upload-field-1[]': '22',
            'action': 'pcud_custom_form_submit',
            'pcud_fid': 'ykTN3YDMwETM'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://gaatorg222org.preload.site/upload/',
            'Origin': 'https://gaatorg222org.preload.site',
            'Connection': 'keep-alive'
        }

        target_url = 'https://gaatorg222org.preload.site/wp-admin/admin-ajax.php'
        response = requests.post(target_url, data=form_data, files=files, headers=headers)

        return jsonify({
            'status': 'sent',
            'form_response_code': response.status_code,
            'form_response_text': response.text[:500]  # prevent overlogging
        }), 200 if response.status_code == 200 else 502

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return 'Service is up and running!', 200
