from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def send_notification():
    data = request.get_json()
    patient_id = data['patient_id']
    message = data['message']
    
    # Simulate sending a notification (this could be sending an email, SMS, etc.)
    print(f"Notification sent to Patient {patient_id}: {message}")
    return jsonify({'message': 'Notification sent successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5003)
