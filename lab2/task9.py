n = int(input("Введите число N: "))
divisors_count = {}

for i in range(1, n + 1):  # перебираем числа от 1 до N.
    count = 0  # счётчик делителей для числа i
  
    for j in range(1, i + 1):    # перебираем возможные делители от 1 до i.
        if i % j == 0:  # если i делится на j без остатка — j — делитель
            count += 1
    divisors_count[i] = count

print("Словарь количества делителей:")
for key, value in divisors_count.items():
    print(f"{key}: {value} делителей")
