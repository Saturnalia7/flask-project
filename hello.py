from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
    
@app.route('/css')
def css():
    return url_for('static', filename='style.css')
