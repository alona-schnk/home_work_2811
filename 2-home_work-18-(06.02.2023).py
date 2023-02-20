class Zoo:
    name_vida = str()
    weight = int()
    speed = int()



    def name_zoo(self, name_vida: str):
        self.name_vida = name_vida
        print(f"Ім'я виду тварини {self.name_vida} ")

    def weight_zoo(self, weight: int):
        self.weight = weight
        print(f"Вага тварини {self.weight}")

    def speed_zoo(self, speed: int):
        self.speed = speed
        print(f"Максимальна швидкість тварини {self.speed}")


class Birds(Zoo):

    def __init__(self,  characteristic_features: str):
        self.charac_feature = characteristic_features

    def character(self):
        print(self.charac_feature)

class Orel(Birds, Zoo):

    def __init__(self, kind_orel: str):
        self.kind_orel = kind_orel

    def kind_orel_metod(self):
        print(self.kind_orel)

class Albatross(Birds, Zoo):

    def __init__(self, family: str):
        self.family = family

    def kind_orel_metod(self):
        print(self.family)


class Mammals(Zoo):

    def __init__(self,  sounds: str):
        self.sounds = sounds

    def say(self):
        print(self.sounds)


class Leo(Mammals, Zoo):
    def __init__(self, kind_leo: str):
        self.kind_leo = kind_leo

    def kind_leo_metod(self):
       print(self.kind_leo)

class Wolf(Mammals, Zoo):
    def __init__(self, number: str):
        self.number = number

    def number_metod(self):
        print(self.number)

class Reptiles(Zoo):
    def __init__(self, poison: str):
        self.poison = poison

    def poison_metod(self):
        print(self.poison)

class Serpentes(Reptiles, Zoo):

    def __init__(self, area_life: str):
        self.area_life = area_life

    def area_metod(self):
        print(self.area_life)

class Lizard(Reptiles, Zoo):

    def __init__(self, eat: str):
        self.eat = eat

    def eat_metod(self):
        print(self.eat)


leo = Leo("Хижі")
leo.name_zoo("Ссавці")
leo.kind_leo_metod()
leo.speed_zoo(80)



