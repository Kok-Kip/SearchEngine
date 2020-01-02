from app.database.document import get_documents_by_ids, get_document_number
from app.database.word import get_word_by_term
from app.database.wordDocRef import get_word_doc_ref_by_word_id
from collections import defaultdict
import math
import jieba

# const parameters for bm25
k1 = 2
b = 0.75
avgdl = 50  # Document Average Length


def get_pertinent_doc_by_key(query):
    seg = jieba.cut_for_search(query)
    score = get_score_of_document(seg)


def get_score_of_document(seg):
    # score = w1 * tfidf + w2 * bm25 + w3 * word-embedding
    w1 = 0.3
    w2 = 0.3
    w3 = 0.4

    # 计算 tiidf
    tfidf = get_score(seg, w1, True)
    # 计算 bm25
    bm25 = get_score(seg, w2, False)
    emb = get_score_embedding(seg)

    add_dict(tfidf, bm25)
    add_dict(emb, bm25)
    return bm25


def get_score(seg, weight, score_type=True):
    # score_type 为真时用 tfidf 算法, 为假时用 bm25 算法
    score = dict()
    for term in seg:
        score_temp = calculate_score(term, weight, score_type)
        add_dict(score_temp, score)
    return score


def calculate_score(term, weight, score_type=True):
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
            # score_type 为真时用 tfidf 算法
            score[ref.document_id] = weight * (ref.frequency / documents[ref.document_id].length) * idf
        else:
            # score_type 为假时用 em25 算法
            K = k1 * (1 - b + b * documents[ref.document_id].length / avgdl)
            score[ref.document_id] = weight * (ref.frequency * (k1 + 1) / (ref.frequency + K)) * idf
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
