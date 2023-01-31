import csv
import json
import re
from collections import Counter

def censor1(text, list):
    for i in list:
        text = re.sub(i, '*' * len(i), text, flags=re.I)
    with open('redactor.txt', 'wt') as red:
        red.write(text)
        print("REVIEW file redactor_file.txt")

def censor2(file_text):
    list_res = []
    for i in file_text:
        list_res.append(i.strip("'.,!?()").lower())
    count_file = Counter(list_res)
    with open('stat.json', 'w') as stat:
        json.dump(count_file, stat)
    print("REVIEW file stat.json")

def censor3(file_text):
    list_res = []
    for i in file_text:
        list_res.append(i.strip("'.,!?()").lower())
    count_file = Counter(list_res)
    with open('stat.csv', 'wt') as stat:
        writer = csv.DictWriter(stat, fieldnames=count_file.keys(), delimiter=';')
        writer.writeheader()
        writer.writerow(count_file)
        print("REVIEW file stat.csv")