from flask import Flask, jsonify, request
from password import validate_password, generate_password


app = Flask(__name__)


@app.route('/generate', methods=['Post'])
def generate():
    length = request.json['length']

    return jsonify({'password': generate_password(length)})


@app.route('/validate', methods=['Post'])
def validate():
    password = request.json['password']

    return jsonify(validate_password(password))


@app.route('/', methods=['GET'])
def index():
    return jsonify('welcome to password service the available routes are /generate and /validate')


if __name__ == '__main__':
    app.run(debug=False)
