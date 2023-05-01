import telebot

bot = telebot.TeleBot('6217254132:AAEdGaOyvaQMTLqffnGtUheeWpejnqgUmNs')
print("bot started")

user = bot.get_me()
idi = user.id


@bot.message_handler()
def msg(message):
    def sendMessage(txt: str):
        bot.send_message(message.chat.id, txt)

    def congrutilate():
        bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEIzxpkT99D0SoRfbLUtMN62dfub0siVQACCAADJQIYFKHIFj2hN9VwLwQ")
        sendMessage("С днем рождения тебя! С днем рождения тебяя! С днем рождения, с днем рождения @BLACK_F0XXXX !!!!!!!!!!! \n Ураааа!!!!")
        sendMessage("А вот и торт!!!!")
        bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEIzxxkT99Iy17Jy7XrNYTGP3H1SrBBngACBAADJQIYFPM0mGz681pHLwQ")
        audio = open(r'C:/Users/Diyorbek/PycharmProjects/JarvisCloneBotTg/song.mp3', 'rb')
        bot.send_chat_action(message.chat.id,"upload_audio")
        bot.send_audio(message.chat.id,audio)
        audio.close()

    if message.text == 'Jarvis запусти протокол веселый вечер':
        sendMessage("Выполняю сэр...")
        congrutilate()
    elif message.text == "Жарвис заупусти протокол веселый вечер":
        sendMessage("Выполняю сэр...")
        congrutilate()
    else:
        bot.send_message(message.chat.id, "Не пон!")


bot.polling(none_stop=True)
