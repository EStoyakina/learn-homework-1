"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    a = input("Введите строку: ")
    b = input("Введите еще одну строку: ")
    if (type(a) != str) or (type(b) != str):
        print("0")
    elif a == b:
        print("1")
    elif a != b and len(a) > len(b):
        print("2")
    elif a != b and b == "learn":
        print("3")


if __name__ == "__main__":
    main()
