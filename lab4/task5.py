import matplotlib.pyplot as plt

# Данные
categories = ['Категория A', 'Категория B', 'Категория C', 'Категория D']
values = [23, 45, 56, 78]

# Создаём фигуру
plt.figure(figsize=(8, 6))

# Построение горизонтальной столбчатой диаграммы
# Вместо plt.bar(categories, values) используем plt.barh
plt.barh(categories, values, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

# Подписи
plt.title('Горизонтальная столбчатая диаграмма')
plt.xlabel('Значения')
plt.ylabel('Категории')

# Сетка
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Сохранение и отображение
plt.savefig('task5.png', dpi=300, bbox_inches='tight')
plt.savefig('task5.pdf', bbox_inches='tight')
plt.show()