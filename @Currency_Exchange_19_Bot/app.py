import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду в следующем формате:\n"Имя валюты цену которой хотите узнать"  \
"Имя валюты в которой надо узнать цену первой валюты"  \
"Количество первой валюты"\nНапример: евро рубль 1500 \nЧтобы увидеть список всех доступных для запроса валют, нажмите или введите: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные для конвертации валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Вы ввели неверное количество параметров, введите данные в формате: евро рубль 1500')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'За {amount} {quote} Вы получите: {total_base} {base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
