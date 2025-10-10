n = input("Введите число N: ")  

product = 1 
found_digit = False

for char in n:
    if char.isdigit():  # проверяет есть цифры
        digit = int(char)
        product = product * digit
        found_digit = True
     
if found_digit:
    print("Произведение всех цифр в строке:", product)
else:
    print("В строке не было цифр.")
