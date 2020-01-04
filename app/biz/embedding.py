from gensim.models import KeyedVectors

path = './data/test.bin'

model = KeyedVectors.load(path)


def get_embedding(term):
    if term in model.vocab:
        return model[term]
    else:
        return None


def embedding2Bytes(embedding):
    if embedding is None:
        return None
    else:
        return embedding.tostring()


def bytes2Embedding(bytes):
    return np.frombuffer(bytes, dtype=np.float32)
