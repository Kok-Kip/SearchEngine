import numpy as np

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