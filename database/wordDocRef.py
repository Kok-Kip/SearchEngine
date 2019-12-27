from database.models import WordDocRef
from database import db

def create_wordDocRef(word_id, document_id):
  wordDocRef = WordDocRef()
  wordDocRef.word_id = word_id
  wordDocRef.document_id = document_id

  db.session.add(wordDocRef)
  db.session.commit()

def getWordDocRefByWordID(word_id):
  wordDocRefs = db.session.query(WordDocRef).filter_by(word_id=word_id).all()
  return wordDocRefs

def update_wordDocRef(word_id, document_id, frequency):
  wordDocRef = db.session.query(WordDocRef).filter_by(word_id=word_id, document_id=document_id).first()
  wordDocRef.frequency = frequency
  db.session.commit()
  return
  
def isWordDocRefExisted(word_id, document_id):
  wordDocRef = db.session.query(WordDocRef).filter_by(word_id=word_id, document_id=document_id).first()
  if (wordDocRef == None):
    return False, None
  return True, wordDocRef