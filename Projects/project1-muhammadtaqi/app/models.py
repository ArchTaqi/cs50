from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)

user = 'books'
password = 'books'
host = 'localhost'
port = 5432
db = 'books' 
url = 'postgresql://{}:{}@{}:{}/{}'
url = url.format(user, password, host, port, db)
app.config['SQLALCHEMY_DATABASE_URI'] = url #'sqlite:////tmp/db_python.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)


########################################################################
class User(db.Model):
    __tablename__ = "tbl_users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
	confirmed_at = db.Column(db.DateTime())
 
    #----------------------------------------------------------------------
    def __init__(self, email, password):
        """"""
        self.email = email
        self.password = password