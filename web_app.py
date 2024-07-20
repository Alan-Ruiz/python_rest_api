from flask import Flask, render_template_string
import db_connector as db

app = Flask(__name__)

@app.route('/users/get_user_data/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    result = db.get_user(user_id)
    if result['status'] == 'ok':
        return render_template_string("<p id='user_name'>{{ user_name }}</p>", user_name=result['user_name']), 200
    else:
        return render_template_string("<p id='error'>{{ error }}</p>", error=result['reason']), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)