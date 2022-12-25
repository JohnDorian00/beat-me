import pprint
import time

from gensim.models import KeyedVectors


def create_model():
    model = KeyedVectors.load_word2vec_format("model/model.txt", binary=False)
    model.save("model/model")
    return model


def load_model():
    return KeyedVectors.load("model/model")


def get_words_list(word, size):
    words = load_model().most_similar(positive=[word + "_NOUN"], topn=size)

    for i in range(len(words)):
        words[i] = words[i][0].split("_")[0]

    return words


# For test
if __name__ == "__main__":
    start = time.time()

    list_words = get_words_list("провайдер", 15)

    pprint.pprint(list_words)

    print(len(list_words))
    print(round(time.time() - start, 3))
