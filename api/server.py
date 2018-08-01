from flask import Flask, jsonify, request, make_response
from models import Users
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)


@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/v2/sign_up', methods = ['POST'])
def sign_up():
    return jsonify({'user_name': 'james', 'user_password': 'password'})

@app.route('/api/v2/auth/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({'msg': 'Missing Json Request'}), 400

    user_name = request.json.get('user_name')
    password = request.json.get('password')
    if not user_name:
        return jsonify({'msg': 'input username'}), 400
    if not user_password:
        return jsonify({'msg': 'input password'}), 400  
    if user_name != 'test'or user_password !='test':
        return jsonify({'msg': 'incorrect username or password'})

    access_token = create_access_token(identity=user_name)
    return jsonify(access_token = access_token), 200

@app.route('/api/v2/dashboard', methods = ['GET'])
@jwt_required
def dashboard():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as = current_user), 200

if __name__ == '__main__':
    app.run(debug=True)