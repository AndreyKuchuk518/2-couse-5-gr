class Order:
    orders_quantity = 0

    def __init__(self):
        self.items = {}
        Order.orders_quantity += 1

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"\n[Успешно] Товар '{item_name}' добавлен в заказ по цене {price} руб.")

    def remove_item(self, item_name):
        if item_name in self.items:
            while True:
                prompt = f"Вы уверены, что хотите удалить '{item_name}'? (да/нет): "
                confirmation = input(prompt).lower().strip()
                if confirmation == 'да':
                    del self.items[item_name]
                    print(f"\n[Успешно] Товар '{item_name}' был удалён.")
                    break
                elif confirmation == 'нет':
                    print("\n[Отмена] Удаление отменено.")
                    break
                else:
                    print("\n[Ошибка] Пожалуйста, введите 'да' или 'нет'.")
        else:
            print(f"\n[Ошибка] Товар '{item_name}' не найден в вашем заказе.")

    def get_total(self):
        return sum(self.items.values())


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()  # .strip() убирает пробелы по краям
        if value:  # пустая строка после .strip() расценивается как False
            return value
        else:
            print("[Ошибка] Ввод не может быть пустым. Попробуйте еще раз.")


def get_valid_price():
    while True:
        price_str = input("Введите цену товара: ")
        try:
            price = float(price_str)  # Попытка превратить строку в число
            if price > 0:
                return price  # если получилось и число > 0, возвращаем его
            else:
                print("[Ошибка] Цена должна быть положительным числом. Попробуйте еще раз.")
        except ValueError:
            print("[Ошибка] Введите числовое значение (например, 150 или 99.50). Попробуйте еще раз.")



def show_menu():

    print("\n" + "-" * 30)
    print("МЕНЮ УПРАВЛЕНИЯ ЗАКАЗОМ:")
    print("1. Добавить товар в заказ")
    print("2. Удалить товар из заказа")
    print("3. Показать текущий заказ и стоимость")
    print("4. Выйти из программы")
    print("-" * 30)


def main():    # интерактивный цикл программы
    print("Система управления заказами")
    my_order = Order()

    while True:
        show_menu()
        choice = input("Выберите действие (введите номер): ")

        if choice == '1':
            print("\n--- Добавление нового товара ---")
            # Теперь мы используем наши новые функции-помощники
            item_name = get_non_empty_string("Введите название товара: ")
            item_price = get_valid_price()

            # Мы вызываем метод add_item только с уже проверенными данными
            my_order.add_item(item_name, item_price)

        elif choice == '2':
            if not my_order.items:
                print("\n[Информация] Ваш заказ пока пуст, удалять нечего.")
                continue

            print("\n--- Удаление товара ---")
            item_name = get_non_empty_string("Введите название товара, который хотите удалить: ")
            my_order.remove_item(item_name)

        elif choice == '3':
            items = my_order.items
            print("\n" + "--- ВАШ ТЕКУЩИЙ ЗАКАЗ ---")
            if not items:
                print("Заказ пока пуст.")
            else:
                for name, price in items.items():
                    print(f"- {name}: {price} руб.")
            print("--------------------------")
            print(f"Общая стоимость: {my_order.get_total()} руб.")
            print("--------------------------")

        elif choice == '4':
            print("\nСпасибо за использование нашей системы.")
            break
        else:
            print("\n[Ошибка] Неверный выбор. Пожалуйста, введите число от 1 до 4.")


if __name__ == "__main__":
    main()