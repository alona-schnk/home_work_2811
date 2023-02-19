class Person:
    """
    Клас описує людину
    """
    __person = str()
    __firstname = str()
    __lastname = str()
    __age = int()



    @property
    def person(self):
        return self.__person
    
    @property
    def name(self):
        return self.__firstname

    @property
    def last_name(self):
        return self.__lastname

    @property
    def age(self):
        return self.__age


    def __init__(self, person: str, name: str, lastname: str, age: int):
        self.__person = person
        self.__firstname = name
        self.__lastname = lastname
        self.__age = age



class Family(Person):

    __father = dict()
    __mother = dict()
    __children = list()

    def __init__(self):
        self.list_hello = str
        self.__father = Person("Батько", input("Введіть імя батька : "), input("Ведіть його прізвище: "), \
                               input("Скільки йому років: "))
        self.__mother = Person("Мати", input("Введіть імя мами: "), input("Ведіть її прізвище: "), \
                               input("Скільки їй років: "))
        children = input("Чи є в сім'ї діти? y/n: ")
        if children == "y":
            self.__child = Person("Дитина", input("Введіть імя дитини: "), input("Ведіть її прізвище: "), \
                                  input("Скільки їй років: "))



pers = Family()
pers.__init__()



