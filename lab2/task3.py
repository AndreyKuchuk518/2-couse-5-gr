input1 = input("Введите элементы первого множества через пробел: ")
set1 = set(map(int, input1.split())) #split разбивает на пробелы мап применяет функцию инт к каждому элементу сет - создаёт множество

input2 = input("Введите элементы второго множества через пробел: ")
set2 = set(map(int, input2.split()))

only_in_one = set1.symmetric_difference(set2)

print("Множество 1:", set1)
print("Множество 2:", set2)
print("Элементы, которые есть только в одном из множеств:", only_in_one)
