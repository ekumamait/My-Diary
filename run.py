from routes.views import app
from flask import Flask, jsonify, request, make_response
from models.models import Users
import models
from models.models import Database

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
    # Database.create_all()
