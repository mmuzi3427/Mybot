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
    bot.send_message(m.chat.id, m.voice.file_id)
def id(m):
    admin.getid(m.from_user.id, m.text)
    bot.send_message(m.chat.id, "Yuboriladigan xabarni kiriting!")
    bot.register_next_step_handler(m, getme)
def getme(m):
    admin.getext(m.from_user.id, m.text)
    try:
        bot.send_message(int(admin.id(m.from_user.id)), str(admin.text(m.from_user.id)), reply_markup=Calcbtn.tushundim())
        bot.send_message(m.chat.id, "Xabarni yubordim ✅", reply_markup= Text.btn())
    except:
        bot.send_message(m.chat.id, "Xabar yuborilmadi?", reply_markup= Text.btn())
@bot.message_handler(content_types=['video'])
def video(m):
    bot.send_message(m.chat.id, m.video.file_id)
@bot.message_handler(content_types=['photo'])
def photo(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_message(m.chat.id, m.photo[0].file_id)
@bot.message_handler(commands=['search', 'wiki', 'поиск'])
def search(m):
    if m.from_user.language_code == "uz":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "🔎", reply_markup=kvuz.kv())
    elif m.from_user.language_code == "ru":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "🔎")
        bot.send_message(m.chat.id, "Введите условия поиска!")
        bot.register_next_step_handler(m, get_search)
@bot.message_handler(commands=['start'], func=lambda message:True)
def start(m: types.Message):
    b = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "uz":
        if b != "left":
            if test.getb(m.from_user.id) == "1":
                bot.set_message_reaction(m.chat.id, m.id, [ReactionTypeEmoji("👍")])
                bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAIpyGciXQnyHUs-gjvizk1KKNZO9Yy9AAJFAQACzRswCCofUpmKTO9lNgQ")
                time.sleep(5)
                bot.delete_message(m.chat.id, m.message_id+1)
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, f"<i>Assalomu Alaykum!</i>\n<u><b>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}!</b>\n\n<i>Bugun nimani oʻrganishni xohlaysiz! ✅</i></u> ", reply_markup=Calcbtn.k1(), parse_mode='html', protect_content=True)
                bot.pin_chat_message(m.chat.id, m.message_id+2)
                bot.delete_message(m.chat.id, m.message_id+3)
            else:
                Nat.adduser(m.from_user.id)
                funcs.adduser(m.from_user.id)
                bot.set_message_reaction(m.chat.id, m.id, [ReactionTypeEmoji("🔥")])
                bot.send_message(m.chat.id, "⌛")
                time.sleep(4)
                bot.delete_message(m.chat.id, m.message_id+1)
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, f"Assalomu Alaykum {m.from_user.first_name}\n\nmen MATEMATIKA FANIDAN TESTLAR kanalining rasmiy botiman!", reply_markup=Calcbtn.k2())
                bot.send_message(admin_id, f"Botga {m.from_user.first_name} /start buyrugʻini yubordi.\n\nIsmi:  {m.from_user.first_name}\n\nUsername:  @{m.from_user.username}\n\nID:  {m.from_user.id}")
        else:
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=Calcbtn.obuna())
    elif m.from_user.language_code == "ru":
        funcs.adduser(m.from_user.id)
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, f"Привет {m.from_user.first_name}\n\nЯ официальный бот канала MATEMATIKADAN TESTLAR!", reply_markup=Tilbtn.ru())
    else:
        bot.send_message(m.chat.id, "⌛")
