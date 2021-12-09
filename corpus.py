import nltk
import re

from nltk.corpus import stopwords
from bs4 import BeautifulSoup
nltk.download('stopwords')


def extract_corpus(html):

   """The function extract the corpus of the Wikipedia page, then a light preprocessing is applied
   removing punctuation, stopwords and to lowercase"""
    soup = BeautifulSoup(html, 'lxml')

    paras = []
    for paragraph in soup.find_all('p'):
        paras.append(str(paragraph.text))


    text = [val for val in paras]
    text = ' '.join(text)

    text = re.sub(r"\[.*?\]+", '', text)
    text = re.sub(r'[^\w^\s^-]', '', text)
    text = text.lower()
    text = text.split()
    corpus = [word for word in text if word not in stopwords.words()]
    return corpus


if __name__ == '__main__':
    fname = 'simple/f/a/b/Fabio_Cannavaro_6778.html'
    with open(fname, 'r') as f:
        print(extract_corpus(f))
