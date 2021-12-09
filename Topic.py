import numpy as np
from collections.abc import Sequence
from PageRank import read_graph, PageRank
from corpus import extract_corpus
import json

class TopicRank(PageRank):
    def __init__(
            self,
            graph: dict[str: Sequence[str]],
            meta: dict[str: Sequence[str]],
            topic: str,
            rank: np.ndarray = None,
    ) -> None:
        self.G = graph
        self.M = meta
        self.n = len(G.keys())
        self.R = np.zeros((self.n, self.n))
        self.J = np.zeros(self.n)
        self.rank = rank
        self.topic = topic
    """
    This class inherit from PageRank class and it's used to compute topic
    sensitive pagerank.The main difference is the computation of the 
    jump vector, indeed all the webpages which contains the topic in 
    their metadata will have a probability of 1 over the total amount 
    of webpages containing the topic, 0 elsewhere. At the same time 
    the corpus of the webpage is extracted and the words are added 
    to a term frequency dictionary specific for the topic.
    """
    
    def compute_J(self) -> None:
        tf_dict = {}
        for i, key in enumerate(self.M.keys()):
            for m in self.M[key]:
                words = m.split(',')
                for w in words:
                    if w.lower() == self.topic:
                        self.J[i] = 1
                        with open('simple/'+key, 'r') as f:
                            corpus = extract_corpus(f)
                            for c in corpus:
                                tf_dict[c] = tf_dict.get(c, 0) + 1
        n = len(tf_dict)
        for key in tf_dict.keys():
            tf_dict[key] /= n
        with open(f'{self.topic}_tf_dict.json', 'w') as fp:
            json.dump(tf_dict, fp, ensure_ascii=False)
        self.J = self.J/np.sum(self.J)

    def update_Rank(
            self,
            alpha: int,
            epsilon: int,
    ) -> None:
        self.compute_R()
        self.compute_J()
        err = np.inf
        if self.rank is not None:
            x = self.rank
        else:
            x = np.random.rand(self.n)
            x = x / x.sum()

        while err > epsilon:
            x_new = self.PageRank_iteration(x, alpha)
            err = (abs(x_new - x)).sum()
            print(err)
            x = x_new

        self.rank = np.array([x[0, i] for i in range(x.shape[1])])





if __name__ == '__main__':
    G = read_graph("data/data_filters.json")
    meta = read_graph('data/meta.json')
    topic = ['food']
    Topic_Rank = [TopicRank(G, meta, t) for t in topic]
    for tr in Topic_Rank:
        tr.update_Rank(0.2, 0.001)
        results = dict(zip(G.keys(), tr.rank))
        with open(f'{tr.topic}_rank.json', 'w') as fp:
            json.dump(results, fp, ensure_ascii=False)
