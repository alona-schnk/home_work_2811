import json
import csv

class Employee:
    firstname = 'Ivasik'
    lastname = 'Telesik'
    age = 13
    email = 'ivasik-telesik1732@izkurnanog.ua'
    skills = ['ходити', 'говорити', 'кодити']
    people_lang = ['Ukrainian', 'English']
    coding_lang = ['Python', 'C++', 'lisp']

    def vuvod(self):
        print(f'{self.firstname}у {self.age} років, і він вміє {self.skills[1]} {self.people_lang[0]}')

    def storinka_facebook(self):
        print(f''
              f'Name: {self.lastname}\n'
              f'Lastname: {self.lastname}\n'
              f'Age: {self.age}\n'
              f'Email: {self.email}\n'
              f'Language: {self.people_lang[0]}\n'
              f'Foreign Language: {self.people_lang[1]}\n'
              f'Programing: {self.coding_lang[0]}'
              f'')

    def file_write(self):
        key = ['name', 'lastname', 'age', 'email', 'people_lang',  'coding_lang']
        value = [self.firstname, self.lastname, self.age, self.email, \
                 self.people_lang, self.coding_lang]
        self.listing = dict(zip(key, value))
        listing = self.listing

        with open('sotrudniki.json', 'w') as file:
            json.dump(listing, file)
        with open('sotrudniki.csv', 'wt') as stat:
            writer = csv.DictWriter(stat, fieldnames=listing, delimiter=';')
            writer.writeheader()
            writer.writerow(listing)




obj = Employee()
obj.vuvod()
obj.storinka_facebook()
obj.file_write()



