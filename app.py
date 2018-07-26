from flask import Flask, jsonify, request  
from datetime import datetime


app = Flask(__name__)
date = datetime.now()
now = date.strftime("%d-%m-%Y %H:%M")

Entries = []

@app.route('/')
def index():
	return "Welcome to My-Diary"

@app.route('/api/v1/entries', methods = ['GET'] )
def all_entries():
	return jsonify(Entries)

@app.route('/api/v1/entries/<int:entry_id>', methods = ['GET'] )
def single_entry(entry_id):

	entry = [entry for entry in Entries if entry['entry_id']==entry_id]
	return jsonify({'entry': entry[0]})

@app.route('/api/v1/entries', methods = ['POST'] )
def add_entry():
	new_entry = request.get_json() 
	new_entry['date'] = now
	Entries.append(new_entry)
	id = 1
	for entry in Entries:
		entry['entry_id'] = id
		id += 1
	return jsonify({'entries': Entries})

@app.route('/api/v1/entries/<int:entry_id>', methods = ['Delete'] )
def delete_entry(entry_id):	
	for entry in Entries:
		if entry['entry_id'] == entry_id:
			Entries.remove(entry)	
			return jsonify({'200': 'Entry removed'})	

@app.route('/api/v1/entries/<int:entry_id>', methods = ['PUT'] )
def edit_entry(entry_id):
	new_entry = request.get_json()
	entry = [entry for entry in Entries if entry['entry_id']==entry_id]
	for entry in Entries:
		if entry['entry_id'] == entry_id:
			entry['content'] = new_entry['content']
	return jsonify({'200' : 'Entry updated'})			

if __name__=='__main__':
	app.run(debug=True)	