from database.models import Document
from database import db


def create_document(link, length):
    document = Document()
    document.link = link
    document.length = length

    db.session.add(document)
    db.session.flush()
    document_id = document.id
    db.session.commit()

    return document_id


def get_document_by_id(document_id):
    document = db.session.query(Document).filter_by(id=document_id).first()
    return document


def get_document_number():
    documents = db.session.query(Document).all()
    return len(documents)
