import telebot
import cfg
import random
import os
from telebot import types

#tgbot by DrSobeck

bot = telebot.TeleBot(cfg.TOKEN)

def read_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        data = f.read().split('\n')
    return data

fact = read_file('fact.txt')
cit = read_file('cit.txt')
zia = read_file('zia.txt')

@bot.message_handler(commands=["start"])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Цитата")
    item3 = types.KeyboardButton("Сарказм")
    item4 = types.KeyboardButton("Музыка")
    markup.add(item1, item2, item3, item4)
    bot.send_message(m.chat.id, 'Выберите опцию:', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт':
        answer = random.choice(fact)
    elif message.text.strip() == 'Цитата':
        answer = random.choice(cit)
    elif message.text.strip() == 'Сарказм':
        answer = random.choice(zia)
    elif message.text.strip() == 'Музыка':
        send_random_music(message.chat.id, r'D:\Programing\Project\PyBotTg\mus')
        return
    else:
        answer = "Я не понимаю ваш запрос."

    bot.send_message(message.chat.id, answer)

def send_random_music(chat_id, music_dir):
    music_list = os.listdir(music_dir)
    random_music = random.choice(music_list)
    with open(os.path.join(music_dir, random_music), 'rb') as music_file:
        bot.send_audio(chat_id, music_file)



if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)