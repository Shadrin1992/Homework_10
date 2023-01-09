import telebot
import requests
from cnfg import TOKEN

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

def extract_arg(arg):
    return arg.split()[1:]

bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Чтобы узнать курс валюты введите \currency код валюты. Например: \currency AUD")

@bot.message_handler(commands=['currency'])
def send_currency(message):
    key = extract_arg(message.text)
    result = " ".join((map(str, (res['Valute'][key[0]]['Name'], res['Valute'][key[0]]['Value']))))
    bot.send_message(message.chat.id, f'{result}')
    print(result)
bot.infinity_polling()
