from app.database.models import Document
from app.database import db
from typing import Dict
from app.biz.common import parseFile


def create_document(link, length):
    document = Document()
    document.link = link
    document.length = length

    db.session.add(document)
    db.session.flush()
    document_id = document.id
    db.session.commit()

    return document_id


def get_documents_by_ids(document_ids) -> Dict[int, Document]:
    documents = db.session.query(Document).filter(Document.id.in_(document_ids)).all()
    return {d.id: d for d in documents}

def get_document_details(document_ids) -> Dict[int, dict]:
    documents = db.session.query(Document).filter(Document.id.in_(document_ids)).all()
    result = dict()
    for d in documents:
        title, date, text = parseFile(d.link)
        detail = {"title": title, "date": date, "text": text}
        result[d.id] = detail

    return result

def get_document_number():
    documents = db.session.query(Document).all()
    return len(documents)
