from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecretkey'

from app.models import Database
db = Database()
db.table()

from app import views
from app.models import Users, Entries