import main_11

with open(input("Введіть назву файла для TASK1 в форматі 'файл.txt': ")) as file1:
    forbidden = input("Введіть слова для заміни в список: ").split()
    text1 = file1.read()
with open(input("Введіть назву файла для TASK2 в форматі 'файл.txt': ")) as file2:
    text2 = file2.read()
main_11.redactor(text1, forbidden)
main_11.calk_kay(text2.split())


