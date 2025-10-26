# Определяем класс Order
class Order:
    orders_quantity = 0# Атрибут класса: считает общее количество созданных заказов

    # Конструктор класса: вызывается при создании нового объекта Order
    def __init__(self):
        Order.orders_quantity += 1 # счётчик

        self.items = {}


    def add_item(self, item, price): # метод добавления товара

        if price <= 0: # проверка на положительность
            print("Ошибка: цена должна быть положительной!")
            return self.items  # Возвращаем текущий список без изменений

        self.items[item] = price# Добавляем или обновляем товар в словаре items

        print(f"Товар '{item}' добавлен с ценой {price}")

        return self.items

    def remove_item(self, item): # Метод удаления товара из заказа с подтверждением
        # Проверяем, есть ли такой товар в заказе
        if item not in self.items:
            print(f"Ошибка: товар '{item}' не найден в заказе.")
            return self.items  # Возвращаем без изменений

        confirmation = input(f"Вы уверены, что хотите удалить '{item}'? (да/нет): ").strip().lower()

        # Если пользователь подтвердил удаление
        if confirmation == "да":
            # Удаляем товар из словаря
            del self.items[item]
            print(f"Товар '{item}' успешно удалён.")
        else:
            print("Удаление отменено.")

        return self.items

    def get_total(self):
        # Суммируем все значения
        total = sum(self.items.values())
        return total

order = Order()# Создаём первый заказ

print("Добавляем товары...")
order.add_item("Хлеб", 50)
order.add_item("Молоко", 80)

print("\nОбщая стоимость:", order.get_total()) #

print("\nПопробуем удалить 'Хлеб':")
order.remove_item("Хлеб")

print("\nНовая общая стоимость:", order.get_total())

print(f"\nВсего заказов создано: {Order.orders_quantity}") #