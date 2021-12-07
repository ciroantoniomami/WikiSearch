import json
import numpy as np
import PySimpleGUI as sg

def WikiSearch(term):
    topic = ['arts', 'economics', 'games', 'health', 'news',
             'science', 'society', 'politics', 'food', 'football', 'mathematics', 'basketball']
    Rank_by_topic = {t :{} for t in topic}
    TF_by_topic = {t :{} for t in topic}
    for t in topic:
        with open(f'Rank/{t}_rank.json') as rank:
            Rank_by_topic[t] = json.load(rank)

        with open(f'term-frequency/{t}_tf_dict.json') as tf:
            TF_by_topic[t] = json.load(tf)

    new_rank = dict(zip(Rank_by_topic[topic[0]].keys(), np.zeros(len(Rank_by_topic[topic[0]]))))

    for key in new_rank.keys():
        for t in topic:
            new_rank[key] += (TF_by_topic[t].get(term.lower(), 0)*Rank_by_topic[t].get(key))


    sort_orders = sorted(new_rank.items(), key=lambda x: x[1], reverse=True)
    j = 0
    for i in sort_orders:
        if j == 10:
            break
        j += 1
        print(i[0], i[1])

if __name__ == '__main__':
    # Very basic window.
    # Return values using
    # automatic-numbered keys
    sg.theme('DarkTeal9')
    layout = [
        [sg.Text('', size=(15, 1)), sg.InputText()],
        [sg.Submit()]
    ]

    window = sg.Window('WIKISEARCH', layout)
    event, values = window.read()
    tag = WikiSearch(values[0])
    window.close()
    print = sg.Print
    # The input data looks like a simple list
    # when automatic numbered
    print(tag)