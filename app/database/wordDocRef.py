from app.database.models import WordDocRef
from app.database import db


def create_word_doc_ref(word_id, document_id):
    word_doc_ref = WordDocRef()
    word_doc_ref.word_id = word_id
    word_doc_ref.document_id = document_id

    db.session.add(word_doc_ref)
    db.session.commit()


def get_word_doc_ref_by_word_id(word_id):
    word_doc_refs = db.session.query(WordDocRef).filter_by(word_id=word_id).all()
    return word_doc_refs


def update_word_doc_ref(word_id, document_id, frequency):
    word_doc_ref = db.session.query(WordDocRef).filter_by(word_id=word_id, document_id=document_id).first()
    word_doc_ref.frequency = frequency
    db.session.commit()


def is_word_doc_ref_existed(word_id, document_id):
    word_doc_ref = db.session.query(WordDocRef).filter_by(word_id=word_id, document_id=document_id).first()
    if word_doc_ref is None:
        return False, None
    return True, word_doc_ref
