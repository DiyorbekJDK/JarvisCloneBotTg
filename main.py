import telebot
import random
import time
from telebot import types
import os

bot = telebot.TeleBot('6217254132:AAEdGaOyvaQMTLqffnGtUheeWpejnqgUmNs')
print("bot started")

random_sticker_list = ["CAACAgIAAxkBAAEKV9ZlCr7-ZsDOiNCL2bdpVJdLKePiIgAC0wgAAmxpeEhutjKphXzGUDAE",
                       "CAACAgIAAxkBAAEKV9plCr8Q1fkquXAvQN0BBuu0Ik0dagACaR4AAh3tYUkpdZKPeRAC_jAE",
                       "CAACAgIAAxkBAAEKV9xlCr8d_GU8fPDnDIH4cvbqpU2KCQACFwkAAobXeEjwOpl9qSewaTAE",
                       "CAACAgIAAxkBAAEKV95lCr8fWg2bglaXI6K7W_CAC6mcbAACtAkAAoK1eUjLqezXdkUPwDAE",
                       "CAACAgIAAxkBAAEKV-BlCr87kDNDY9hQlH9Zro49RFlovgACTQkAAnYreUgDJEKDRPfmCDAE",
                       "CAACAgIAAxkBAAEKV-JlCr896715aySjmQL0Wz_ZW4Pc6QACQAoAA4h4SDdg9Kl-RqBqMAQ",
                       "CAACAgIAAxkBAAEKV-RlCr8_S6wVh97uxSNgtvJOgvrOcwACgAoAAn-IeUgQj9SZDgzuSTAE",
                       "CAACAgIAAxkBAAEKV-ZlCr9BkSUmhnJlf3GIo-7NRDZV4gACPgoAAkRoeEjk3oI22WsWQTAE",
                       "CAACAgIAAxkBAAEKV-hlCr9EJJK-i4No7uohKZ-QeGNHiAACGAwAAvE8eUikdLCSqv4MHjAE",
                       "CAACAgIAAxkBAAEKV-plCr9G5gKEYJ4hnvcEYskz5EKFcgACGgcAAnT3eUhYeUB74HivvDAE",
                       "CAACAgIAAxkBAAEKV-xlCr9HXQde8WgRBd6moZtnqV_riwAClwoAAubLeEiZZiDo53Y34zAE",
                       "CAACAgIAAxkBAAEKV-5lCr9LmSyWFHugjpj_QoP7E3gH5QACiwgAAub8cUh80WZ4Zf8UujAE",
                       "CAACAgIAAxkBAAEKV_BlCr9N-4SeqpMzba234xH5UHiWvQACKQkAArZCeEgyGp9fixDGCDAE",
                       "CAACAgIAAxkBAAEKV_JlCr9QLlyR67WAY2_mJHaoPedGWAACUQsAAuyPeEgmAAEJlOjDHmcwBA",
                       "CAACAgIAAxkBAAEKV_ZlCr9U-t1Cq1l3PwWHGB6meHz1MgACQQkAApzGeUjCxJbPUqXv8TAE",
                       "CAACAgIAAxkBAAEKV_hlCr_r3W9gZcg86ovyThtuxKBn1QACaA8AAi38AUnlpsXzzLmvFjAE",
                       "CAACAgIAAxkBAAEKV_plCsAJWSyEeE3DT71JvweOBqvB4QACtCwAAo1rqEitTV7X93F1CjAE",
                       "CAACAgIAAxkBAAEKV_xlCsGe0lEVBKerH9J4AaLyFQh6MAAChR4AAkS4cEud4F6td2-uQzAE",
                       "CAACAgIAAxkBAAEKV_5lCsHzJtpdYZ5qlGWUFrhBYpPtwwACZwMAAvzsFz7gwTU5voorgDAE",
                       "CAACAgIAAxkBAAEKWAABZQrB-P_kZSvOi3fxUkYIqVV0pnoAAl4EAAL87Bc-P_f6TOpSRVMwBA",
                       "CAACAgIAAxkBAAEKWAJlCsH8sK4AAdK_Lz7F9yYhHDhpGdgAAnkEAAL87Bc-iDNJZuM0olwwBA",
                       "CAACAgIAAxkBAAEKWARlCsIAAb0lVrqcOj_qdAEhMJz6wfsAApQbAAIpZvlKZBWvqCSvDn4wBA",
                       "CAACAgIAAxkBAAEKWAZlCsIDvGWLkK0ZJviAULY7J7BfwAACOiAAAqmb6Ui7OGd7pdRFaTAE",
                       "CAACAgIAAxkBAAEKWAhlCsIFlfC4BwRq8wZe2EtR7SmQqgACiiYAAsyrSEmmn6tyU2qswzAE",
                       "CAACAgIAAxkBAAEKWAplCsII53EmXeKE3LJwnoIJ_EFIXwACIycAAn8oQEnd8DQf-moF8jAE",
                       "CAACAgIAAxkBAAEKWAxlCsJXLqx8kNKpSSZ5HEJUMl_nqAACXCUAAlVOSUmsmGEiX5icijAE"
                       ]
