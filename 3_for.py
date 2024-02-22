"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
def count_items_sum(quantity):
    items_sum = 0
    for items in quantity:
        items_sum += items
    return items_sum
all_items_sum = 0
for one_product in sales:
        items_sum = count_items_sum(one_product["items_sold"])
        print(f'Суммарное количество продаж каждого товара: {one_product["product"]}: {items_sum}')
        all_items_sum += items_sum
print(f'Суммарное количество продаж всех товаров: {all_items_sum}')
def count_items_avg(quantity):
    items_sum = 0
    for items in quantity:
        items_sum += items
    return items_sum / len(quantity)
items_avg_sum = 0
for one_product in sales:
        items_sum = count_items_avg(one_product["items_sold"])
        print(f'Среднее количество продаж каждого товара: {one_product["product"]}: {items_sum}')
        items_avg_sum += items_sum
print(f'Cреднее количество продаж всех товаров:{items_avg_sum / len(sales)}')










if __name__ == "__main__":
    main()
