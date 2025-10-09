info = {
    "a": 5,
    "b": 15,
    "c": 8,
    "d": 20,
    "e": 3
}

filtered_info = {}

for key, value in info.items():   # перебор все пары ключ-значение, items возвращает ключ и значение отновременно
    
    if value >= 10:
        filtered_info[key] = value # добавляем пару в словарь

print("Исходный словарь:", info)
print("Словарь отфильтрованный:", filtered_info)