hello_sticker_list = [
    "CAACAgIAAxkBAAEKWBBlCsRY0CYL8eFnpWXPixrqWF1QsQACyCkAAhDrWUmLx3dgYPgVTTAE",
    "CAACAgIAAxkBAAEKWA5lCsQYotoP-NrSvyr4PXOJo3ysyAACjSQAAr8OSUnzmyS_A8yCtTAE",
    "CAACAgIAAxkBAAEKWA5lCsQYotoP-NrSvyr4PXOJo3ysyAACjSQAAr8OSUnzmyS_A8yCtTAE",
    "CAACAgIAAxkBAAEKYCxlD-eJbMCBQmrYFWx2drq2Ojw3lwACcSoAAsgt8UknhfArLvXSZTAE",
    "CAACAgIAAxkBAAEKYC5lD-eaJFHrh2N43EVZD_TAWycAAe8AAi4AA9n1Mgox-JrplWWsfzAE",
    "CAACAgIAAxkBAAEKYDBlD-erIZvyDs4xpxjTjTWr_Ra5FwACEyIAAiO60ErugP0LGPd1mzAE",
    "CAACAgIAAxkBAAEKYDJlD-e8XzX8hR_IwK6Umj_GQjEfOQAC-xUAAgLfUUlAKQs-3ZtHgTAE",
    "CAACAgIAAxkBAAEKYDRlD-fL8qQvm8XEASqPOgkTrKWfpwACPBMAAoElyUsiXeSDccqJwzAE",
    "CAACAgEAAxkBAAEKYDZlD-fVCxl31t65agIoaoaKWJR2cQACpQIAAkb-8Ec467BfJxQ8djAE",
    "CAACAgIAAxkBAAEKYDhlD-fuS_mSMwm1Bf1Xzig4yBlVpQACgyIAAuZDUErZXGjKdYmCWzAE",
    "CAACAgIAAxkBAAEKYDplD-gIg0PxZ7yvaBDN8S7DnYErwQACBQEAArhnMQ9dxHUkfc1rITAE",
    "CAACAgIAAxkBAAEKYD9lD-gfd-9qfVLVUASaxWwYR3UqBwACggADuGcxD6ergfjePzsoMAQ",
    "CAACAgIAAxkBAAEKYENlD-gtqGtQm_xPfThrMMGsIvEoYwACIAgAAkVRkw70vQtHNDxB-DAE",
    "CAACAgIAAxkBAAEKYEVlD-hWlVse4qZ2UYvXSteTiURr5wAClAgAAkVRkw5a5g9obirzzzAE",
    "CAACAgIAAxkBAAEKYEdlD-hgKl53Qi1QLZHKF-LKZNgXIgAClQgAAkVRkw5jfKB0Pcvj7jAE"

]
hello_text_list = [
    'дарова',
    'даров',
    'пр',
    'привет',
    'ку',
    'ну чё как',
    'вечер в хату',
    'привет лохи',
    'саламалекум',
    'салам',
    'админ в чате',
    'босс в чате',
    'прив',
    'драсьте',
    'здраствуйте',
    'здрасте',
    'добрый день',
    'добрый вечер'
]
hello_answer_text_list = [
    'ну чё как',
    'пр',
    'даров',
    'прив',
    'ку',
    'привет',
    'здарова!',
    'салам бро',
    'салам',
    'саламалейкум',
    'дратуйте',
    'добрый день',
    'добрый вечер',
    'доброе утро'
]
bad_words_list = [
    "жопа",
    "пизда",
    "пиздец",
    "хуй",
    "нахуй",
    "сука",
    "хуйня",
    "блять",
    "мразь",
    "су ка",
    "с у к а",
    "пидор",
    "пидорас",
    "пидоры",
    "писька",
    "ж о п а",
    "жо п а",
    "жо па",
    "пи до р",
    "лох",
    "ебать",
    "ебанись",
    "сусука",
    "лошара",
    "сукасука",
    "суксука",
    "пидорасс",
    "писюн",
    "писюна",
    "похуй",
    "гей",
    "уебан"
]
happy_evening_text_list = [
    'jarvis запусти протокол др',
    'жарвис запусти протокол др',
    'запусти протокол др',
    'протокол др',
    'жарвис запусти протокол веселый вечер',
    'жарвис запусти протокол весёлый вечер',
    'jarvis запусти протокол веселый вечер',
    'jarvis запусти протокол весёлый вечер',
    'протокол веселый вечер',
    'активировать протокол весёлый вечер',
]
osk_text_list = [
    'иди в жопу',
    'иди в жопу!',
    'иди нахуй',
    'Иди на хуй',
    'джарвис ты гей',
    'жарвис ты гей',
    'ты пидор?',
    'чмо',
    'ты пидр',
    'ты пидр?',
]
dance_text_list = [
    'танцуй',
    'танцуй!',
    'жарвис запусти протокол танцы',
    'jarvis запусти протокол танцы',
    'запусти протокол танцы',
    'протокол танцы',
    'танцы'
]
praise_words_lis = [
    'мило',
    'молодец',
    'харош',
    'лучший',
    'умничка',
    'топ',
    'топчик',
    'тоже доброго дня'
]
rest_text_list = [
    'всё жарвис отдыхай',
    'жарвис спи',
    'жарвис иди спи',
    'жарвис отдыхай',
    'жарвис иди отдыхай',
    'жарвис спать',
    'всё jarvis отдыхай',
    'jarvis спи',
    'jarvis отдыхай',
    'jarvis спать',
    'джарвис спать',
]
dance_stickers_list = [
    'CAACAgIAAxkBAAEKbPtlGQFJJQdtqZs7aXDZx1n8rZSnKgACOyIAAr7maUv7VPeYre_DojAE',
    'CAACAgIAAxkBAAEKbP1lGQFPaS-H4xR7SJGEKS4esZ0URQACtB8AAopzcEt4PSZViagUkTAE',
    'CAACAgIAAxkBAAEKbQFlGQFcx2KVi3zJ1S3HBRqTFb85VAAC4BwAAnbQcUvyswPrqKIEgzAE',
    'CAACAgIAAxkBAAEKbQNlGQFmfbfOEpQ4meS379GH7hshYAACVSUAAm-5aUtRH58998eFxDAE',
    'CAACAgIAAxkBAAEKV75lCrtXUSpPCm8fz_eWEOh3jfSgPQAC8SoAAhS96EorE2GPCSFbODAE',
    'CAACAgIAAxkBAAEKV8BlCrtrUeHWrMuK6BNUpMa5lur6HAACZxUAAoKxyUstXbxOsyjFNDAE',
    'CAACAgQAAxkBAAEKV8JlCruJtXOR9WWvLTwXPey0pPW3dgACcQ4AAl4JwVLjLumufink5jAE',
    'CAACAgIAAxkBAAEKbQVlGQI9GBn1XOAgOALInaXIfUq3nwACCCQAAkY56EhxNTUovMYg7TAE',
    'CAACAgIAAxkBAAEKbQdlGQKCsNmbEwu8cEYQhEs5sOaq9gAClBsAAilm-UpkFa-oJK8OfjAE',
    'CAACAgIAAxkBAAEKbQllGQKIg15oWhfe7PPqxwHgS8v9EAACJiEAAlVi-EoJD4yYNUESaDAE',
    'CAACAgIAAxkBAAEKbQtlGQKOhZnsRYKe3gT5gZhEQoFOjAACmSQAAu_62Ek5zY4ospbwfDAE',
    'CAACAgIAAxkBAAEKbRJlGQLazhKxNasJBpL97SAuL7mlOwAC2SoAAi1oOEmp-_RdN5KAdDAE',
    'CAACAgIAAxkBAAEKbRRlGQLe26-Jt56b5H6X4i9MCW7xFQACTh4AAilGQEkT47aeWhWwhTAE',
    'CAACAgIAAxkBAAEKbRZlGQLjAAHUxE-EmuiK4vHbKlISfAUAArMlAAKZK0BJMfs5sfFpngMwBA',
    'CAACAgIAAxkBAAEKbRhlGQMBBbREgdcUkIOquoGfONOSEgACTBkAAl11-Ujbhgg6l6SFnjAE',
    'CAACAgIAAxkBAAEKbRplGQMDc1UEbGRMQSIDdOa3axyxxwACEBkAAo3Z8EhPY8U6lajVLTAE',
    'CAACAgIAAxkBAAEKbRxlGQMNwTi3ECoBu7uCsc56gWi-2AACWhUAAgju-EikZH3HWeXOAAEwBA',
    'CAACAgIAAxkBAAEKbR5lGQMRZMvYr_Z2FHyvi3GuE6d6JwACORoAApzl8EgmVQFgFQJkIzAE',
    'CAACAgIAAxkBAAEKbSBlGQMdiiyImwqd4PbXCPaHd1ql8QAC3CcAAjfcEEl2Pzw5-uhoGDAE',  # колбаса
    'CAACAgIAAxkBAAEKbSJlGQMjSMTEX2SWB4FSVg9S_Ei7FQACqwADP20WIIg1JHvA0ofSMAQ',  # бургер
    'CAACAgIAAxkBAAEKbSRlGQMtQA0PUd3-vAoShHgrbwLprQACIrQAAmOLRgwwf-4oA4n_LzAE',  # сосиски
    'CAACAgIAAxkBAAEKbSZlGQNnx4uDUL6WxVIhF1B4gTyZyAACax0AAoygUUp0d_jHXbyzNzAE',
    'CAACAgIAAxkBAAEKbShlGQN2Zl9N-jjPP08yOThY07cqfwACcQEAAntOKhBCopR29izOTzAE',
    'CAACAgIAAxkBAAEKbSplGQN-FMaQKFLTL-rO2EB3n7A2CQACGC0AAun_YEoO4BNZq4FnszAE',
    'CAACAgIAAxkBAAEKbSxlGQODo-HMEoH6RdAU_q5g_bJ_KAACJysAAvlL6Urt8ZuDpuZoZDAE',
    'CAACAgIAAxkBAAEKbS5lGQOFbS-webxUmUt5jBoP0BcnKwACKyUAAiDfQUozb3ejrLUliDAE',
    'CAACAgIAAxkBAAEKbTBlGQPRzWQHdRRrG5ppXeSuX6J25wACYS0AArQs6EobusaY0XFzljAE',
    'CAACAgIAAxkBAAEKbTJlGQPW_Zk7BgjZH_fvXpqewRCj2wAC8SoAAhS96EorE2GPCSFbODAE'
]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Чем помочь сэр?")


