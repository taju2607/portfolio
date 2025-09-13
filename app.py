from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

# !!! IMPORTANT !!!
# For your security, do not hardcode your credentials here.
# It is highly recommended to use environment variables or a configuration file.
SENDER_EMAIL = "tajuddinpathan2607@gmail.com"
APP_PASSWORD = "ccur epti wfuj svuq"
RECEIVER_EMAIL = "tajuddinpathan0709@gmail.com"

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'Please fill in all fields.'}), 400

    msg = MIMEText(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
    msg['Subject'] = f"New message from {name} via your portfolio"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(SENDER_EMAIL, APP_PASSWORD)
            smtp_server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        return jsonify({'message': 'Message sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
