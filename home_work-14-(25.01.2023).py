def dilennya_1():
    '''
    Кожний елемент списка values_to_devide ділиться на кожний елемент списка divide_values
    :return:
    i//j
    '''
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    for i in values_to_devide:
        for j in divide_values:
            try:
                print(i//j)
            except ZeroDivisionError:
                print("На нуль ділити не можна")
            except TypeError:
                print("Не можна комбінувати ці типи даних")



def dilennya_2():
    '''
    Кожний елемент списка values_to_devide ділиться на кожний елемент списка divide_values
    :return:
    i//j
    '''
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    for i in values_to_devide:
        for j in divide_values:
            try:
                print(i // j)
            except Exception:
                print("Щось пішло не так")
            else:
                print("Ділення пройшло успішно")



def index_3():
    '''
    Виводить елемент списка по заданому індексу
    :return:
    list_of_integers[index]
    '''
    list_of_integers = [0, 1, 2, 3, 4, 5]
    try:
        index = int(input("Введіть значення індексу: "))
        print(list_of_integers[index])
    except ValueError:
        print("Потрібно ввести ціле число!")
    except IndexError:
        print("Такого індексу не існує")



def slovnuk():
    '''
    Виводить елемент словника по заданому ключу
    :return:
    person_data[key]
    '''
    person_data = {"name": "Bolt", "age": 23, "gender": "male", "born_date": "06.07.1990"}
    try:
        key =  input("Введіть ключ: ")
        print(person_data[key])
    except KeyError:
        print("Такого ключа не існує")
    finally:
        print("Чекаю наступного ключа!")







dilennya_1()
dilennya_2()
index_3()
slovnuk()
