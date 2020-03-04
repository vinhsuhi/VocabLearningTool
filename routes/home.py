from flask import jsonify,render_template,json,request
from app import app 

@app.route('/')
def goHome():
   return render_template('home.html')