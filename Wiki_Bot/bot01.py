import wikipedia
from buttons import til
import logging
from aiogram import Bot, Dispatcher, executor, types



API_TOKEN = '5771212988:AAEhQ-e5EN22yFNy3g2XMYQQsEqBCJpELI0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#_____________________________________________________________________________________________________

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(f"\nID: {message.from_user.id}\nUsername: {message.from_user.username}\nIsmi: {message.from_user.first_name}\nFamiliyasi: {message.from_user.last_name}")
    await message.reply("Assalom alaykum!\nUshbu bot sizga qulaylik uchun yaratildi"
    	"\nKamchilik bo'lsa oldindan uzr so'rayman.\nHurmat bilan Sanjar!😊\n\nEslatma: Qaysi tilda ma'lumot kerak bo'lsa,"
    	"\nSo'zni o'sha til alifbosida kiriting\nMasalan: Russia - Компьютер")


#______________________________________________________________________________________________________

@dp.message_handler()
async def echo(message: types.Message):
	global BOT 
	BOT = message.text
	await message.answer("Kerakli tilni tanlang: 😊",reply_markup=til)

#_______________________________________________________________________________________________________

@dp.callback_query_handler(text="uz")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("uz")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
		
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="ru")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("ru")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")

#________________________________________________________________________________________________________

@dp.callback_query_handler(text="en")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("en")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="tr")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("tr")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="fr")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("fr")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="de")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("de")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="jp")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("jp")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="es")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("es")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="cn")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("cn")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

@dp.callback_query_handler(text="de")
async def echo(call: types.CallbackQuery):
	try:
		wikipedia.set_lang("de")
		tarjima = wikipedia.summary(BOT)
		await call.message.answer(tarjima)
	except:
		await call.message.answer("Afsuski ma'lumot topilmadi.😞")
#________________________________________________________________________________________________________

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)