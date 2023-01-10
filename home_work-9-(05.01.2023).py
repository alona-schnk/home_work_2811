print("Завдання №1")
persons = [
    {'name':'Dan', 'age':16},
    {'name':'Jon', 'age':22},
    {'name':'Filip', 'age':18},
    {'name':'Milan', 'age':17},
    {'name':'Gary', 'age':16}
]
print("A")
list_age = []
list_name = []
for i in persons:
    list_age.append(i['age'])
for i in persons:
    if i['age'] == min(list_age):
        list_name.append(i['name'])
print(list_name)
print("\n")

print("Б")
list_name_len = []
list_name_long = []
for i in persons:
    list_name_len.append(len(i['name']))
for i in persons:
    if len(i['name']) == max(list_name_len):
        list_name_long.append(i['name'])
print(list_name_long)
print("\n")

print("В")
new_age_list = []
for i in persons:
    new_age_list.append(i['age'])
average_age = sum(new_age_list) / len(new_age_list)
print("Середній вік:", average_age)
print("\n")

print("Завдання №2")

my_dict1 = {'name':'Nina', 'age':23, 'job':'seller', 'profession':'jurist', 'live':'Lviv'}
my_dict2 = {'surname':'Olecsina', 'name':'Olha', 'profession':'designer', 'live':'Malta'}
print("A")
my_dict_kay1 = []
for i in (my_dict1 | my_dict2):
    if i in my_dict1 and i in my_dict2:
        my_dict_kay1.append(i)
print(my_dict_kay1)
print("\n")

print("Б")
my_dict_kay2 = []
for i in my_dict1:
    if i not in my_dict2:
        my_dict_kay2.append(i)
print(my_dict_kay2)
print("\n")

print("B")
my_dict_kay3 = dict()
for i in my_dict1:
    if i not in my_dict2:
        my_dict_kay3[i] = my_dict1[i]
print(my_dict_kay3)
print("\n")

print("Г")
my_dict_kay4 = dict()
for i in my_dict1:
    if i not in my_dict2:
        my_dict_kay4[i] = my_dict1[i]
    else:
        my_dict_kay4[i] = my_dict1[i], my_dict2[i]
for i in my_dict2:
    if i not in my_dict1:
        my_dict_kay4[i] = my_dict2[i]
print(my_dict_kay4)