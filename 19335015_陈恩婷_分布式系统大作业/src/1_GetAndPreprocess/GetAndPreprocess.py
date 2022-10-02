from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import requests
import pickle


def check_non_ascii(text):
    return any(ord(c) > 127 for c in text)


def check_if_next_page_exist(obj):
    if len(obj.find_all(name='a', attrs={'class': "next_page"})) == 0:
        return False
    else:
        return True


site = "https://github.com/"
repository = "tensorflow/tensorflow/"
label_site = "labels"
issue_site = "issues"
max_page_num = 100
dataset = {}

print("get all labels")
for i in range(1, max_page_num + 1):
    # get webpage
    url = site + repository + label_site + f'?page={i}'
    html = requests.get(url)

    # parse html with BeautifulSoup
    obj = BeautifulSoup(html.text, 'html.parser')

    # get all labels
    label_list = obj.find_all(name='div', attrs={'class': 'js-label-list'})[0]
    for label in label_list.contents:
        if isinstance(label, str):
            continue
        label_name = ''.join(label.span.contents)
        if label_name.find('comp') != -1:
            dataset[label_name] = []

    # check if next page exist
    if not check_if_next_page_exist(obj):
        break

# get all issues
print("get all issues")
for issue_label in dataset:
    print("get issues of " + issue_label)
    for i in range(1, max_page_num + 1):
        if issue_label.find(' ') != -1:
            url = site + repository + issue_site + \
                f'?page={i}&q=label:\"' + \
                issue_label.replace(" ", "%20") + "\"+is:closed"
        else:
            url = site + repository + issue_site + \
                f'?page={i}&q=label:' + issue_label + "+is:closed"
        html = requests.get(url)
        obj = BeautifulSoup(html.text, 'html.parser')
        issue_list = obj.find_all(name='div', attrs={'aria-label': "Issues"})
        if len(issue_list) == 0:
            break
        issue_list = issue_list[0].contents[1]
        for issue in issue_list.contents:
            if isinstance(issue, str):
                continue
            issue_title = ''.join(issue.a.contents)
            if check_non_ascii(issue_title):
                continue
            dataset[issue_label].append(issue_title)

        # check if next page exist
        if not check_if_next_page_exist(obj):
            break

labels = [
    'comp:apis',
    'comp:autograph',
    'comp:cloud',
    'comp:core',
    'comp:signal',
    'comp:tensorboard',
    'comp:tf.function',
    'comp:tfdbg',
    'comp:tpus',
    'comp:xla'
]

with open("issue_titles.txt", "w") as f:
    for i in range(10):
        current = labels[i]
        for x in dataset[current]:
            f.write(x + '\n')
        f.write('\n')
