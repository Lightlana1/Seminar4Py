# Вычислить число ПИ c заданной точностью d
#
#     *Пример:*
#
#     - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10

import math
a = str(math.pi)
import random
n = int(random.uniform(1, 6))
print('Показать число ПИ в формате:', 10**(-n))
for i in range(n+2):
    print(a[i], end='')