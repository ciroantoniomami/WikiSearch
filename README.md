# WikiSearch
WikiSearch is a tool that aims to emulate in the most accurate way a search engine.
The user insert a query through a command-line interface and the most relevants Wikipedia pages 
are retrieved from the [simple Wikipedia dump of April 2007]{https://dumps.wikimedia.org/other/static_html_dumps/April_2007/}.
The 10 most relevant pages are saved in *['result.html'].


The algorithm under the tool is based on the work of Taher H. Haveliwala ["Topic Sensitive PageRank"]{https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.85.9098&rep=rep1&type=pdf}.

## How to run WikiSearch
* run ` python3 wikiSearch.py`.
* insert your query.
* insert ' quit' if you want to shut down the program.
