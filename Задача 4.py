# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k(до 6 степени).*
#
#         *Пример:*
#
#         - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Введите степень многочлена от 1 до 6: '))
import random
a = int(random.uniform(0, 10))
b = int(random.uniform(0, 10))
c = int(random.uniform(0, 10))
d = int(random.uniform(0, 10))
e = int(random.uniform(0, 10))
f = int(random.uniform(0, 10))
n = int(random.uniform(0, 10))
print(a, b, c, d, e, f, n)
str = []
if k == 6:
    str = [a,'*x^6 + ',b,'*x^5 + ',c,'*x^4 + ',d,'*x^3 + ',e,'*x^2 + ',f,'*x + ',n,' = 0']
if k == 5:
    str = [b,'*x^5 + ',c,'*x^4 + ',d,'*x^3 + ',e,'*x^2 + ',f,'*x + ',n,' = 0']
if k == 4:
    str = [c,'*x^4 + ',d,'*x^3 + ',e,'*x^2 + ',f,'*x + ',n,' = 0']
if k == 3:
    str = [d,'*x^3 + ',e,'*x^2 + ',f,'*x + ',n,' = 0']
if k == 2:
    str = [e,'*x^2 + ',f,'*x + ',n,' = 0']
if k == 1:
    str = [f,'*x + ',n,' = 0']

for i in range(len(str)):
    if str[i] == 0:
        str[i] = 'del'
        n = i + 1
        str[n] = 'del'

str2 = []
for i in range(len(str)):
    if str[i] != 'del':
        str2.append(str[i])

with open("file.txt", "w") as file:
    for items in str2:
        file.write('%s' % items)


