import os
import telebot
from chat_gpt import chatgpt

bot = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY"))

@bot.message_handler(content_types=['text'])
def handle_message(message):
    response = chatgpt(message.text)
    
    bot.send_message(chat_id=message.from_user.id, text=response)
    print(f"""
          user: {message.from_user.username}
          message: {message.text}
          resp: {response}
          """)

bot.polling()