@bot.message_handler(content_types=['text'])
def get_text(m):
    channeltest = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "uz":
        if channeltest != "left":
            if m.text == 'Kalkulyator':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Kalkulyatorga xush kelibsiz!\nIltimos sonni kiriting", reply_markup=Calcbtn.calcb())
                bot.set_message_reaction(m.chat.id, m.id+1, [ReactionTypeEmoji("⚡")])
                funcs.toza(m.from_user.id)
            elif m.text == "Chiqish ↩️ va tugatish ✔️":
                try:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.delete_message(m.chat.id, m.message_id - 1)
                    bot.send_message(m.chat.id, f"{Nat.natol(m.from_user.id)}", reply_markup=Nat.yangi())
                    bot.send_message(m.chat.id, f"Jami savollar soni: 10 ta\n✅ Toʻgʻri javoblar soni: {Nat.h(m.from_user.id)} ta", reply_markup=Calcbtn.uzat(f"{m.from_user.first_name}"))
                    bot.pin_chat_message(m.chat.id, m.message_id+2)
                    Nat.delete(m.from_user.id)
                except:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_message(m.chat.id, Nat.natol(m.from_user.id), reply_markup=Nat.yangi())
            elif m.text == "📼 Video darslar":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Oʻzingizga kerakli boʻlimni tanlang!" , reply_markup=Video.menu())
            elif m.text == "⚙ Sozlamalar":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup=Calcbtn.edit())
            elif m.text == "Asosiy sahifa ♻️":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Asosiy sahifaga qaytdik!", reply_markup=Calcbtn.mdel())
                bot.send_photo(m.chat.id, "AgACAgIAAxkBAAICkmbYMj7HBh2xM2OS3wABIcEM19RSZgACKNsxG73HwUqoJ16vtcQvmAEAAwIAA3MAAzYE", f"<i><b>Salom! <u>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}</u></b>\n\nTayyor boʻlsangiz quyidagi tugmani bosing!👇</i>", reply_markup=Calcbtn.test12(), parse_mode="html")
            elif m.text == "Ma'umotlar toʻgʻri 100%":
                test.editb(m.from_user.id, 1)
                bot.delete_message(m.chat.id, m.message_id)
                bot.delete_message(m.chat.id, m.message_id - 1)
                bot.send_photo(m.chat.id, "AgACAgIAAxkBAAICkmbYMj7HBh2xM2OS3wABIcEM19RSZgACKNsxG73HwUqoJ16vtcQvmAEAAwIAA3MAAzYE", "Tayyor boʻlsngiz qiyidagi tugmani bosing! 👇", reply_markup=Calcbtn.test12())
            elif m.text == "📊 Testda qatnashish":
                f = test.getb(m.from_user.id)
                if f == "1":
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_photo(m.chat.id, "AgACAgIAAxkBAAICkmbYMj7HBh2xM2OS3wABIcEM19RSZgACKNsxG73HwUqoJ16vtcQvmAEAAwIAA3MAAzYE", f"<b><i>Salom!</i> <u>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}</u></b> \n\n<i>Tayyor boʻlsangiz quyidagi tugmani bosing!👇</i>", reply_markup=Calcbtn.test12(), parse_mode="html")
                else:
                    test.adduser(m.from_user.id)
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_message(m.chat.id, "👋")
                    bot.send_message(m.chat.id, "👋\nKeling testni boshlashdan oldin siz bilan tanishib olamiz! ✅")
                    bot.send_message(m.chat.id, "Iltimos ismingizni kiriting!", reply_markup=Calcbtn.mdel())
                    bot.register_next_step_handler(m, get_name)
            elif m.text == 'Tasodifiy raqam':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Tasodifiy raqam tanlandi : " + str(random.randint(1, 100)) + " ✅", reply_markup=Calcbtn.delete())
                bot.set_message_reaction(m.chat.id, m.id+1, [ReactionTypeEmoji("🦄")])
            else:
                bot.set_message_reaction(m.chat.id, m.id, [ReactionTypeEmoji("👎")])
                bot.send_message(m.chat.id, "❌ Noma'lum buyruq!\n\nSiz to'g'ridan-to'g'ri bot chatiga xabar yubordingiz, yoki\nbot tuzilishi yaratuvchisi tomonidan o'zgartirilgan boʻlishi mumkin.\n\nℹ️ Xabarlarni to'g'ridan-to'g'ri botga yubormang yoki\n/start orqali bot menyusini yangilang", reply_markup=Calcbtn.mdel())
                bot.set_message_reaction(m.chat.id, m.id+1, [ReactionTypeEmoji("🔥")])
        else:
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=Calcbtn.obuna())
    elif m.from_user.language_code == "ru":
        if m.text == "Калькулятор":
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Добро пожаловать в калькулятор!\nПожалуйста, введите номер", reply_markup=Calcbtn.calcb())
        elif m.text == "Случайное число":
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, f"Было выбрано случайное число: {str(random.randint(1, 100))} ✅", reply_markup=Tilbtn.rudel())
        else:
            bot.send_message(m.chat.id, "❌ Неизвестная команда!\n\nВы отправили сообщение прямо в чат бота, или\nСтруктура бота могла быть изменена создателем.\n\nℹ️ Не отправляйте сообщения напрямую боту или\nОбновите меню бота через /start", reply_markup=Calcbtn.mdel())
def get_search(m):
    if m.from_user.language_code == "ru":
        try:
            bot.delete_message(m.chat.id, m.message_id)
            bot.delete_message(m.chat.id, m.message_id - 1)
            bot.delete_message(m.chat.id, m.message_id - 2)
            wikipedia.set_lang('ru')
            bot.send_message(m.chat.id, wikipedia.summary(m.text), reply_markup=Tilbtn.rudel())
        except:
            bot.send_message(m.chat.id, "У меня нет информации,\nкоторый вы ищете!", reply_markup=Tilbtn.tu())
@bot.callback_query_handler(func=lambda call: True)

