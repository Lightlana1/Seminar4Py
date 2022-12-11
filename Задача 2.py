# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input('Введите число: '))
def find_mult(num):
    lst = []
    div = 2
    while num > 1:
        while num % div == 0:
            lst.append(div)
            num //= div
        div += 1
    return lst
lst_number = find_mult(number)
print('Простые множители числа', number, ':', lst_number)