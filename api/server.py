from flask import Flask, jsonify, request, make_response
from models import Users

app = Flask(__name__)

# my_user = Users()

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/v2/sign_up', methods = ['POST'])
def sign_up():
    data = request.get_json()
    
    return jsonify({'account created'})

@app.route('/api/v2/auth/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({'msg': 'Missing Json Request'}), 400

    if not request.is_json:
        return jsonify({'msg': 'Missing Json Request'}), 400
    user_name = request.json.get('user_name')
    password = request.json.get('user_password')
    if not user_name:
        return jsonify({'msg': 'input user_name'}), 400

    if not password:
        return jsonify({'msg': 'input user_password'}), 400 

    if user_name != 'test'or password !='test':
        return jsonify({'msg': 'incorrect username or password'})

# @app.route('/api/v1/entries', methods = ['GET'] )
# def all_entries():
# 	return jsonify(Entries)

# @app.route('/api/v1/entries/<int:entry_id>', methods = ['GET'] )
# def single_entry(entry_id):
#     entry = [entry for entry in Entries if entry['entry_id']==entry_id]
#     return jsonify({'entry': entry[0]})

# @app.route('/api/v1/entries', methods = ['POST'] )
# def add_entry():
# 	new_entry = request.get_json() 
# 	new_entry['date'] = now
# 	Entries.append(new_entry)
# 	id = 1
# 	for entry in Entries:
# 		entry['entry_id'] = id
# 		id += 1
#     return jsonify({'entries': Entries})

# @app.route('/api/v1/entries/<int:entry_id>', methods = ['PUT'] )
# def edit_entry(entry_id):
# 	new_entry = request.get_json()
# 	entry = [entry for entry in Entries if entry['entry_id']==entry_id]
# 	for entry in Entries:
# 		if entry['entry_id'] == entry_id:
# 			entry['content'] = new_entry['content']
# 			return jsonify({'200' : 'Entry updated'})
#     return jsonify({'404':'Resource not found'}

if __name__ == '__main__':
    app.run(debug=True)