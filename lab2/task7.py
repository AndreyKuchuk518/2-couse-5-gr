text = input("Введите строку: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"  # Определяем гласные буквы 

consonant_count = 0 # счётчик согласных

for char in text: # перебор каждого символа
    if char.isalpha():  # isalpha() — проверяет, буква ли это
        if char not in vowels:  # если не гласная — значит, согласная
            consonant_count += 1

print("Количество согласных букв:", consonant_count)
