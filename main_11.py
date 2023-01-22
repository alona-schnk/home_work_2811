import re
from collections import Counter

def redactor(text, list):
    '''
    На вход функция получает имя файла и список слов для замены,
    функция ничего не возвращает, но в результате ее работы необходимо создать файл,
    в котором слова из списка заменены шаблоном(звездочками например)
    :param text:
    :param list:
    '''
    for i in list:
        text = re.sub(i, '*' * len(i), text, flags=re.I)
    with open('redactor.txt', 'wt') as red:
        red.write(text)
        print("TASK1 == Ok, REVIEW file redactor.txt")


def calk_kay(file_text):
    '''
    На вход функция получает имя файла, функция возвращает словарь,
    содержащий в качестве ключей слова из текстового файла, а в качестве значений их количество.
    :param file_text:
    '''
    list_res = []
    for i in file_text:
        list_res.append(i.strip("'.,!?()").lower())
    count_file = Counter(list_res)
    print("TASK2 == ", count_file)