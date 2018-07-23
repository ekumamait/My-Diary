from flask import Flask, jsonify, request  


app = Flask(__name__)

Entries = [
{"entry_id": 1, "date": "01/11/2018", 'title': "first safari",'description': "advkbfsdkjbv"},
{"entry_id": 2, "date": "01/11/2018", 'title': "first safari",'description': "advkbfsdkjbv"},
{"entry_id": 3, "date": "01/11/2018", 'title': "first safari",'description': "advkbfsdkjbv"}]

@app.route('/')
def index():
	return "Hello World"

@app.route('/api/v1/entries', methods = ['GET'] )
def all_entries():
	return jsonify({'entries': Entries})

@app.route('/api/v1/entries/<int:entry_id>', methods = ['GET'] )
def single_entry(entry_id):

	entry = [entry for entry in Entries if entry['entry_id']==entry_id]
	return jsonify({'entry': entry[0]})

@app.route('/api/v1/entries', methods = ['POST'] )
def add_entry():

	new_entry = dict(entry_id = request.json['entry_id'], date=request.json['date'], title=request.json['title'], description=request.json['description']) 
	Entries.append(new_entry)
	return jsonify({'entries': Entries})

@app.route('/api/v1/entries/<int:entry_id>', methods = ['Delete'] )
def delete_entry(entry_id):

	entry = [entry for entry in Entries if entry['entry_id']==entry_id]
	Entries.remove(entry[0])
	return jsonify({'entries': Entries})	

@app.route('/api/v1/entries/<int:entry_id>', methods = ['PUT'] )
def edit_entry(entry_id):

	entry = [entry for entry in Entries if entry['entry_id']==entry_id]
	Entries[0]['entry_id']= request.json['entry_id']
	return jsonify(dict(entry=entry[0]))			

if __name__=='__main__':
	app.run(debug=True)	