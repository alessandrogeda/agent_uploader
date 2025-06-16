# Agent Uploader Webhook

Riceve webhook (da Zapier o altri) e compila il form su WordPress con email e upload file via Selenium.

## 🔧 Requisiti

- Python 3.9+
- Chrome + ChromeDriver (Render lo supporta)

## 🚀 Deploy su Render

1. Forka o clona il repo su GitHub
2. Vai su [Render](https://render.com)
3. Deploy del repo con:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `gunicorn app:app`

## 🧪 Test webhook

Esempio JSON da inviare via POST:

```json
{
  "email": "utente@example.com",
  "file_url": "https://example.com/file.pdf"
}
