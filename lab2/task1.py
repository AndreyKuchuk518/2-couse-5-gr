n = input("Введите число N: ")  
product = 1  

for digit_char in n:
    digit_int = int(digit_char)
    product = product * digit_int

print("Произведение всех цифр числа:", product)
