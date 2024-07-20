from flask import Flask, request, jsonify
import db_connector as db

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['POST'])
def create_user(user_id):
    data = request.json
    user_name = data.get('user_name')
    if not user_name:
        return jsonify({"status": "error", "reason": "user_name is required"}), 400
    result = db.add_user(user_id, user_name)
    if result['status'] == 'ok':
        return jsonify(result), 200
    else:
        return jsonify(result), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    result = db.get_user(user_id)
    if result['status'] == 'ok':
        return jsonify(result), 200
    else:
        return jsonify(result), 500

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user_name = data.get('user_name')
    if not user_name:
        return jsonify({"status": "error", "reason": "user_name is required"}), 400
    result = db.update_user(user_id, user_name)
    if result['status'] == 'ok':
        return jsonify(result), 200
    else:
        return jsonify(result), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = db.delete_user(user_id)
    if result['status'] == 'ok':
        return jsonify(result), 200
    else:
        return jsonify(result), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)