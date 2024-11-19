from telebot import TeleBot, types
#from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot.types import ReactionTypeEmoji
import random
import Text
import calldat
import Calcbtn
import Video
import funcs
import test
import Nat
import lugat
import Tilbtn
import kvuz
import func
import admin
import time
import wikipedia
wikipedia.set_lang("uz")
channel = ""#@channelusername
admin_id = "" #group id
master_id = #admin id
text = ""
audio = {}
bot = TeleBot("<bot_token>")
@bot.message_handler(content_types=["sticker"])
def getstick(m):
    bot.send_message(m.chat.id, m.sticker.file_id)
@bot.message_handler(content_types=['audio'])
def au(m):
    bot.send_message(m.chat.id, m.audio.file_id)
    bot.send_audio(m.chat.id, m.audio.file_id)
@bot.message_handler(commands=['admin'])
def admin1(m):
        if m.from_user.id == master_id:
        admin.adduser(m.from_user.id)
        bot.send_message(m.chat.id, "Kimga xabar yubormoqchisiz? ID:")
        bot.register_next_step_handler(m, id)
@bot.message_handler(commands=['weather'])
def command_weather(message):
    markup = types.ForceReply(selective=True)
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E", "👍"]  # or use ["🔥", "🤗", "😎"]
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)
    bot.send_message(message.chat.id, "answers.weatherRequestShort", reply_markup=markup)
@bot.message_handler(content_types=['voice'])
def audio1(m):
    
