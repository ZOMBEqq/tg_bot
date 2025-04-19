import telebot
from telebot.types import Message
import random
from bot_logic import gen_pass, gen_emodji, flip_coin

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Команды: /hello, /bye, /pass, /emodji /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! (не хейт)")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Поки")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['knb'])
def knb_cmd(message: Message):
    bot.send_message(message.chat.id, "Игра запустилась, напишите камень/ножницы/бумага или отмена (чтобы остановить игру)")
    bot.register_next_step_handler(message, knb_game)

def knb_game(message: Message):
    text = message.text.lower()
    if text == 'отмена':
        bot.send_message(message.chat.id, "Игры остановлен, вам сново доступны все команды")
        return
    if text not in ['камень', 'ножницы', 'бумага']:
        bot.send.message(message.chat.id, "Вы написали что то не то, вам снова доступны все команды")
        return
    comp = random.choice(['камень', 'ножницы', 'бумага'])
    if text == comp:
        bot.send_message(message.chat.id, "Ничья, если хотите поиграть снова, напишите /knb" )
        return
    elif (text == 'камень' and bot == 'ножницы') or (text == 'ножницы' and bot == 'бумага') or (text == 'бумага' and bot == 'камень'):
        bot.send_message(message.chat.id, "Вы победили, если хотите поиграть снова, напишите /knb")
        return
    else:
        bot.send_message(message.chat.id, "Вы проиграли, если хотите поиграть снова, напишите /knb")
        return
    















bot.infinity_polling()