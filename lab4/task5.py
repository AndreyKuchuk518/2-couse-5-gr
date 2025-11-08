import matplotlib.pyplot as plt # Импорт библиотеки для гра-ка

categories = ['Яблоки', 'Бананы', 'Апельсины', 'Виноград', 'Киви']  # Названия категорий (будут на оси Y)
sales = [23, 45, 12, 34, 28]  # Значения продаж для каждой категории (будут на оси X)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(categories, sales, height=0.5, color='skyblue', edgecolor='navy') # первые идут Y а затем X

ax.set_title('Продажи фруктов за неделю', fontsize=16) # заголовок графика

ax.set_xlabel('Количество проданных единиц', fontsize=12)
ax.set_ylabel('Виды фруктов', fontsize=12)

ax.grid(axis='x', linestyle='--', alpha=0.6) # сетка по оси X для удобства прочтения

for i, value in enumerate(sales):
    ax.text(value + 1, i, str(value), va='center', fontsize=10) # подпись со значениями на концах столбцов

plt.tight_layout() # отступы

plt.savefig('horizontal_bar_chart.png', dpi=300, bbox_inches='tight')

plt.show()