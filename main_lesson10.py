from typing import List, Any

def fun_list1(list1):
    """
    Функция возвращает новый список в котором содержаться
    элементы из my_list по следующему правилу:
    Если строка стоит на нечетном месте в my_list, то ее заменить на
    перевернутую строку. "qwe" на "ewq".
    Если на четном - оставить без изменения.
    :param list1:
    """
    result_list1 = []
    for i, j in enumerate(list1):
        if i % 2 != 0:
            result_list1.append(j[::-1])
        else:
            result_list1.append(j)
    print("1")
    print(result_list1)


def fun_list2(list2):
    """
    Функция возвращает новый список в котором содержаться
    элементы из my_list у которых первый символ - буква "a".
    :param list2:
    """
    result_list2 = []
    for i in list2:
        if i[0] == 'a' or i[0] == 'A':
            result_list2.append(i)
    print("2")
    print(result_list2)


def fun_list3(list3):
    """
    Функция возвращает новый список в котором содержаться
    элементы из my_list в которых есть символ - буква "a" на любом месте.
    :param list3:
    """
    result_list3 = []
    for i in list3:
        if (i.find('a') or i.find('A')) != -1 or (i[0] == 'a' or i[0] == 'A'):
            result_list3.append(i)
    print("3")
    print(result_list3)


def fun_list4(list4_1):
    """
    Функция возвращает новый список в котором содержаться только строки из my_list.
    """
    result_list4 = []
    for i in list4_1:
        if type(i) == str:
            result_list4.append(i)
    print("4")
    print(result_list4)


def fun_list5(list5):
    """
    Функция возвращает новый список в котором содержаться те символы из my_str,
    которые встречаются в строке только один раз.
    :param list5:
    """
    result_list5 = []
    for stroka in list5:
        for i in stroka:
            if stroka.count(i) == 1:
                result_list5.append(i)
    print("5")
    print(result_list5)


def fun_list6(list6_1, list6_2):
    """
    Функция возвращает список в который поместить те символы,
    которые есть в обеих строках хотя бы раз.
    :param list6_1:
    :param list6_2:
    """

    result_list6 = []
    for i in set(list6_1 + list6_2):
        if i in list6_1 and i in list6_2:
            result_list6.append(i)
    print("6")
    print(result_list6)


def fun_list7(list7_1, list7_2):
    """
   Функция возвращает список в который поместить те символы, которые есть в обеих строках,
    но в каждой только по одному разу.
   :param list7_1:
   :param list7_2:
   """
    rews_1 = [sumvol for sumvol in list7_1 if list7_1.count(sumvol) == 1]
    rews_2 = [sumvol for sumvol in list7_2 if list7_2.count(sumvol) == 1]
    res = list(set(rews_1) & set(rews_2))
    print("7")
    print(res)
