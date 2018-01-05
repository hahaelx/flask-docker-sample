from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import logging
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DBUSER = 'marco'
DBPASS = 'foobarbaz'
DBHOST = 'database'
DBPORT = '5432'
DBNAME = 'testdb'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'foobarbaz'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
	app.logger.info('Info')
	return 'hello_world:'

@app.route('/test')
def test():
    return 'testqq'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
