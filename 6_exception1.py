"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_say = input("Как дела? ")
        if user_say == "Хорошо":
            try:
                print("Рад за тебя")
            except KeyboardInterrupt:
                print("Пока!")
            break
        else:
            print(user_say)




if __name__ == "__main__":
    hello_user()
