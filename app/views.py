from flask import jsonify, request, make_response
import datetime
from app import app
from app.models import Users, Entries

db = Entries()
bd = Users()
now = datetime.datetime.now()


@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/v2/sign_up', methods = ['POST'])
def sign_up():
	new_user = request.get_json()
	bd.insert_new_user(new_user['user_name'], new_user['user_password'])
	return jsonify({'msg': 'account created'}), 200

@app.route('/api/v2/auth/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({'msg': 'Missing Json Request'}), 400

    user_name = request.json.get('user_name')
    password = request.json.get('user_password')
    if not user_name:
        return jsonify({'msg': 'input user_name'}), 400

    if not password:
        return jsonify({'msg': 'input user_password'}), 400 

    return jsonify({'msg': 'logged in'})

@app.route('/api/v2/entries', methods = ['GET'] )
def all_entries():
    entries = db.get_all_entries() 
    return jsonify({'entries': entries}), 200

@app.route('/api/v2/entries/<int:entry_id>', methods = ['GET'] )
def single_entry(entry_id):
    entry = db.get_entry_by_id(entry_id)
    return jsonify({'entry': entry})

@app.route('/api/v2/entries', methods = ['POST'] )
def add_entry():
	entry = request.get_json()
	entry['date'] = now
	db.insert_new_entry(entry['title'], entry['description'], entry['date'])
	return jsonify({'msg': 'new entry added'}), 200

@app.route('/api/v2/entries/<int:entry_id>', methods = ['PUT'] )
def edit_entry(entry_id):
    new_entry = request.get_json()
    db.edit_entry(entry_id, new_entry['title'], new_entry['description'])
    return jsonify({'msg': 'entry updated'}), 200
   