# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.*
# Пример:
#
#             - 2*x² + 4*x + 5 = 0
#             - 5*x² + 2*x + 43 = 0
#             - Результат: 7*x^2 + 6*x + 48 = 0

with open('file.txt', 'r') as file:
    lst = file.readline()

with open('file2.txt', 'r') as file2:
    lst2 = file2.readline()

a, lit1, b, lit2, c,  lit3, d,  lit4,  e,  lit5, f,  lit6, n = lst[:-3].split()
a = int(a[:a.index('*')])
b = int(b[:b.index('*')])
c = int(c[:c.index('*')])
d = int(d[:d.index('*')])
e = int(e[:e.index('*')])
f = int(f[:f.index('*')])
n = int(n)

a1, lit11, b1, lit12, c1,  lit13, d1,  lit14,  e1,  lit15, f1,  lit16, n1 = lst2[:-3].split()
a1 = int(a1[:a1.index('*')])
b1 = int(b1[:b1.index('*')])
c1 = int(c1[:c1.index('*')])
d1 = int(d1[:d1.index('*')])
e1 = int(e1[:e1.index('*')])
f1 = int(f1[:f1.index('*')])
n1 = int(n1)


count = lst.count('*')

a2 = a + a1
b2 = b + b1
c2 = c + c1
d2 = d + d1
e2 = e + e1
f2 = f + f1
n2 = n + n1

lst = [a2, '*x^', count, ' + ', b2, '*x^', count-1, ' + ', c2, '*x^', count-2, ' + ', d2, '*x^', count-3, ' + ', e2, '*x^', count-4,' + ', f2, '*x^', count-5, ' + ', n2, ' = 0']

with open("file3.txt", "w") as file:
    for items in lst:
        file.write('%s' % items)