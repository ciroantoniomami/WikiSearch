import json
import numpy as np
import webbrowser
from pyfiglet import Figlet

def WikiSearch(term):
    """
    The function takes as input a term to be searched and return the top ten pages by
    rank associated with that term. This operation is performed by retrieving all the ranks
    and the term frequency dictionary for all topic, and then the final rank is computed
    according to the paper by Taher H. Haveliwala "Topic Sensitive PageRank"
    """
    topic = ['Mathematics', 'Football (soccer)', 'Film', 'Government', 'Music', 'Book', 'Food', 'Computer',
             'Actor', 'Animal', 'Plant']
    Rank_by_topic = {t :{} for t in topic}
    TF_by_topic = {t :{} for t in topic}
    for t in topic:
        with open(f'data/rank/{t}_rank.json') as rank:
            Rank_by_topic[t] = json.load(rank)

        with open(f'data/term-frequency/{t}_tf_dict.json') as tf:
            TF_by_topic[t] = json.load(tf)

    new_rank = dict(zip(Rank_by_topic[topic[0]].keys(), np.zeros(len(Rank_by_topic[topic[0]]))))

    for key in new_rank.keys():
        for t in topic:
            prob = 1
            for w in term.split():
                prob *= TF_by_topic[t].get(w.lower(), 0)
            new_rank[key] += (prob*Rank_by_topic[t].get(key))

    """
    The pages are ordered by their rank and printed in an html file 
    """
    paths = []
    for p in sorted(new_rank.items(), key=lambda x: x[1], reverse=True):
        paths.append('simple/' + p[0])

    with open('result.html', 'w') as r:
        message = """<html>
        <head>
      </head>
      <body>
         <h1 style="color:green;font-size:40px;">WikiSearch</h1>
      </body>
        </html>"""
        r.write(message)
        for i in range(10):
            path = paths[i]
            name = path[13:]
            name = name.replace('.html', '')
            print(f"\u001b]8;;{path}\u001b\\{name}\u001b]8;;\u001b\\")
            r.write(f'<p><a href={path}>{name}</a></p>')


if __name__ == '__main__':
    f = Figlet(font='slant')
    print(f.renderText('WikiSearch'))
    term = str(input('SEARCH (digit exit to close):'))
    while term != 'exit':
        WikiSearch(term)
        term = str(input('SEARCH (digit exit to close):'))
