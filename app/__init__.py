import os
from peewee import *
from flask import Flask, render_template
from dotenv import load_dotenv
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MY_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow: Audrey Chen", url=os.getenv("URL"))

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

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }



if __name__ == '__main__':
    app.run(debug=True)
