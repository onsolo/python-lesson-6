# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

import fractions

for i in range(1, 11):
    for k in range(2, 12):
        if i < k and fractions.Fraction(i, k).denominator == k:
            print(f'{i}/{k}')
