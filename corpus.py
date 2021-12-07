from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re

def extract_corpus(html):
    # Specify url of the web page
    # Make a soup
    soup = BeautifulSoup(html, 'lxml')

    # Extract the plain text content from paragraphs
    paras = []
    for paragraph in soup.find_all('p'):
        paras.append(str(paragraph.text))

    # Extract text from paragraph headers

    # Interleave paragraphs & headers
    text = [val for val in paras]
    text = ' '.join(text)

    # Drop footnote superscripts in brackets
    text = re.sub(r"\[.*?\]+", '', text)
    text = re.sub(r'[^\w^\s^-]', '', text)
    text = text.lower()
    text = text.split()
    tokens_without_sw = [word for word in text if word not in stopwords.words()]
    # Replace '\n' (a new line) with '' and end the string at $1000.
    return tokens_without_sw

if __name__ == '__main__':
    fname = 'simple/f/a/b/Fabio_Cannavaro_6778.html'
    with open(fname, 'r') as f:
        print(extract_corpus(f))
