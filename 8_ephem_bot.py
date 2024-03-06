"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Привет! Ты вызвал команду start")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def my_constellation(update, context):
    text = 'Вызван /planet'
    print(text)
    update.message.reply_text(f"Введите название планеты из списка: {', '.join(planets)}")
    user_planet_choice = planets
    if user_planet_choice == "Mercury":
        update.message.reply_text(ephem.constellation(ephem.Mercury('2024/02/29')))
    elif  user_planet_choice == "Venus":
        update.message.reply_text(ephem.constellation(ephem.Venus('2024/02/29')))
    elif user_planet_choice == "Earth":
        update.message.reply_text(ephem.constellation(ephem.Earth('2024/02/29')))
    elif user_planet_choice == "Mars":
        update.message.reply_text(ephem.constellation(ephem.Mars('2024/02/29')))
    elif user_planet_choice == "Jupiter":
        update.message.reply_text(ephem.constellation(ephem.Jupiter('2024/02/29')))
    elif user_planet_choice == "Saturn":
        update.message.reply_text(ephem.constellation(ephem.Saturn('2024/02/29')))
    elif user_planet_choice == "Uranus":
        update.message.reply_text(ephem.constellation(ephem.Uranus('2024/02/29')))
    elif user_planet_choice == "Neptune":
        update.message.reply_text(ephem.constellation(ephem.Neptune('2024/02/29')))
    else:
        print("Планета неизвестна")


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", my_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

