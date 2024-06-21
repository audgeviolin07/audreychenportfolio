import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow: Audrey", url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/workexperience')
def workexperience():
    return render_template('workexperience.html')

@app.route('/hobbies')
def hobbies():
    projects = [
        {'name': 'Project 1', 'description': 'Description of project 1.'},
        {'name': 'Project 2', 'description': 'Description of project 2.'},
        {'name': 'Project 3', 'description': 'Description of project 3.'}
    ]
    return render_template('hobbies.html', page_title='My Hobbies', page_description='Here is a list of my hobbies:', page_url='/hobbies', projects=projects)

@app.route('/travelmap')
def travelmap():
    return render_template('travelmap.html')

if __name__ == '__main__':
    app.run(debug=True)
