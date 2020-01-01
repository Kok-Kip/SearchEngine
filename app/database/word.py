from app.database.models import Word
from app.database import db


def create_word(term):
    word = Word()
    word.term = term

    db.session.add(word)
    db.session.flush()
    word_id = word.id
    db.session.commit()

    return word_id


def get_word_by_term(term):
    word = db.session.query(Word).filter_by(term=term).first()
    return word


def is_word_existed(term):
    word = db.session.query(Word).filter_by(term=term).first()
    if word is None:
        return False, -1
    return True, word.id
