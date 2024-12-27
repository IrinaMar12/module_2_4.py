numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    is_prime = True # Предполагаем, что число простое
    if num <= 1:
        is_prime = False # 1 и числа меньше 1 не являются простыми
    else:
        for i in range(2, num): # Проверяем делимость на числа от 2 до num-1
            if num % i == 0:
                is_prime = False # Если делится без остатка, то не простое
                break # Выходим из внутреннего цикла, т.к. уже знаем, что не простое

    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print("Простые числа:", primes)
print("Не простые числа:", not_primes)
