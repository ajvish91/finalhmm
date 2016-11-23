import sys
import string
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from wordcloud import WordCloud
from collections import defaultdict
import os
import cv2


def get_common_surface_form(original_corpus, stemmer):
    counts = defaultdict(lambda: defaultdict(int))
    surface_forms = {}
    for document in original_corpus:
        for token in document:
            stemmed = stemmer.stem(token)
            counts[stemmed][token] += 1
    for stemmed, originals in counts.items():
        surface_forms[stemmed] = max(originals, key=lambda i: originals[i])
    return surface_forms


category = sys.argv[1]
stemmer = PorterStemmer()
stemmed_corpus = []
original_corpus = []
# print os.getcwd()
# path = "./textForms1/" + (category).lower()
path = "./textForms1/a"
for file in os.listdir(path):
    contents = open(path + "/" + file).read().lower()
    contents = ' '.join([word for word in contents.split()
                         if word not in stopwords.words("english")])
    contents = "".join(l for l in contents if l not in string.punctuation)
    tokens = word_tokenize(contents)
    stemmed = [stemmer.stem(token) for token in tokens]
    stemmed_corpus.append(stemmed)
    original_corpus.append(tokens)
dictionary = Dictionary(stemmed_corpus)
counts = get_common_surface_form(original_corpus, stemmer)
vectors = [dictionary.doc2bow(text) for text in stemmed_corpus]
tfidf = TfidfModel(vectors, normalize=True)
weights = tfidf[vectors[0]]
weights = [(counts[dictionary[pair[0]]], pair[1]) for pair in weights]
print(weights)
wc = WordCloud(
    background_color="white",
    max_words=2000,
    width=1024,
    height=720,
    stopwords=stopwords.words("english")
)
wc.generate_from_frequencies(weights)
wc.to_file("word_cloud.png")
cv2.imshow("word_cloud.png", cv2.imread("word_cloud.png"))
cv2.waitKey(10000)
