import telebot
import requests
import json

bot = telebot.TeleBot('7093337586:AAFvNFOKuRAtpBiwiFPneDIEc4nYD5qnIZ8')
API = 'f848ea6ef59ea770c725824305f12cf7'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введи название своего города: ')
    
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'sunny.png' if temp > 28.0 else 'sun.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан не верно')
        
bot.infinity_polling()