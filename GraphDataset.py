from __future__ import annotations

import os
from bs4 import BeautifulSoup
import json


def filtering(filename: str, subdir: str) -> bool:
    if filename in ['COPYING.html', 'index.html', 'Wikimedia_Commons_7b57.html']:
        return True
    if subdir in ['images', 'raw', 'upload', 'skins']:
        return True
    if 'User' in filename:
        return True
    if 'Image' in filename:
        return True

    return False


class GraphDataset:

    def __init__(
            self,
            path: str,
    ) -> None:
        self.pages = {}
        self.pages_filtered = {}
        self.meta = {}
        ATTRIBUTES = ['description', 'keywords', 'Description', 'Keywords']
        for subdir, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.html'):
                    if filtering(file, subdir):
                        continue
                    fname = os.path.join(subdir, file)
                    key = fname.replace('simple/', '')
                    self.pages[key] = []
                    self.meta[key] = []
                    with open(fname, 'r') as f:
                        soup = BeautifulSoup(f.read(), 'html.parser')
                        # parse the html as you wish
                        for meta in soup.find_all('meta'):
                            if 'name' in meta.attrs:
                                name = meta.attrs['name']
                                if name in ATTRIBUTES:
                                    self.meta[key].append(meta.attrs['content'])
                        for link in soup.find_all('a'):
                            if link.get('href') is not None:
                                self.pages[key].append(link.get('href').replace("../../../", ""))
        for key in self.pages.keys():
            self.pages_filtered[key] = [item for item in self.pages[key] if item in self.pages.keys()]


if __name__ == '__main__':

    dataset = GraphDataset('simple')
    with open('data.json', 'w') as fp:
        json.dump(dataset.pages, fp, ensure_ascii=False)
    with open('data_filters.json', 'w') as fp:
        json.dump(dataset.pages_filtered, fp, ensure_ascii=False)
    with open('meta.json', 'w') as fp:
        json.dump(dataset.meta, fp, ensure_ascii=False)
    #with open('data.json') as json_file:
    #    data = json.load(json_file)

