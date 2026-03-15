import telebot

from bot_logic import gen_pass, gen_emodji, flip_coin, get_class  # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8689148746:AAELRkQvUOkSxxykvmfpob_FBLW33cfhf58")

@bot.message_handler(content_types=['photo'])
def photo (message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result=get_class(image_path=file_name)

    bot.send_message(message.chat.id, result)
# Запускаем бота
bot.polling()