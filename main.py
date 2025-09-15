while True:
    a = int(input("Введите положительное целое число a больше 0 = "))
    if a > 0:
        break
    else:
        print("Попробуйте еще раз")

while True:
    b = int(input("Введите положительное целое число b больше 0 = "))
    if b > 0:
        break
    else:
        print("Попробуйте еще раз")

print("Для чисел ", a, " и", b, " НОД равен")

while a!=0 and b!=0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)