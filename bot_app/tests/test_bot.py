import os
import pytest
from bot_app import handle_message
import telebot


bot = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY"))
print(f'token: {os.getenv("TELEGRAM_API_KEY")}')
@bot.message_handler(func=lambda _: True)
def handle_message(message):
    return message



@pytest.mark.parametrize("message, expected", [
        (handle_message('test'), 'Test Ok!'),
    ],
    ids=[
        'first test',
    ]
)

def test_bot_app(message, expected):
    assert handle_message(message) == expected