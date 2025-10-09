# Задание 13: z1 и z2
import math  
alpha = math.pi / 2

sin_3alpha = math.sin(3 * alpha)

if sin_3alpha == 0:
    print("Ошибка: sin(3a) = 0, деление на ноль!")
else:
    
    sin_inv_squared = 1 / (sin_3alpha ** 2)
    cos_2alpha = math.cos(2 * alpha)

    z1 = 1 - (1/4) * sin_inv_squared + 3 * cos_2alpha
    cos_3alpha = math.cos(3 * alpha)
    sin_alpha = math.sin(alpha)

    z2 = (cos_3alpha ** 2) + (sin_alpha ** 4)

    print(f"Значение α = {alpha} радиан ({math.degrees(alpha)} градусов)")
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")
