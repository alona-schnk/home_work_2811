class Family:
     persona = str()
     name = str()
     age = int()

     def __init__(self, persona: str, name: str, age: int):
         self.persona = persona
         self.name = name
         self.set_age(age)

     def __str__(self):
         return f'Persona: {self.persona}, Name: {self.name}, Age: {self.age}'

     def set_age(self, age: int):
         if age >= 0:
             self.age = age
         else:
             self.age = 0

obj = Family('Mother', 'Alla', 34)
obj.set_age(-23)
print(obj)


