from flask_cors import CORS, cross_origin
from flask import jsonify,json
from app import app

from routes import *

if __name__ == "__main__":
    CORS(app)
    app.run(debug=True, host="localhost", threaded=True, port=5050)