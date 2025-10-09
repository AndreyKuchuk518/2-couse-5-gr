numbers = [5, 10, 12, 15, 20, 23, 25, 30]

filtered_numbers = [] # список с не делящимися на 5 числами

for num in numbers:
    if num % 5 != 0:
        filtered_numbers.append(num)

print("Исходный список:", numbers)
print("Список без чисел, делящихся на 5:", filtered_numbers)
