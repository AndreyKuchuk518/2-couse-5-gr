input_numbers = input("Введите числа через пробел: ")
parts = input_numbers.split()

numbers = []
for part in parts:
    try:
        num = int(part)
        numbers.append(num)
    except ValueError:
        # Игнорируем нечисловые значения
        continue

if not numbers:
    print("Не введено ни одного числа.")
else:
    total = sum(numbers)  # можно использовать встроенную функцию sum()
    count = len(numbers)
    average = total / count

    print("Список:", numbers)
    print("Среднее арифметическое:", average)