from app.database.document import get_documents_by_ids, get_document_number
from app.database.word import get_word_by_term, get_frequent_words, get_words_embedding_byte
from app.database.wordDocRef import get_word_doc_ref_by_word_id
from app.biz.embedding import get_embedding
from app.biz.common import *
import math
import jieba
from typing import Dict
import numpy as np

# const parameters for bm25
k1 = 2
b = 0.75
avgdl = 50  # Document Average Length


def get_pertinent_doc_by_key(query):
    seg = jieba.cut_for_search(query)
    score = get_score_of_document(seg)
    doc_ids = get_best_document_by_score(score, 10)
    docs = get_documents_by_ids(doc_ids)
    return docs


def get_best_document_by_score(score, k: int):
    items = score.items()
    reverse_score = [[v[1], v[0]] for v in items]
    reverse_score.sort(reverse=True)
    sorted_score = reverse_score[:k]
    document_ids = [s[1] for s in sorted_score]
    return document_ids


def get_score_of_document(seg) -> Dict[int, float]:
    # score = w1 * tfidf + w2 * bm25 + w3 * word-embedding
    w1 = 0.3
    w2 = 0.3
    w3 = 0.4

    # calculate tiidf
    tfidf = get_score(seg, w1, True)
    # calculate bm25
    bm25 = get_score(seg, w2, False)
    # calculate embedding
    emb = get_score_embedding(seg)

    add_dict(tfidf, bm25)
    add_dict(emb, bm25)
    return bm25


def get_score(seg, weight, score_type=True) -> Dict[int, float]:
    # score_type 为真时用 tfidf 算法, 为假时用 bm25 算法
    score = dict()
    for term in seg:
        score_temp = calculate_score(term, weight, score_type)
        add_dict(score_temp, score)
    return score


def calculate_score(term, weight, score_type=True) -> Dict[int, float]:
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
    score = {}
    all_high_frequency_word_list = get_frequent_words(3)
    # for each document, calculate similarity
    for document_id, word_list in all_high_frequency_word_list.items():
        count = 0
        emb_list = get_words_embedding_byte(word_list)
        document_score = 0
        for s in seg:
            s_emb = get_embedding(s)
            if s_emb is None:
                continue
            for emb in emb_list:
                count += 1
                cos = calculate_cosine_similarity(s_emb, emb)
                document_score += cos
        document_score /= count
        score[document_id] = document_score
    return score


