# WikiSearch
WikiSearch is a tool that aims to emulate in the most accurate way a search engine.
The user inserts a query through a command-line interface and the most relevant Wikipedia pages 
are retrieved from the [simple Wikipedia dump of April 2007](https://dumps.wikimedia.org/other/static_html_dumps/April_2007/).
The 10 most relevant pages are saved in [`result.html`].

![alt text](https://github.com/ciroantoniomami/WikiSearch/blob/main/img/Wikisearch.png)


The algorithm under the tool is based on the work of Taher H. Haveliwala ["Topic Sensitive PageRank"](http://www-cs-students.stanford.edu/~taherh/papers/topic-sensitive-pagerank.pdf).

## How to run WikiSearch
* run ` python3 wikiSearch.py`.
* insert your query.
* insert ' quit' if you want to shut down the program.

## Structure of the code
* ` dataset.py` retrieves all the .html files and generates ` data.json` where a graph representing the structure of Wikipedia is stored. And ` meta.json` where the keywords for each Wikipedia page is stored.
* ` corpus.py` extracts the corpus of a Wikipedia page and preprocess it.
* ` pageRank.py` computes the famous PageRank algorithm.
* ` topicPageRank.py` computes a topic specific PageRank, for each topic two ` .json` file are created, a ` topic_rank.json` which contains the rank biased on that specific topic, and ` topic_tf_dict.json` which contains a term-frequency dictionary for each topic. The topics used for this tool have been selected from the most common keywords of the data and are:
    * Actor
    * Animal
    * Book
    * Computer
    * Film
    * Food
    * Football
    * Government
    * Mathematics
    * Music
    * Plant
* ` wikiSearch.py` is the interface of the tools, it takes the query as input and, after computing the rank accordingly to the paper cited above, it returns the 10 most relevant pages.
