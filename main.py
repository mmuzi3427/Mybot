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
            elif call.data =="Q":
                wiki("Q")
            elif call.data =="W":
                wiki("W")
            elif call.data =="E":
                wiki("E")
            elif call.data =="R":
                wiki("R")
            elif call.data =="T":
                wiki("T")
            elif call.data =="Y":
                wiki("Y")
            elif call.data =="U":
                wiki("U")
            elif call.data =="I":
                wiki("I")
            elif call.data =="O":
                wiki("O")
            elif call.data =="P":
                wiki("P")
            elif call.data =="O1":
                wiki("Oʻ")
            elif call.data =="A":
                wiki("A")
            elif call.data =="S":
                wiki("S")
            elif call.data =="D":
                wiki("D")
            elif call.data =="F":
                wiki("F")
            elif call.data =="G":
                wiki("G")
            elif call.data =="H":
                wiki("H")
            elif call.data =="J":
                wiki("J")
            elif call.data =="K":
                wiki("K")
            elif call.data =="L":
                wiki("L")
            elif call.data =="G1":
                wiki("Gʻ")
            elif call.data =="Z":
                wiki("Z")
            elif call.data =="X":
                wiki("X")
            elif call.data =="C":
                wiki("C")
            elif call.data =="V":
                wiki("V")
            elif call.data =="B":
                wiki("B")
            elif call.data =="N":
                wiki("N")
            elif call.data =="M":
                wiki("M")
            elif call.data =="kichkina":
                wiki("")
            elif call.data == "katta":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"🔎\n\n{funcs.getmatn(call.from_user.id)}|", reply_markup=kvuz.kv())
            elif call.data == "text":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, "Jami savollar soni: 10\nTest ishlashni boshladik ❗️❗️❗️\n⏰ Vaqt belgilanmagan\n\nNatijalarni xohlagan payti chiqish tugmasi orqali ko'rishingiz mumkin 👇", reply_markup=Nat.qayt())
                bot.send_message(call.message.chat.id, "1). Hisoblang:  -78+1745 = ?\nA) 1567\nB) 1667\nC) 1777", reply_markup=Calcbtn.test1())
            elif call.data == "A1":
                delta("1). A)❌  B)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=Calcbtn.test2())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "B1":
                delta("1). B)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=Calcbtn.test2())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "C1":
                delta("1). C)❌ B)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=Calcbtn.test2())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "A2":
                delta("2). A)❌  C)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=Calcbtn.test3())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "B2":
                delta("2). B)❌  C)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=Calcbtn.test3())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "C2":
                delta("2). C)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=Calcbtn.test3())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "A3":
                delta("3). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=Calcbtn.test4())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B3":
                delta("3). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=Calcbtn.test4())
            elif call.data == "C3":
                delta("3). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=Calcbtn.test4())
            elif call.data == "A4":
                delta("4). A)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=Calcbtn.test5())
            elif call.data == "B4":
                delta("4). B)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=Calcbtn.test5())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "C4":
                delta("4). C)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=Calcbtn.test5())
            elif call.data == "A5":
                delta("5). A)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=Calcbtn.test6())
            elif call.data == "B5":
                delta("5). B)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=Calcbtn.test6())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "C5":
                delta("5). C)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=Calcbtn.test6())
            elif call.data == "A6":
                delta("6). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup= Calcbtn.test7())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B6":
                delta("6). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup= Calcbtn.test7())
            elif call.data == "C6":
                delta("6). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup= Calcbtn.test7())
            elif call.data == "A7":
                delta("7). A)❌  C)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup= Calcbtn.test8())
            elif call.data == "B7":
                delta("7). B)❌  C)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup= Calcbtn.test8())
            elif call.data == "C7":
                delta("7). C)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup= Calcbtn.test8())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "A8":
                delta("8). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup= Calcbtn.test9())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B8":
                delta("8). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup= Calcbtn.test9())
            elif call.data == "C8":
                delta("8). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup= Calabtn.test9())
            elif call.data == "A9":
                delta("9). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup= Calcbtn.test10())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B9":
                delta("9). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup= Calcbtn.test10())
            elif call.data == "C9":
                delta("9). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup= Calcbtn.test10())
            elif call.data == "A10":
                delta("10). A)❌  B)☑️")
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.send_message(call.message.chat.id, f"{Nat.natol(call.from_user.id)}", reply_markup=Nat.yangi())
                bot.send_message(call.message.chat.id, f"Jami savollar soni: 10 ta\nToʻgʻri javoblar soni: { Nat.h(call.from_user.id)} ta")
                Nat.delete(call.from_user.id)
            elif call.data == "B10":
                delta("10). B)✅")
                n()
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
                bot.send_message(call.message.chat.id, f"{Nat.natol(call.from_user.id)}", reply_markup=Nat.yangi())
                bot.send_message(call.message.chat.id, f"Jami savollar soni: 10 ta\nToʻgʻri javoblar soni: {Nat.h(call.from_user.id)} ta")
                Nat.delete(call.from_user.id)
            elif call.data == "C10":
                delta("10). C)❌  B)☑️")
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.send_message(call.message.chat.id, f"{Nat.natol(call.from_user.id)}", reply_markup=Nat.yangi())
                bot.send_message(call.message.chat.id, f"Jami savollar soni: 10 ta\nToʻgʻri javoblar soni: {Nat.h(call.from_user.id)} ta")
                Nat.delete(call.from_user.id)
            elif call.data == "delete1":
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == "1_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMLZtb82iRb_tmr9Sv1nRQnBGG2I6EAAjg5AAIoi2lJeLuJ88cn0Ok1BA", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "2_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMPZtb-P1QE9omLTMfSFC6DTIft_hgAAtY7AAIBJXlJ_EQMKEiWma81BA", caption="<b>🎞 Video\n•   Hajmi -- 450.6 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="3_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMWZtb-qB-RGhgxSRpzZEBEYpl0o54AAok1AAIv5qhJa4Flwozf7ig1BA", caption="<b>🎞 Video\n•   Hajmi -- 438.2 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="4_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMYZtb-53l1ROnebXtVojaVvfPDvIkAAqtEAAL4llhKS2PZRWxNxQQ1BA", caption="<b>🎞 Video\n•   Hajmi -- 513.5 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="5_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMhZtcKnKHQAs-RevecLca-wEN4E7gAAnY4AALBqwABS72Icmc__exbNQQ", caption="<b>🎞 Video\n•   Hajmi -- 369.5 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="6_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMjZtcMf843PbYuqr09mhx4gl0BVf8AAns4AALBqwABSzA8_MLx2TNtNQQ", caption="<b>🎞 Video\n•   Hajmi -- 287.6 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="7_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMlZtcM-aU2B6pdWxrp46zJYOGkvCgAAiUlAAKMTalLOTyuc6LLNfo1BA", caption="<b>🎞 Video\n•   Hajmi -- 560.5 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="8_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMnZtcNVBlgI5R5x0v3amg2KX2jpa4AAhQ0AALLNHFKoy5L41iKfGI1BA", caption="<b>🎞 Video\n•   Hajmi -- 410.2 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="9_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMpZtcNq3M3Gu880pIuaIAbQQ5R7mgAAuhEAAL0EzFI01zcnI6F2aQ1BA", caption="<b>🎞 Video\n•   Hajmi -- 714.4 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="10_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMrZtcTC2zQaO7Vdsb_30PW98nhdYMAAps_AALMFSFLEkYakZd3tGE1BA", caption="<b>🎞 Video\n•   Hajmi -- 576.5 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="11_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMtZtcTdkI2clvKs_q9PhzDqxvDd78AAs83AALjMnBKIKhvXMPOJes1BA", caption="<b>🎞 Video\n•   Hajmi -- 440.7 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="12_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMvZtcT-Kja0HSj9fsulgit9GwULAIAAupDAALvMPlJjJVTifspfJA1BA", caption="<b>🎞 Video\n•   Hajmi -- 498.9 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="13_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMxZtcUTL5OttGdGDa3ohCy2c-EqM8AAgE_AAKnogFKL3xG1I8EsfY1BA", caption="<b>🎞 Video\n•   Hajmi -- 286.6 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="14_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAMzZtcV4ERFBaE5YkGtpM8pqTD-XFUAAl0-AAJas4FKttyTThwm7ZA1BA", caption="<b>🎞 Video\n•   Hajmi -- 461.7 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="15_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAM1ZtcaQBjcUt-jo2iinn5N72qfsS4AAn8oAALPNOBIpzKtkPRGIm01BA", caption="<b>🎞 Video\n•   Hajmi -- 343.5 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="16_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAM3Ztcaj36Z5BXa5FKGikTyc_WFVnoAAoIoAALPNOBIM7A5SpdceH01BA", caption="<b>🎞 Video\n•   Hajmi -- 547.2 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="17_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAM5Ztca17Cs3nlVpuNxZu0slJ6_WC4AAoQoAALPNOBImQX4yp4DwFU1BA", caption="<b>🎞 Video\n•   Hajmi -- 435.6 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="18_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAM7ZtcbKCkrSld7hoRFuuW64J36QyAAAvcuAAIBfmlIUGUgQPJ0lGw1BA", caption="<b>🎞 Video\n•   Hajmi -- 273.4 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="19_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAM9ZtcbSCT3J_yjRfYKp-l9fyktGo0AAjMpAAIZ7PFIzTNJC9WshYA1BA", caption="<b>🎞 Video\n•   Hajmi -- 522.3 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="20_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAAM_ZtcbaZoZ0H0cyjMOwCSIc68ggk4AApEhAAIbhKBIfh9gwAoC3R41BA", caption="<b>🎞 Video\n•   Hajmi -- 251 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="21_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANBZtcbiHCM8DXcAssN73_ZVPAqXjMAAoAoAAJNXrhIGnmBKlVycE81BA", caption="<b>🎞 Video\n•   Hajmi -- 478 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="22_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANDZtcbqL7X2C8YMPAlrBW9XZcNF4YAArwuAAJnsNFIKVCE9nfV5sM1BA", caption="<b>🎞 Video\n•   Hajmi -- 500.9 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="23_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANFZtcb0FpMQ_Nn9w88a7WExQm3PisAAjcpAAIZ7PFIWmOtoPQjOXo1BA", caption="<b>🎞 Video\n•   Hajmi -- 469.2 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="24_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANHZtcb8azUFjHBhbXdzY6_RZP4N8oAAv1AAAJ-iOhJoC4viC2EEVQ1BA", caption="<b>🎞 Video\n•   Hajmi -- 621.5 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="25_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANJZtccDZGdZQJgInzMx92fvGYI50sAAmEtAAJJ7zlJmDD6oOAYY301BA", caption="<b>🎞 Video\n•   Hajmi -- 538.3 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="26_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANLZtccKfx4IcRbH_PWz0D6UnVJh4kAAlgvAAJVY9hKFZyQoBN8jdU1BA", caption="<b>🎞 Video\n•   Hajmi -- 419.9 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="27_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANNZtccRwdpIDHhLYOfupDS-R5eTmAAAhEvAAJkxMBKFeldFE41RTA1BA", caption="<b>🎞 Video\n•   Hajmi -- 494 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="28_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANPZtccX7i2EFhm4Wzg-LqAAnW52jIAAqYjAALs4GhJixHUIRTs0BU1BA", caption="<b>🎞 Video\n•   Hajmi -- 519.7 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="29_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANRZtccei-AY6QP8UmhBqm1Wg8bF-wAAk8vAAKB44FJhQ9HNfn4KrQ1BA", caption="<b>🎞 Video\n•   Hajmi -- 474.6 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="30_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANTZtccmGrRGLx8UDs9dhdJGLVh8yIAAlwvAAJVY9hKp5Fh48UL5EE1BA", caption="<b>🎞 Video\n•   Hajmi -- 510.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="31_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANVZtcctt_yQ8LTIA1m65FmpBoqZYsAAqoqAAKS4ChL00JGDQ7HT4w1BA", caption="<b>🎞 Video\n•   Hajmi -- 455.7 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="32_dars":
                bot.send_video(call.message.chat.id, "BAACAgIAAxkBAANXZtcc0pYi1rftYCYaDw_tWLbarC0AAistAAIPizhKFI_bKecDRMI1BA", caption="<b>🎞 Video\n•   Hajmi -- 582.7 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="matematika":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, "Matematika kursi darslari tanlang!", reply_markup=Video.videos())
            elif call.data == "1":
                editing("1")
            elif call.data =="2":
                editing("2")
            elif call.data =="3":
                editing("3")
            elif call.data =="4":
                editing("4")
            elif call.data =="5":
                editing("5")
            elif call.data =="6":
                editing("6")
            elif call.data =="7":
                editing("7")
            elif call.data =="8":
                editing("8")
            elif call.data =="9":
                editing("9")
            elif call.data =="0":
                editing("0")
            elif call.data == "+":
                editing1("+")
            elif call.data =="-":
                editing1("-")
            elif call.data == "*":
                editing1("*")
            elif call.data == "/":
                editing1("/")
            elif call.data == "nuqta":
                editing2(".")
            elif call.data == "=":
                func.teng(call.from_user.id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=func.retson(call.from_user.id), reply_markup=Calcbtn.calcb())
            elif call.data == "clear":
                try:
                    func.clear(call.from_user.id)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Natija :  " + func.retson(call.from_user.id) + "\n....@Matematikauniversalbot....", reply_markup= Calcbtn.calcb())
                except:
                    bot.answer_callback_query(call.id, "Xatolik yuz berdi", show_alert=True)
            else:
                try:
                    text=calldat.call1[str(call.data)]
                    bot.send_message(call.message.chat.id, "⌛"+text)
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="⚠️ Bu tugma ishlamayapti! ⌛", show_alert=True)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.answer_callback_query(callback_query_id=call.id, text="Barcha kanallarga obuna boʻlishingiz shart! ✅", show_alert=True)
            bot.send_message(call.message.chat.id, "Kanallarga obuna boʻling!", reply_markup= Calcbtn.obuna())
    elif call.from_user.language_code == "ru":
        def son(n):
            funcs.changeson(call.from_user.id, n)
            try:
                d = funcs.getSon(call.from_user.id)
                matn = ""
                for i in d:
                    matn += i
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Текущий статус:\n\n{matn}", reply_markup=Calcbtn.calcb())
            except:
                bot.answer_callback_query(call.id, "Произошла ошибка ❌", show_alert=True)
        if call.data == "1":
            son(1)
        elif call.data == "2":
            son(2)
        elif call.data == "3":
            son(3)
        elif call.data == "4":
            son(4)
        elif call.data =="5":
            son(5)
        elif call.data =="6":
            son(6)
        elif call.data =="7":
            son(7)
        elif call.data =="8":
            son(8)
        elif call.data =="9":
            son(9)
        elif call.data =="0":
            son(0)
        def a(a):
            funcs.changeamal(call.from_user.id, a)
             call.data == "3":
            son(3)
        elif call.data == "4":
            son(4)
        elif call.data =="5":
            son(5)
        elif call.data =="6":
            son(6)
        elif call.data =="7":
            son(7)
        elif call.data =="8":
            son(8)
        elif call.data =="9":
            son(9)
        elif call.data =="0":
            son(0)
        def a(a):
            funcs.changeamal(call.from_user.id, a)
            try:
                dat = funcs.getSon(call.from_user.id)
                funcs.belgi(call.from_user.id)
                mat = ""
                for i in dat:
                    mat += i
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Текущий статус:\n\n{mat}", reply_markup=Calcbtn.calcb())
            except:
                bot.answer_callback_query(call.id, "Произошла ошибка ❌", show_alert=True)
        if call.data == "+":
            a("+")
        elif call.data == "-":
            a("-")
        elif call.data == "*":
            a("*")
        elif call.data == "/":
            a("//")
        elif call.data == "toza":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="История калькулятора очищена, и вы можете продолжить расчет!...", reply_markup=Calcbtn.calcb())
                funcs.toza(call.from_user.id)
            except:
                bot.answer_callback_query(callback_query_id=call.id, text="Слишком много попыток ❌\nДанные удалены!\nВы можете продолжить подсчет, нажимая на цифры. Все начинается с 0 ✅", show_alert=True)
        elif call.data == "=":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Результат:\n\n{funcs.getRes(call.from_user.id)}", reply_markup=Calcbtn.calcb())
                funcs.davomi(call.from_user.id, funcs.getRes(call.from_user.id))
            except:
                bot.answer_callback_query(call.id, "Произошла ошибка ❌ ♻️", show_alert=True)
        elif call.data == "delru":
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == "qoshimcha":
            bot.answer_callback_query(callback_query_id=call.id, text="Скоро!", show_alert=True)
def get1(m):
    test.addism(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Ism tahrirlandi! ✅")
    bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup=Calcbtn.edit())
    bot.send_message(admin_id, f"Bot sozlamalari orqali ma'lumot oʻzgartirildi✏️\n Oʻzgartirilgan ma'lumot ism ✅!\n\nFoydalanuvchi ma'lumotlari!\nIsmi: {test.ism(m.from_user.id)}✅\nFamiliyasi: {test.familiya(m.from_user.id)}\nYoshi: {test.yosh(m.from_user.id)} da\nID: {m.from_user.id}\nUsername: @{m.from_user.username}", reply_markup= Calcbtn.delete())
def get_name(m):
    test.addism(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.delete_message(m.chat.id, m.message_id - 2)
    bot.delete_message(m.chat.id, m.message_id - 3)
    bot.send_message(m.chat.id, "Yaxshi endi familiyangizni kiriting!")
    bot.register_next_step_handler(m, get_yosh)
def get2(m):
    test.addfamiliya(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Familiya tahrirlandi! ✅")
    bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup= Calcbtn.edit())
    bot.send_message(admin_id, f"Bot sozlamalari orqali ma'lumot oʻzgartirildi✏️\n Oʻzgartirilgan ma'lumot familiya ✅!\n\nFoydalanuvchi ma'lumotlari!\nIsmi: {test.ism(m.from_user.id)}\nFamiliyasi: {test.familiya(m.from_user.id)}✅\nYoshi: {test.yosh(m.from_user.id)} da\nID: {m.from_user.id}\nUsername: @{m.from_user.username}", reply_markup= Calcbtn.delete())
def get_yosh(m):
    test.addfamiliya(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Yoshingiz nechada?")
    bot.register_next_step_handler(m, tasdiqlash)
def get_yosh(m):
    test.addfamiliya(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Yoshingiz nechada?")
    bot.register_next_step_handler(m, tasdiqlash)
def get3(m):
    test.addyosh(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Yosh tahrirlandi! ✅")
    bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup= Calcbtn.edit())
    bot.send_message(admin_id, f"Bot sozlamalari orqali ma'lumot oʻzgartirildi✏️\n Oʻzgartirilgan ma'lumot yosh ✅!\n\nFoydalanuvchi ma'lumotlari!\nIsmi: {test.ism(m.from_user.id)}\nFamiliyasi: {test.familiya(m.from_user.id)}\nYoshi: {test.yosh(m.from_user.id)} da ✅\nID: {m.from_user.id}\nUsername: @{m.from_user.username}", reply_markup= Calcbtn.delete())
def tasdiqlash(m):
    test.addyosh(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(admin_id, f"Yangi fiydalanuvchi\nIsmi: {test.ism(m.from_user.id)}\n<b>Familiyasi: </b> {test.familiya(m.from_user.id)}\nYoshi: {test.yosh(m.from_user.id)}\nUsername: @{m.from_user.username}\nID: {m.from_user.id}", parse_mode='html')
    bot.send_message(m.chat.id, f"Ma'lumotlaringiz toʻgʻri ekanligini tekshiring!\n\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)}\n\n\n\n\nAks holda <b>«Testda qatnashish»</b> tugmasini bosib qayta roʻyxatdan oʻting!", parse_mode='html', reply_markup= Calcbtn.true())
bot.infinity_polling(skip_pending = True)
