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
def call(call):
    def wiki(m):
        try:
            funcs.addwiki(call.from_user.id, m)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"🔎\n\n{funcs.getmatn(call.from_user.id)}|", reply_markup=kvuz.kv1())
        except:
            bot.answer_callback_query(callback_query_id=call.id, text="❌ Xatolik\nJuda koʻp tugmani bosib yubordingiz!", show_alert=True)
    def delta(natija):
        Nat.nat(call.from_user.id, natija)
    def n():
        Nat.true(call.from_user.id)
    def vid(v):
        bot.send_video(call.message.chat.id, v)
    def editing(b):
        func.getson(call.message.chat.id, b)
        nat = func.hisobla(call.from_user.id)
        if nat == None:
            bot.answer_callback_query(call.id, "Xatolik yuz berdi", show_alert=True)
            func.clear(call.from_user.id)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=func.retson(call.from_user.id) + "\n                             Natija : " + nat + "\n....@Matematikauniversalbot....", reply_markup=Calcbtn.calcb())
    def editing1(b):
        try:
            func.getamal(call.message.chat.id, b)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=func.retson(call.from_user.id) + "\n....@Matematikauniversalbot....", reply_markup= Calcbtn.calcb())
        except:
            bot.answer_callback_query(call.id, "Xatolik yuz berdi!\nAC tugmasini bosing!", show_alert=True)
    def editing2(b):
        try:
            func.getfloot(call.message.chat.id, b)
            nat = func.hisobla(call.from_user.id)
            if nat == None:
                bot.answer_callback_query(call.id, "Xatolik yuz berdi", show_alert=True)
                func.clear(call.from_user.id)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=func.retson(call.from_user.id) + "\n                             Natija : " + nat + "\n....@Matematikauniversalbot....", reply_markup= Calcbtn.calcb())
        except:
            bot.answer_callback_query(call.id, "Xatolik yuz berdi⚠️\n Bu yerga nuqta qoʻyolmasysiz! Matematik xato?", show_alert=True)
    test = bot.get_chat_member(channel, call.from_user.id).status
    if call.from_user.language_code == "uz":
        if test != "left":
            if call.data == "obuna":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, f"Assalomu Alaykum {call.from_user.first_name}\n\nmen MATEMATIKA FANIDAN TESTLAR kanalining rasmiy botiman ", reply_markup=Calcbtn.k1())
            elif call.data == "fam":
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_message(call.message.chat.id, "Familiyangizni kiriting!")
                    bot.register_next_step_handler(call.message, get2)
                except:
                    bot.send_message(call.message.chat.id, "Familiyangizni kiriting!")
                    bot.register_next_step_handler(call.message, get2)
            elif call.data == "ism":
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_message(call.message.chat.id, "Ismingizni qayta kiriting!", reply_markup=False)
                    bot.register_next_step_handler(call.message, get1)
                except:
                    bot.send_message(call.message.chat.id, "Ismingizni qayta kiriting!", reply_markup=False)
                    bot.register_next_step_handler(call.message, get1)
            elif call.data == "eyosh":
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_message(call.message.chat.id, "Yoshingizni qayta kiriting!")
                    bot.register_next_step_handler(call.message, get3)
                except:
                    bot.send_message(call.message.chat.id, "Yoshingizni qayta kiriting!")
                    bot.register_next_step_handler(call.message, get3)
            elif call.data == "enter":
                try:
                    d = wikipedia.search(funcs.getmatn(call.from_user.id))
                    m = ""
                    n1 = 0
                    for l in d:
                        r = n1 + 1
                        n1 = n1 + 1
                        m += f"{r}) {l}\n\n"
                    bot.send_message(call.message.chat.id, wikipedia.summary(funcs.getmatn(call.from_user.id)), reply_markup=Calcbtn.delete(), parse_mode="html")
                    bot.send_message(call.message.chat.id, f"Balki xato qilgandirsiz!!! 👇\n\n{m}", reply_markup=kvuz.kv())
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    funcs.del1(call.from_user.id)
                except:
                    try:
                        bot.send_message(call.message.chat.id, lugat.pydev[(funcs.getmatn(call.from_user.id).lower())], reply_markup=kvuz.kv())
                        funcs.del1(call.from_user.id)
                        bot.delete_message(call.message.chat.id, call.message.message_id)
                    except:
                        bot.answer_callback_query(callback_query_id=call.id, text="❌ Topa olmadim! ✏️", show_alert=True)
                        funcs.del1(call.from_user.id)
            elif call.data == "33_dars":
                vid("BAACAgIAAxkBAAISKmb5RQbzic_SGElAlYCpo1GNuFRGAAIFKQACbAsoSsos7677_ejbNgQ")
            elif call.data == "del":
                try:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔎\n\n|", reply_markup=kvuz.kv())
                    funcs.del1(call.from_user.id)
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="Allaqachon tozalangan! ✅", show_alert=True)
            elif call.data == "toza":
                try:
                    funcs.toza(call.from_user.id)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Kalkulyator tarixi tozalandi hisoblashda davom etishingiz mumkin!...", reply_markup=Calcbtn.calcb())
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="Juda koʻp urunishlar ❌\nMa'lumotlar tozalangan!\nRaqamlar ustiga bosib hisoblashda davom etishingiz mumkin. Hammasi 0 dan boshlanadi✅", show_alert=True)
            elif call.data == "deletec":
                try:
                    func.remove1(call.from_user.id)
                    nat = func.hisobla(call.from_user.id)
#                    bot.send_message(call.message.chat.id, str(func.retson(call.message.chat.id)))
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=func.retson(call.from_user.id) + "\n                              Natija : " + nat + "\n....@Matematikauniversalbot....", reply_markup=Calcbtn.calcb())
                except:
                    bot.answer_callback_query(call.id, "Xatolik yuz berdi", show_alert=True)
            elif call.data == "a":
                wiki("a")
            elif call.data == "q":
                wiki("q")
            elif call.data =="w":
                wiki("w")
            elif call.data =="e":
                wiki("e")
            elif call.data =="r":
                wiki("r")
            elif call.data =="t":
                wiki("t")
            elif call.data =="y":
                wiki("y")
            elif call.data =="u":
                wiki("u")
            elif call.data =="i":
                 wiki("i")
            elif call.data =="o":
                wiki("o")
            elif call.data =="p":
                wiki("p")
            elif call.data =="o1":
                wiki("oʻ")
            elif call.data =="s":
                wiki("s")
            elif call.data =="d":
                wiki("d")
            elif call.data =="f":
                wiki("f")
            elif call.data =="g":
                wiki("g")
            elif call.data == "h":
                wiki("h")
            elif call.data =="j":
                wiki("j")
            elif call.data =="k":
                wiki("k")
            elif call.data =="l":
                wiki("l")
            elif call.data =="g1":
                wiki("gʻ")
            elif call.data =="tutuq":
                wiki("ʼ")
            elif call.data =="z":
                wiki("z")
            elif call.data =="x":
                wiki("x")
            elif call.data =="c":
                wiki("c")
            elif call.data =="v":
                wiki("v")
            elif call.data =="b":
                wiki("b")
            elif call.data =="n":
                wiki("n")
            elif call.data =="m":
                wiki("m")
            elif call.data ==",":
                wiki(",")
            elif call.data =="pro":
                wiki(" ")
            elif call.data ==".":
                funcs.addwiki(call.from_user.id, ". ")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"🔎\n\n{funcs.getmatn(call.from_user.id)}|", reply_markup=kvuz.kv())
            
