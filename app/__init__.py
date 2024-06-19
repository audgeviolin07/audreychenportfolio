import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow: Audrey", url=os.getenv("URL"))

@app.route('/education')
def works():
    return render_template('education.html')

@app.route('/workexperience')
def workexperience():
    return render_template('workexperience.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/travelmap')
def travelmap():
    return render_template('travelmap.html')