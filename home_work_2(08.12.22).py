#task 1
student = int(input("Скільки учнів: "))
apple = int(input("Скільки яблук у корзині: "))
student_apple_result = apple // student
apple_box_result = apple % student
print(f"У кожного учня по {student_apple_result} яблук, а в корзині залишилось {apple_box_result} яблук")
print("\n")
#task 2
student_1_clas = int(input("Скільки учнів у 1 класі: "))
student_2_clas = int(input("Скільки учнів у 2 класі: "))
student_3_clas = int(input("Скільки учнів у 3 класі: "))
student_result = student_1_clas + student_2_clas + student_3_clas
table_result = student_result // 2
student_ostatok = student_result % 2
result_class = table_result + student_ostatok
print(f"Всього потрібно закупити {result_class} парт")
print("\n")

#task 3
number = int(input("Введіть трьохзначне число: "))
cifra_1 = number % 10
cifra_2 = (number // 10) % 10
cifra_3 = number // 100
print(f" Перевернуте число {cifra_1}{cifra_2}{cifra_3}")