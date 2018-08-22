from flask import jsonify, request, make_response
import jwt
import datetime
from functools import wraps
from app import app
from app.models import Users, Entries

db = Entries()
bd = Users()
now = datetime.datetime.now()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        """ method to generate tokens for registered users to access secured end points """

        token = request.args.get('token')

        if not token:
            return jsonify({'msg': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
             return jsonify({'msg' : 'Token is invalid'}), 403   

        return f(*args, **kwargs)    

    return decorated

@app.route('/')
def index():
    """ this is the index end point """
    return jsonify({'message': 'This is the index'})

@app.route('/api/v2/sign_up', methods = ['POST'])
def sign_up():
    """ end point for signing up a user """

    new_user = request.get_json()
    bd.insert_new_user(new_user['user_name'], new_user['user_password'])
    return jsonify({'msg': 'account created'}), 200

@app.route('/api/v2/login')
def login():
    """ end point for logging in a signed up user """
    auth = request.authorization

    if auth and auth.password == 'password':
        token =  jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')}), 200

    return make_response('could not verify!', {'WWW-Authenticate': 'Basic realm="Login Required"'}), 401 

@app.route('/api/v2/entries', methods = ['GET'] )
@token_required
def all_entries():
    """  end point for displaying all the entries """

    entries = db.get_all_entries() 
    return jsonify({'entries': entries}), 200

@app.route('/api/v2/entries/<int:entry_id>', methods = ['GET'] )
@token_required
def single_entry(entry_id):
    """ end point for displaying a single entry """

    entry = db.get_entry_by_id(entry_id)
    return jsonify({'entry': entry})

@app.route('/api/v2/entries', methods = ['POST'] )
@token_required
def add_entry():
    """  end point to add an entry """
    entry = request.get_json()
    entry['date'] = now
    db.insert_new_entry(entry['title'], entry['description'], entry['date'])
    return jsonify({'msg': 'new entry added'}), 200

@app.route('/api/v2/entries/<int:entry_id>', methods = ['PUT'] )
@token_required
def edit_entry(entry_id):
    """  end point for modifying the entries """

    new_entry = request.get_json()
    db.edit_entry(entry_id, new_entry['title'], new_entry['description'])
    return jsonify({'msg': 'entry updated'}), 200

@app.route('/api/v2/entries/<int:entry_id>', methods=['Delete'])
@token_required
def delete_one(entry_id):
    """ end point for deleting an entry """

    entry = request.get_json()
    db.delete_entry(entry)
    return jsonify({'message': "entry deleted"}), 200
