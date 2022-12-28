import random


my_list = [random.randint(1, 200) for i in range(20)]
print("\n")

# #task 1
print("TASK 1")
print("Початковий список: ", my_list)
print("РЕЗУЛЬТАТ")
for i in range(len(my_list)):
    if my_list[i] > 100:
        print(my_list[i], end=" ")

print("\n")

#task 2
print("TASK 2")
print("Початковий список: ", my_list)
print("РЕЗУЛЬТАТ")
my_result = []
for i in range(len(my_list)):
    if my_list[i] > 100:
        my_result.append(my_list[i])
print(my_result)
print("\n")

#task 3
print("TASK 3")
print("Початковий список: ", my_list)
print("РЕЗУЛЬТАТ")
if len(my_list) >= 2:
    res = my_list[-1] + my_list[-2]
    my_list.append(res)
else:
    my_list.append(0)
print(my_list)
print("\n")

# #task 4
print("TASK 4")
print("Початковий список: ", my_list)
k = int(input("Вкажіть індекс елемента, який елемент потрібно видалити: "))
print("РЕЗУЛЬТАТ")
for i in range(k,len(my_list) - 1):
   my_list[i] = my_list[i + 1]
my_list.pop(len(my_list) - 1)
for i in range(len(my_list)):
   print(my_list[i], end=' ')
print("\n")

# #task 5
print("TASK 5")
my_list5 = [random.randint(1, 20) for i in range(10)]
print("Початковий список: ", my_list5)
k = int(input("Введіть значення на яку позицію поставити елемент С: "))
c = int(input("Введіть елемент С: "))
print("РЕЗУЛЬТАТ")
my_list5.append(0)
for j in range(len(my_list5) - 1, k, -1):
     my_list5[j] = my_list5[j - 1]
my_list5[k] = c
print(' '.join([str(j) for j in my_list5]))

print("\n")

# #task 6
print("TASK 6")
my_list61 = [random.randint(1, 20) for i in range(10)]
my_list62 = [random.randint(1, 20) for i in range(10)]
print("Початковий список: ", my_list61, "+", my_list62)
print("РЕЗУЛЬТАТ")
for i in range(len(my_list61 + my_list62)):
     for j in range(len(my_list61 + my_list62)):
          if i != j and (my_list61 + my_list62)[i] == (my_list61 + my_list62)[j]:
               break
     else:
          print((my_list61 + my_list62)[i], end=' ')

