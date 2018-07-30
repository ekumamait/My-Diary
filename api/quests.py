from flask import jsonify, request

from api import app

user_details = [
    {"user_id": 1, "user_name": "flintKing", "user_password": "1234"},
    {"user_id": 2, "user_name": "JohnDoe", "user_password": "1234"},
    {"user_id": 3, "user_name": "JaneDoe", "user_password": "1234"}
]


@app.route('/api/v1/users', methods=['GET'])
def return_all_users():
return jsonify({'details': user_details})

@app.route('/api/v1/user/<int:user_id>', methods = ['GET'] )
def single_entry(user_id):

	entry = [entry for entry in Entries if entry['entry_id']==entry_id]
	return jsonify({'entry': entry[0]})