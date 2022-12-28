#task 3
print("TASK 3")
my_list31 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list32 = [9, 10, 11, 12, 13, 14, 15, 16]
my_result = []
my_result.extend(my_list31[::2] + my_list32[1::2])
print(my_result)

print("\n")

#task 11
print("TASK 11")
my_stroka = "Alona Lo search to picture "
my_set = set(my_stroka)
my_list11 = []
for letter in my_set:
    if my_stroka.count(letter) == 1:
        my_list11.append(letter)
print(my_list11)

print("\n")

#task 4
print("TASK 4")
my_list = ("1 2 3 4").split(" ")
new_list = my_list[1:] + [my_list[0]]
print(new_list)

print("\n")

#task 5
print("TASK 5")
my_list = ("1 2 3 4").split(" ")
list = my_list.pop(0)
my_list.append(list)
print(my_list)

print("\n")

#task 6
print("TASK 6")
my_list = ("43 34 56").split(" ")
res = 0
for i in range(len(my_list)):
    res += int(my_list[i])
print(res)



