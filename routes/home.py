from flask import jsonify,render_template,json,request
from app import app 
from services import LoadData

@app.route('/')
def goHome():
   vocabulary = LoadData.getData('Destination_B2_unit2')
   return render_template('home.html',vocabulary=vocabulary)