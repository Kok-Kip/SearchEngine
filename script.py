from app.database.word import get_word_by_term
import numpy as np
import jieba

# term = "细胞"
# word = get_word_by_term(term)
# emb = np.frombuffer(word.embedding, dtype=np.float32)
# print(emb.shape)
# print(emb)

term = "细胞"
seg = jieba.cut_for_search(term)
for s in seg:
    print(s)