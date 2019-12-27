from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:******@127.0.0.1:3306/search_engine"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


# DB Entities
class Document(db.Model):
  "class Document"
  __tablename__ = 'document'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  link = db.Column(db.String(128), unique=False)
  length = db.Column(db.Integer, default=0)

class Word(db.Model):
  "class Word"
  __tablename__ = 'word'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  term = db.Column(db.String(32), unique=True)

class WordDocRef(db.Model):
  "class WordDecRef"
  __tablename__ = 'word_doc_ref'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  word_id = db.Column(db.Integer, db.ForeignKey('word.id'))
  document_id = db.Column(db.Integer, db.ForeignKey('document.id'))
  frequency = db.Column(db.Integer, default=1)