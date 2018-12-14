from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask


basedir = os.path.abspath(os.path.dirname(__file__))
# print(os.path.dirname(__file__))
# print(basedir)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)