# Объявляем пакеты в порядке их значимости и веса в проекте: чего больше, то и первое
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

# Свои импорты определяем после основных от pip
import settings


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')
# Ты определила logging. Почему ты не помогаешь себе им в хендлерах???
# Твой друг в тестировании -- logging! Не print, а logging!
# Добавляем logging.info и чаще смотрим bot.log

# Константы пишем капслоком
# Землю убираем из списка, в модуле ephem нет параметра Earth
PLANETS = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# После определения переменных оставляем 2 пустых строки до определения функций или классов


# Все хендлеры (обработчики команд Телеграм бота импортированы как параметр функции dp.add_handler(CommandHandler())),
# Многие линтеры будут ругаться, т.к. не знают, нафига тут в функциях стоит неявный параметр context
# Если в данный момент ты этот параметр не используешь явно в своих функциях (даже если он нужен системе),
# то принято его прикрывать безымянной заглушкой "_": 'context' rename to '_'
def greet_user(update, _):
    # Класс информирования "обычный", оставляем логи в системе при каждом обработчике запроса от пользователя
    logging.info('greet_user: Отправлена команда: /start')
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Привет! Ты вызвал команду start")


def talk_to_me(update, _):
    text = update.message.text
    logging.info(f'talk_to_me: Отправлен текст: {text}')
    print(text)
    update.message.reply_text(text)


# Названия всего-всего в коде должно быть более информативным.
# Каждая функция своим названием должна говорить, что она делает
def get_constellation_by_planet_name(update, _):
    text_list = update.message.text.split()

    # Пришла команда с дополнительным параметром
    if len(text_list) > 1:
        planet_name = text_list[1]
        # Дата повторяется, определяем для нее переменную
        check_date = '2024/02/29'

        # Известная планета, определяем созвездие
        if planet_name in PLANETS:
            logging.info(f'get_constellation_by_planet_name: Вызвана команда /planet с названием планеты {planet_name}')

            # У тебя в каждом if в действии делается одно и то же тройное действие:
            # update.message.reply_text(ephem.constellation(ephem.Mercury('2024/02/29')))
            # Делаем это действие для всех корректных случаев сразу
            if planet_name == "Mercury":
                planet = ephem.Mercury(check_date)
            elif planet_name == "Venus":
                planet = ephem.Venus(check_date)
            elif planet_name == "Mars":
                planet = ephem.Mars(check_date)
            elif planet_name == "Jupiter":
                planet = ephem.Jupiter(check_date)
            elif planet_name == "Saturn":
                planet = ephem.Saturn(check_date)
            elif planet_name == "Uranus":
                planet = ephem.Uranus(check_date)
            elif planet_name == "Neptune":
                planet = ephem.Neptune(check_date)

            # Определить созвездие по планете
            update.message.reply_text(ephem.constellation(planet))

        # Неизвестная планета
        else:
            logging.info(f'get_constellation_by_planet_name: Вызвана команда /planet с параметром {planet_name}')
            print("Планета неизвестна")
            update.message.reply_text(f"Отправьте команду /planet с названием планеты из списка: {', '.join(PLANETS)}")

    # команда /planet пришла без параметра
    else:
        logging.info('get_constellation_by_planet_name: Вызвана команда /planet без дополнительных параметров')
        update.message.reply_text('Отправьте команду /planet с названием планеты.')


def main():
    # Можно забыть вставить Telegram, проверяем этот случай
    token = settings.TOKEN
    if not token:
        # Класс информирования "критический": вывести ошибку
        logging.error('main: Check settings.TOKEN parameter, please')
        print('Параметр settings.TOKEN не установлен.')
        return None

    # Всё норм, TOKEN есть, запуск бота...
    mybot = Updater(settings.TOKEN)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation_by_planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Команды друг от друга отделяются на 0 или 1 строчку, не больше. Было 2 пустые строки

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

# После завершения кода в файле, в Python ставится одна пустая строка, именно одна (было 2 пустых строчки :) )
