import pprint
import time
import os

from gensim.models import KeyedVectors

dir_path = os.path.dirname(os.path.realpath(__file__))

def create_model():
    model = KeyedVectors.load_word2vec_format(dir_path + "\model\model.txt", binary=False)
    model.save(dir_path + "\model\model")
    return model


def load_model():

    return KeyedVectors.load(dir_path + "\model\model")


def get_words_list(word, size):
    words = load_model().most_similar(positive=[word + "_NOUN"], topn=size)

    for i in range(len(words)):
        words[i] = words[i][0].split("_")[0]

    return words


# For test
if __name__ == "__main__":
    start = time.time()

    # create_model()
    list_words = get_words_list("зима", 15)

    pprint.pprint(list_words)

    print(len(list_words))
    print(round(time.time() - start, 3))
