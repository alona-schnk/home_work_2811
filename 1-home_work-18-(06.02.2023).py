class Transport:
    """
    Клас описує транспорт
    """
    number = "Номер не задано"
    num_wheels = 4
    engine_power = 90
    max_speed = 200

    def num(self, number):
        self.number = number
        print(f"Державний номер {self.number} ")

    def wheels(self, num_wheels):
        self.num_wheels = num_wheels
        print(f"Авто має {num_wheels} коліс")

    def power(self, engine_power):
        self.engine_power = engine_power
        print(f"Потужність двигуна {engine_power}")

    def speed(self, max_speed):
        self.max_speed = max_speed
        print(f"Максимальна швидкість {max_speed}")

class Velosiped(Transport):
    """
    Клас описує двоколісний транспорт
    """
    kind = "Велосипед"
    brand = "SportLife"
    def __init__(self, kind: str, brand: str):
        self.kind = kind
        self.brand = brand

class Motto(Velosiped, Transport):
    pass


class Avto(Transport):
    """
    Клас описує автомобілі
    """
    kind = "Легкова"
    brand = "BMW"
    body_type = "Седан"

    def __init__(self, kind: str, brand: str, body_type: str):
        self.kind = kind
        self.brand = brand
        self.body_type = body_type

class Gruz(Avto, Transport):

    def __init__(self, kind: str, weight: str, appointment: str):
        self.kind = kind
        self.weight = weight
        self.appointment = appointment

    def kind_gruz(self):
        print(self.kind)
    def appoint(self):
        print(self.appointment)


class Bus(Transport):
    """
    Клас описує автобуси
    """
    def __init__(self, kind: str, brand: str):
        self.kind_bus = kind
        self.brand = brand

    def kind_busik(self):
        print(self.kind_bus)

    def brand_bus(self):
        print(self.brand)



bus = Bus("Бус", "Богдан")
bus.kind_busik()
bus.brand_bus()
print(bus.speed(220))


gruz = Gruz("Грузова", "3t", "Перевезення вантажу")
gruz.kind_gruz()
gruz.appoint()
gruz.num("AG5678")
gruz.wheels(6)




