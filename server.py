from app import app
from flask import jsonify, request
import math
import jieba


@app.route('/search', methods=['POST'])
def search():
    req = request.get_json()

    # get_pertinent_doc_by_key(req['key'])

    return jsonify(message='ok')


def get_pertinent_doc_by_key(query):
    seg = jieba.cut_for_search(query)
    score = get_score_of_document(seg)


def get_score_of_document(seg):
    # score = tfidf + bm25 + word-embedding
    # tfidf = get_score_tfidf(seg)
    bm25 = get_score_bm25(seg)
    emb = get_score_embedding(seg)

    w1 = 0.3
    w2 = 0.3
    w3 = 0.4
    score = w1 * tfidf + w2 * bm25 + w3 * emb
    return score


def get_score_tfidf(seg):
    score_tfidf = {}
    for term in seg:
        score_temp = calculate_tfidf(term)
        # TODO
        # merge_dict(score_temp, score_tfidf)
    return score_tfidf


def get_score_bm25(seg):
    score_bm25 = {}
    for term in seg:
        score_temp = calculate_bm25(term)
        add_dict(score_temp, score_bm25)
    return score_bm25


def get_score_embedding(seg):
    pass


def calculate_tfidf(term):
    score = {}
    N = getDocumentNumber()

    # 1. find all relevant documents
    word = getWordByTerm(term)
    word_id = word.id

    wordDocRefs = getWordDocRefByWordID(word_id)
    n = len(wordDocRefs)
    idf = math.log(N / n)

    for ref in wordDocRefs:
        document = getDocumentByID(ref.document_id)
        score[ref.document_id] = (ref.frequency / document.length) * idf
    return score


def calculate_bm25(term):
    tfidf = calculate_tfidf(term)
    relativeness = calculate_R(term)
    score = mul_dict(tfidf, relativeness)
    return score


k1 = 2
b = 0.75
avgdl = 50 # Document Avarage Length


def calculate_R(term):
    score = {}
    # 1. find all relevant documents
    word = getWordByTerm(term)
    word_id = word.id

    wordDocRefs = getWordDocRefByWordID(word_id)
    n = len(wordDocRefs)

    for ref in wordDocRefs:
        score[ref.document_id] = ref.frequency * (k1 + 1) / (ref.frequency + k1 * (1 - b + b * avgdl))
    return score


def add_dict(x, y):
    for k, v in x.items():
        if k in y.keys():
            y[k] += v
        else:
            y[k] = v


def mul_dict(x, y):
    score = {}
    for k, v in x.items():
        if k in y.keys():
            score[k] = v * y[k]
        else:
            print('mul_dict err')
    return score


if __name__ == '__main__':
    app.run(debug=True)
