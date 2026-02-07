import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/test', methods=['GET'])
def test():
    return jsonify(status='success', data='Test endpoint')


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(user_id=user_id, name=f'User {user_id}')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
