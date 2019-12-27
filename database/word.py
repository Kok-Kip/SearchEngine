from database.models import Word
from database import db
from sqlalchemy.sql import exists

def create_word(term):
  word = Word()
  word.term = term

  db.session.add(word)
  db.session.flush()
  word_id = word.id
  db.session.commit()

  return word_id

def getWordByTerm(term):
  word = db.session.query(Word).filter_by(term=term).first()
  return word

def isWordExisted(term):
  word = db.session.query(Word).filter_by(term=term).first()
  if (word == None):
    return False, -1
  return True, word.id