from app.database.word import get_word_by_term
import numpy as np
import jieba
import re

# term = "细胞"
# word = get_word_by_term(term)
# emb = np.frombuffer(word.embedding, dtype=np.float32)
# print(emb.shape)
# print(emb)
filepath = 'data/directory/XIN_CMN_20011221_0027.txt'
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
print(text)