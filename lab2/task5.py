strings = ("яблоко", "банан", "ананас", "мандарин", "арбуз")
longest = strings[0]  # пусть первый элемент самый длинный

for s in strings: # перебор элементов
    if len(s) > len(longest): # len - определяет длину строки
        longest = s

print("Кортеж строк:", strings)
print("Самая длинная строка:", longest)
print("Её длина:", len(longest))
