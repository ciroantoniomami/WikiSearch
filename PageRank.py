from __future__ import annotations

import json
import numpy as np
from collections.abc import Sequence

def read_graph(filename):
    with open(filename, 'r') as f:
        # We have the graph encoded as an adjacency list in a JSON file
        g = json.load(f)
        # The data structure read from JSON is already "good enough" for us
        return g

class PageRank():
    def __init__(
            self,
            graph: dict[str: Sequence[str]],
    ) -> None:
        self.G = graph
        self.n = len(G.keys())
        self.R = np.zeros((self.n, self.n))
        self.J = np.ones(self.n)/self.n
        self.rank = np.zeros(self.n)

    def compute_R(self,
    ) -> None:
        key_to_pos = dict(zip(self.G.keys(), range(0, self.n)))
        for i, source in enumerate(self.G.keys()):
            # The out degree of a node is simply the length of its adjacency list
            out_deg = len(self.G[source])
            for dest in self.G[source]:
                j = key_to_pos[dest]
                self.R[i][j] = 1 / out_deg

    def PageRank_iteration(
            self,
            x: np.ndarray,
            alpha: int,
    ) -> np.ndarray:
        one = np.mat(np.ones(self.n)).T
        P = (alpha * one * self.J + (1 - alpha) * self.R)
        x_prime = x * P
        return x_prime

    def compute_PageRank(
            self,
            alpha: int,
            epsilon: int,
    ) -> None:
        self.compute_R()
        x = np.random.rand(self.n)
        x = x / x.sum()
        err = np.inf
        while (err > epsilon):
            x_new = self.PageRank_iteration(x, alpha, self.J)
            err = (abs(x_new - x)).sum()
            print(err)
            x = x_new
        self.rank = np.array([x[0, i] for i in range(x.shape[1])])

    def print_rank(self):
        print("PageRank scores:")
        for i, k in enumerate(self.G.keys()):
            print(f"{k}: {self.rank[i]}")







if __name__ == '__main__':
    G = read_graph("data_filters.json")
    Page_Rank = PageRank(G)
    Page_Rank.compute_PageRank(0.1, 0.01)
    Page_Rank.print_rank()
    np.savetxt('Rank.csv', Page_Rank.rank, delimiter=',')
    results = dict(zip(Page_Rank.G.keys(), Page_Rank.rank))
    sort_orders = sorted(results.items(), key=lambda x: x[1], reverse=True)
    j = 0
    for i in sort_orders:
        if j == 10:
            break
        j += 1
        print(i[0], i[1])