from flask import Flask, request, Response, jsonify
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('./config/appconfig.cfg')
CONF = f"postgresql://{app.config['PG_USER']}:{app.config['PG_PASSWORD']}@{app.config['PG_HOST']}:{app.config['PG_PORT']}/{app.config ['PG_DATABASE']}"
app.config['SQLALCHEMY_DATABASE_URI'] = CONF

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #remove?
app.secret_key = 'secret_key'
db = SQLAlchemy(app)

# Models
class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), unique=True, nullable=False)
  content = db.Column(db.String(255), nullable=False)

  def __init__(self, title, content):
    self.title = title
    self.content = content

@app.route('/', methods=['GET'])
def get():
    return ""

#Create the 
@app.route('/create', methods=['POST'])
def itemadd():
    # TODO replace
    query = '''CREATE TABLE if not exists item(id serial PRIMARY KEY, title VARCHAR (200) UNIQUE NOT NULL, content VARCHAR (200) NOT NULL);'''
    db.engine.execute(query)

    request_data = request.get_json()
    title = request_data['title']
    content = request_data['content']

    entry = Item(title, content)
    db.session.add(entry) # insert in the db
    db.session.commit()

    return jsonify("item created")


