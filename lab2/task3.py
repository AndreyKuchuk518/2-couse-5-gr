# Задание 14: Множества

my_set = {1, 2, 3, 4, 5}
print("Исходное множество:", my_set)


my_set.add(6)
print("После добавления 6:", my_set)


my_set.remove(3)  
print("После удаления 3:", my_set)


element_to_check = 4
if element_to_check in my_set:
    print(f"Элемент {element_to_check} присутствует в множестве")
else:
    print(f"Элемент {element_to_check} отсутствует в множестве")


another_set = {4, 5, 6, 7, 8}


union_set = my_set | another_set # объединение
print("Объединение:", union_set)


intersection_set = my_set & another_set  # Пересечение 
print("Пересечение:", intersection_set)


difference_set = my_set - another_set
print("Разность (my_set - another_set):", difference_set)
