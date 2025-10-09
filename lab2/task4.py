input_numbers = input("Введите числа через пробел: ")
numbers = list(map(int, input_numbers.split()))

total = 0
for num in numbers:
    total = total + num  #сумма

count = len(numbers)  # для подсчёта элементов
average = total / count

print("Список:", numbers)
print("Среднее арифметическое:", average)
