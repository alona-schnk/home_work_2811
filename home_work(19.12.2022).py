#task 1

my_string = "0123456789"
for i in my_string:
    for j in my_string:
        if i == "0":
            print(int(j), end=" ")
            continue
        if i == "5" and j =="0" :
            print("\n")
        print(int(i), int(j), sep="", end=" ")

print("\n")

#task2
def trigonimetria():
    high: int = int(input("Введіть висоту: "))
    if high >= 3 and high % 2 != 0:
    #A
        for i in range(high-1):
            for j in range(2 * high + 1):
                if (high - j == i) or (j - high == i) or i == high:
                    print("*", end='')
                else:
                    print(" ", end='')
            print()
        print(" *" * high)

        print("\n")


    #B
        for i in range(1, high + 1):
            width = high - i
            print(" " * width + "* " * i)
        print("\n")


    #C
        for i in range(1, high + 1):
            width = high - i
            print(" " * width + " *" * i)
        for i in range(high - 2, 0, -1):
            for j in range(2 * high, 0, -1):
                if (high - j == i) or (j - high == i) or i == high:
                    print("*", end='')
                else:
                    print(" ", end='')

            print()
        print((high - 1) * " ", "*")

        print("\n")


    #D
        for i in range(1, high + 1):
            width = high - i
            print(" " * width + " *" * i)
        for i in range(high - 2, 0, -1):
            for j in range(2 * high, 0, -1):
                if (high - j == i) or (j - high == i) or i == high or j == high:
                    print("*", end='')
                else:
                    print(" ", end='')
            print()

        print((high - 1) * " ", "*")
    else:
        print("Введіть непарне число: ")
        trigonimetria()


trigonimetria()



