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
student_1_result = (student_1_clas // 2) + student_1_clas % 2
student_2_result = (student_2_clas // 2) + student_2_clas % 2
student_3_result = (student_3_clas // 2) + student_3_clas % 2
student_result = student_1_result + student_2_result + student_3_result
print(f"Всього потрібно закупити {student_result} парт(и)")
print("\n")

#task 3
number = int(input("Введіть трьохзначне число: "))
cifra_1 = (number % 10) * 100
cifra_2 = ((number // 10) % 10) * 10
cifra_3 = number // 100

print(f" Перевернуте число {cifra_1 + cifra_2 + cifra_3}")