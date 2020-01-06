from app.database.models import Word, WordDocRef
from app.database import db

from collections import defaultdict
import logging
import time

# 设置 logging 重要性等级
logging.getLogger().setLevel(logging.INFO)


def create_word(term, embedding):
    word = Word()
    word.term = term
    word.embedding = embedding

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


def get_frequent_words(k: int):
    logging.info(f'Starting to get the word refs at {time.asctime(time.localtime(time.time()))}')
    word_refs = db.session.query(WordDocRef).order_by(WordDocRef.frequency.desc()).all()
    logging.info(f'Finish getting the word refs at {time.asctime(time.localtime(time.time()))}')
    words = defaultdict(list)
    for ref in word_refs:
        if len(words[ref.document_id]) != k:
            words[ref.document_id].append(ref.word_id)

    return words


def get_words_embedding_byte(word_ids):
    words = db.session.query(Word).filter(Word.id.in_(word_ids) & Word.embedding.isnot(None)).all()
    res = {w.id: w.embedding for w in words}
    return res
