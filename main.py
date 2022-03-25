import model, view, control
from flask import Flask
import os
'''
app = Flask(__name__)

id_list = []

os.environ['FLASK_APP'] = 'main.py'
os.environ['FLASK_ENV'] = 'development'
os.environ['APP_URL'] = 'http://localhost:5000'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generate_id")
def generate_id():
    return control.generate_id(id_list)

app.run()'''

control.discord_bot.run([])