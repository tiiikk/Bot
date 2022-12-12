import telebot
from telebot import types
import scrap

API_Key = '5856739243:AAE91ARzXdwTlJ0HGDjFDfZ6iY1wMjl_Yro'
bot = telebot.TeleBot(API_Key)




@bot.message_handler(commands = ['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Այսորվա միջին առքի փոխարժեքը Հայաստանում',callback_data='q1')
    item1 = types.InlineKeyboardButton('Այսորվա միջին վաճառքի փոխարժեքը Հայաստանում',callback_data='q2')

    markup.add(item,item1)
    bot.send_message(message.chat.id, 'Բարև!',reply_markup=markup)




@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
    if call.message:
        if call.data=='q1':
            for curr, value in scrap.arq_dict.items():
                arjuyt = curr
                arq_arjeq = value
                bot.send_message(call.message.chat.id, f'{arjuyt}:  {arq_arjeq} AMD')
        if call.data=='q2':
            for curr, value in scrap.vacharq_dict.items():
                arjuyt = curr
                vach_arjeq = value
                bot.send_message(call.message.chat.id, f'{arjuyt}:   {vach_arjeq} AMD')




bot.polling()