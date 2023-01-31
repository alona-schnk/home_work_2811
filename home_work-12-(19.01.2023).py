import main_12

with open(input("Введіть назву файла для TASK1 в форматі 'файл.txt': ")) as file1:
    forbidden = input("Введіть слова для заміни в список: ").split()
    text1 = file1.read()

main_12.censor1(text1, forbidden)
main_12.censor2(text1.split())
main_12.censor3(text1.split())