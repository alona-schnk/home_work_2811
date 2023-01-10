#task 1
cifra_input_1 = int(input("Введіть перше число: "))
cifra_input_2 = int(input("Введіть друге число: "))
operand_input = input("Введіть операнд (+, -, /, *, **): ")
if "+" in operand_input:
    result = cifra_input_1 + cifra_input_2
    print(result)
elif "-" in operand_input:
    result = cifra_input_1 - cifra_input_2
    print(result)
elif "/" in operand_input:
    if cifra_input_2 == 0:
        print('На нуль ділити не можна!')
    else:
        result = cifra_input_1 / cifra_input_2
        print(result)
elif "**" in operand_input:
    result = cifra_input_1 ** cifra_input_2
    print(result)
elif "*" in operand_input:
    result = cifra_input_1 * cifra_input_2
    print(result)
else:
    print("Non operand")
print("\n")

#task 2
cifra_n = int(input("Введіть число N: "))

for i in range(1, cifra_n):
    if i ** 2 <= cifra_n:
        print(i ** 2, end=" ")
print("\n")

# task 3
chislo = int(input("Введіть число: "))
count = 0
for i in range(1, chislo + 1):
    if chislo % i == 0:
        count = count + 1
        if count == 3:
            print("No")
            break
else:
    print("Yes")

