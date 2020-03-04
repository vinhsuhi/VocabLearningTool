from flask import Flask, render_template, request,jsonify 
from app.config import AppConfig

app = Flask(__name__,template_folder='../templates',static_folder="../statics/")

app.config.from_object(AppConfig)