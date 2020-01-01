from app import app
from database.document import get_documents_by_ids, get_document_number
from database.word import get_word_by_term
from database.wordDocRef import get_word_doc_ref_by_word_id
from flask import jsonify, request
import math
import jieba


k1 = 2
b = 0.75
avgdl = 50  # Document Average Length





def get_pertinent_doc_by_key(query):
    seg = jieba.cut_for_search(query)
    score = get_score_of_document(seg)


def get_score_of_document(seg):
    # score = tfidf + bm25 + word-embedding
    # 计算 tiidf
    tfidf = get_score(seg, True)
    # 计算 bm25
    bm25 = get_score(seg, False)
    emb = get_score_embedding(seg)

    w1 = 0.3
    w2 = 0.3
    w3 = 0.4
    score = w1 * tfidf + w2 * bm25 + w3 * emb
    return score


def get_score(seg, score_type=True):
    # score_type 为真时用 dfidf 算法, 为假时用 bm25 算法
    score = dict()
    for term in seg:
        score_temp = calculate_score(term, score_type)
        add_dict(score_temp, score)
    return score


def calculate_score(term, score_type=True):
    score = dict()
    N = get_document_number()

    # 1. find all relevant documents
    word = get_word_by_term(term)
    word_id = word.id

    word_doc_refs = get_word_doc_ref_by_word_id(word_id)
    n = len(word_doc_refs)
    idf = math.log(N / n)

    document_ids = [r.document_id for r in word_doc_refs]
    documents = get_documents_by_ids(document_ids)

    for ref in word_doc_refs:
        if score_type:
            # score_type 为真时用 dfidf 算法
            score[ref.document_id] = (ref.frequency / documents[ref.document_id].length) * idf
        else:
            # score_type 为假时用 em25 算法
            K = k1 * (1 - b + b * documents[ref.document_id].length / avgdl)
            score[ref.document_id] = (ref.frequency * (k1 + 1) / (ref.frequency + K)) * idf
    return score


def get_score_embedding(seg):
    # TODO
    return 0


def add_dict(x, y):
    for k, v in x.items():
        if k in y.keys():
            y[k] += v
        else:
            y[k] = v


if __name__ == '__main__':
    app.run(debug=True)
