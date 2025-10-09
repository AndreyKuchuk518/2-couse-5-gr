input_numbers = input("Введите числа через пробел: ")
numbers = list(map(int, input_numbers.split()))

even_sum = 0  # сумма чётных
odd_sum = 0   # сумма нечётных

for num in numbers:   #Перебор чисел
    if num % 2 == 0:  
        even_sum += num
    else:             
        odd_sum += num

difference = even_sum - odd_sum

print("Список:", numbers)
print("Сумма чётных:", even_sum)
print("Сумма нечётных:", odd_sum)
print("Разность (чётные - нечётные):", difference)
