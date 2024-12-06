from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


til = InlineKeyboardMarkup(
	inline_keyboard = [
	    [
	        InlineKeyboardButton(text="🇨🇳Xitoycha", callback_data="cn"),
	        InlineKeyboardButton(text="🇷🇺Ruscha", callback_data="ru"),
	        InlineKeyboardButton(text="🇹🇷Turkcha", callback_data="tr"),
	        InlineKeyboardButton(text="🇫🇷Fransuzcha", callback_data="fr")


	    ],
	    [
	        InlineKeyboardButton(text="🇩🇪Nemischa", callback_data="de"),
	        InlineKeyboardButton(text="🇪🇸Ispancha", callback_data="es"),
	        InlineKeyboardButton(text="🇸🇦Arabcha", callback_data="sa"),
	        InlineKeyboardButton(text="🇯🇵Yaponcha", callback_data="jp")
	    ],
	    [
	        InlineKeyboardButton(text="🇺🇸Inglizcha", callback_data="en"),
	        InlineKeyboardButton(text="🇺🇿O'zbekcha", callback_data="uz")
	    ],
	],
)
