from flask import Flask, render_template, request,jsonify 
from app.config import AppConfig
import os

app = Flask(__name__,template_folder='../templates',static_folder=os.path.abspath("./statics/"))

app.config.from_object(AppConfig)