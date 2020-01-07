import numpy as np
import re


def parseFile(filepath):
    print(filepath)
    title = ''
    date = ''
    text = ''
    with open(filepath, encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            if line == '\n':
                continue
            head = re.search(r'^<(.*)>(.+)(</.*>)?', line, re.M | re.I)
            if head is not None and head.group(1) == 'HEADLINE':
                title = head.group(2)
            if head is not None and head.group(1) == 'DATELINE':
                date = head.group(2)
            if line[0] != '<':
                h = re.search(r'^(.+)</(.*)>', line, re.M | re.I)
                if h:
                    if h.group(2) == 'HEADLINE':
                        title = h.group(1)
                    elif h.group(2) == 'DATELINE':
                        date = h.group(1)
                else:
                    text = text + line

    print(f'Title: {title}')
    print(f'Date: {date}')
    print(f'Text: {text}')
    return title, date, text


def add_dict(x, y):
    for k, v in x.items():
        if k in y.keys():
            y[k] += v
        else:
            y[k] = v


def calculate_cosine_similarity(a, b):
    if a is None:
        print('a is None')
        return
    if b is None:
        print('b is None')
        return
    if a.shape != b.shape:
        print('shape not equal!')
        return
    vector_a = np.mat(a)
    vector_b = np.mat(b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim
