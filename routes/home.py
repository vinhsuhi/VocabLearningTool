from flask import jsonify,render_template,json,request
from app import app 
from services import LoadData

@app.route('/')
def goHome():
   fileName = request.args.get('filename')
   vocabulary = LoadData.getData(fileName)
   return render_template('home.html',vocabulary=vocabulary)