@bot.message_handler(commands=['sticker'])
def stick(message):
    stick3 = random.choice(random_sticker_list)
    bot.send_sticker(message.chat.id, stick3)


@bot.message_handler(commands=['add'])
def add_words(message):
    # Получаем текст команды
    user_text = message.text[len('/add '):]

    if user_text:
        # Открываем файл и добавляем текст с использованием UTF-8 кодировки
        with open('new_words.txt', 'a', encoding='utf-8') as file:
            file.write(user_text + ',')
        bot.reply_to(message, f'Добавлено: {user_text}')
    else:
        bot.reply_to(message, 'Пожалуйста, укажите текст после команды /add')


# Файл для хранения плохих слов
BAD_WORDS_FILE = 'bad_words.txt'


# Функция для загрузки плохих слов из файла
def load_bad_words():
    if not os.path.exists(BAD_WORDS_FILE):
        return set()
    with open(BAD_WORDS_FILE, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        if not content:
            return set()
        return set(word.strip().lower() for word in content.split(','))


# Функция для сохранения плохих слов в файл через запятую
def save_bad_words(bad_words):
    with open(BAD_WORDS_FILE, 'w', encoding='utf-8') as file:
        file.write(','.join(bad_words))


# Загрузка плохих слов в память
bad_words = load_bad_words()


@bot.message_handler(commands=['bad'])
def add_bad_word(message):
    new_word = message.text[len('/bad '):].strip().lower()
    if not new_word:
        bot.reply_to(message, "Используйте команду /bad <слово или фраза>")
        return
    if new_word in bad_words:
        bot.reply_to(message, "Это слово уже в списке плохих слов.")
    else:
        bad_words.add(new_word)
        save_bad_words(bad_words)
        bot.reply_to(message, f"Слово или фраза '{new_word}' добавлено в список плохих слов.")


@bot.message_handler(commands=['getbadwords'])
def get_bad_words(message):
    if not bad_words:
        bot.reply_to(message, "Список плохих слов пуст.")
    else:
        bad_words_list2 = ', '.join(bad_words)
        bot.reply_to(message, f"Список плохих слов: {bad_words_list2}")


@bot.message_handler()
def msg(message):
    fox_id = 5544158479

    mess = message.text.lower()

    # functions

    def sendMessage(txt: str):
        bot.send_message(message.chat.id, txt)

    def sendSticker(sticker: str):
        bot.send_sticker(message.chat.id, sticker)

    def congratulate():
        bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEIzxpkT99D0SoRfbLUtMN62dfub0siVQACCAADJQIYFKHIFj2hN9VwLwQ")
        sendMessage(
            f"С днем рождения тебя! С днем рождения тебяя! С днем рождения, с днем рождения @atom_prod !!!!!!!!!!! \n Ураааа!!!!")
        sendMessage("А вот и торт!!!!")
        bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEIzxxkT99Iy17Jy7XrNYTGP3H1SrBBngACBAADJQIYFPM0mGz681pHLwQ")
        audio = open(r"D:/CanDeleteAnyTime/PycharmProjects/JarvisCloneBotTg/song.mp3", 'rb')
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, audio)
        audio.close()

    def dance():
        stick = random.choice(dance_stickers_list)
        stick2 = random.choice(dance_stickers_list)
        stick3 = random.choice(dance_stickers_list)
        sendSticker(stick)
        sendSticker(stick2)
        sendSticker(stick3)
        sendMessage("Дупас стак стак аыаыафафыафа Урааа!!!")
        audio = open(r"D:/CanDeleteAnyTime/PycharmProjects/JarvisCloneBotTg/song2.mp3", 'rb')
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, audio)
        audio.close()

    def fire_out(message):
        if message.reply_to_message:
            chat_id = message.chat.id
            # user_id = message.reply_to_message.from_user.id
            user2 = message.reply_to_message.from_user.username
            bot.send_message(chat_id=chat_id, text=f'@{user2} ты уволен😈!!!',
                             reply_to_message_id=message.reply_to_message.message_id)

    def come_back(message):
        if message.reply_to_message:
            chat_id = message.chat.id
            # user_id = message.reply_to_message.from_user.id
            user2 = message.reply_to_message.from_user.username
            bot.send_message(chat_id=chat_id, text=f'@{user2} ты возвращён обратно!!!😏',
                             reply_to_message_id=message.reply_to_message.message_id)

    def muteUser(message):
        if message.reply_to_message:
            chat_id = message.chat.id
            user_id = message.reply_to_message.from_user.id
            user_status = bot.get_chat_member(chat_id, user_id).status
            if user_status == 'administrator' or user_status == 'creator':
                bot.reply_to(message, "Невозможно замутить администратора.")
            else:
                duration = 60  # Значение по умолчанию - 1 минута
                args = message.text.split()[1:]
                if args:
                    try:
                        duration = int(args[0])
                    except ValueError:
                        bot.reply_to(message, "Неправильный формат времени.")
                        return
                    if duration < 1:
                        bot.reply_to(message, "Время должно быть положительным числом.")
                        return
                    if duration > 1440:
                        bot.reply_to(message, "Максимальное время - 1 день.")
                        return
                bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + duration * 60)
                bot.reply_to(message,
                             f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
        else:
            bot.reply_to(message,
                         "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")

    def unmute(message):
        if message.reply_to_message:
            chat_id = message.chat.id
            user_id = message.reply_to_message.from_user.id
            bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True,
                                     can_send_other_messages=True, can_add_web_page_previews=True)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размучен.")
        else:
            bot.reply_to(message,
                         "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")

    def makeHappy(username):
        sendSticker("CAACAgIAAxkBAAEKbThlGQZmc1WyYIcGpNAQ_jw0RtzhGgAC8QIAApBZdi0kD_ALmg0shzAE")
        bot.send_message(message.chat.id, f"@{username} улыбнись!")

    def sendMessToGroup(message):
        bot.send_message(-1002032812787, message.text)
        bot.send_message(message.chat.id, "Отправлено")

    def sendMessToFox(message_m):
        bot.send_message(fox_id, message_m.text)
        bot.send_message(message.chat.id, "Отправлено")

    def makeDr(message_m):
        mss = message_m.text.lower()
        if mss == "да" or mss == "дэ" or mss in happy_evening_text_list and message.chat.id == fox_id:
            congratulate()
            dance()
            makeHappy(message_m.chat.username)

    # Проверка
    for word in bad_words:
        if word in mess:
            bot.delete_message(message.chat.id, message.message_id)
            # bot.send_message(message.chat.id, "📛Найдено плохое слово(мат), так нельзя!")
            break
    if mess == "жарвис" or mess == "jarvis":
        bot.send_message(chat_id=message.chat.id, text="Да, сэр?", reply_to_message_id=message.message_id)
    elif mess == "пон" or mess == "понятно":
        bot.send_animation(message.chat.id,
                           "CgACAgIAAx0EeSpC8wACMFVmZdy_roElEbkYZN14toNxrFj4UQACpEwAA6oxS5xHvCQmPWOZNQQ",
                           reply_to_message_id=message.message_id)
        # animation_path = 'D:/CanDeleteAnyTime/PycharmProjects/JarvisCloneBotTg/pon_gif.MP4'
        # with open(animation_path, 'rb') as animation_file:
        #     msg = bot.send_animation(message.chat.id, animation_file)
        #     # Сохраняем file_id
        #     file_id = msg.animation.file_id
        #     print(f"file_id: {file_id}")
        # bot.send_message(chat_id=message.chat.id, text="Лютый пон", reply_to_message_id=message.message_id)
    # elif mess in bad_words_list:
    #    sendMessage("📛Найдено плохое слово(мат), так нельзя!")
    #    bot.delete_message(message.chat.id, message.message_id)
    elif mess in happy_evening_text_list:
        bot.send_message(chat_id=message.chat.id, text="Выполняю сэр...", reply_to_message_id=message.message_id)
        congratulate()
    elif mess in osk_text_list:
        bot.send_message(chat_id=message.chat.id, text="Сам иди!", reply_to_message_id=message.message_id)
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=time.time() * 60)
        try:
            print(message.chat.id)
            user_to_ban = message.from_user.id
            bot.kick_chat_member(message.chat.id, user_to_ban)
            bot.reply_to(message, "Пользователь забанен.")
        except:
            sendMessage("Не получилось забанить админа!")
    elif mess in dance_text_list:
        bot.send_message(chat_id=message.chat.id, text="Выполняю сэр...", reply_to_message_id=message.message_id)
        dance()
    elif mess == "data":
        sendMessage(f'{message}')
    elif mess in praise_words_lis:
        if message.reply_to_message:
            txt = random.choice(['Спасибо😊', 'Благодарю сэр...'])
            bot.send_message(chat_id=message.chat.id, text=txt, reply_to_message_id=message.message_id)
    elif mess in hello_text_list and message.chat.id == fox_id:
        word = "Приветсвую сэр!"
        bot.send_message(chat_id=message.chat.id, text=word.capitalize(), reply_to_message_id=message.message_id)
        random_hello_sticker = random.choice(hello_sticker_list)
        sendSticker(random_hello_sticker)
        sendMessage("Активировать протокол весёлый вечер?")
        bot.register_next_step_handler(message, makeDr)
    elif mess in hello_text_list:
        word = random.choice(hello_answer_text_list)
        bot.send_message(chat_id=message.chat.id, text=word.capitalize(), reply_to_message_id=message.message_id)
        random_hello_sticker = random.choice(hello_sticker_list)
        sendSticker(random_hello_sticker)
    elif mess == "пук пук":
        sendMessage(
            "💨Пёрнуто 1000 тыс тонн тратила в лицо всем участникам группы")
    elif mess == "стик":
        stick = random.choice(random_sticker_list)
        bot.send_sticker(message.chat.id, stick)
    elif mess == "бот":
        sendMessage("На месте✅")
    elif mess == "пин":
        sendMessage("Понг")
    elif mess in rest_text_list:
        sendMessage("Хорошо сэр🫡")
        sendMessage("Я отключаюсь")
    elif mess == "уволить":
        fire_out(message)
    elif mess == "вернуть" or mess == "вернуть обратно":
        come_back(message)
    elif mess == "мут":
        muteUser(message)
    elif mess == "размут":
        unmute(message)
    elif mess == "обрадовать":
        if message.reply_to_message:
            makeHappy(message.reply_to_message.from_user.username)
    elif mess == "созвать всех":
        bot.send_message(chat_id=message.chat.id,
                         text="взываю всех",
                         reply_to_message_id=message.message_id)
        sendMessage("Всех на базу!")
    elif mess == "data":
        sendMessage(message)
    elif mess == "аы":
        markup = types.ReplyKeyboardMarkup()
        youtube = types.KeyboardButton('Отправить сообщение в группу')
        markup.add(youtube)
        bot.send_message(message.chat.id, "Меню:", reply_markup=markup)
    elif mess == "отправить сообщение в группу":
        sendMessage("Твоё сообщение:")
        bot.register_next_step_handler(message, sendMessToGroup)
    elif mess == "спасибо" or "спс" and message.chat.id == fox_id:
        sendMessage("Не за что сэр! Обращяйтесь...")
    elif mess == "смс" and message.chat.id == 1342503849:
        markup = types.ReplyKeyboardMarkup()
        youtube = types.KeyboardButton('Отправить сообщение в кому-то')
        markup.add(youtube)
        bot.send_message(message.chat.id, "Меню:", reply_markup=markup)
    elif mess == "отправить сообщение в кому-то":
        sendMessage("Твоё сообщение:")
        bot.register_next_step_handler(message, sendMessToFox)


bot.polling(none_stop=True)
