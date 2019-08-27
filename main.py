import ptbot
import settings

from pytimeparse import parse
from progressbar import render_progressbar

api_key = settings.APIKEY
chat_id = settings.CHAT_ID

bot = ptbot.Bot(api_key)
bot.send_message(chat_id, 'На сколько запустить таймер?')

def notify_progress(secs_left, message_id, time):
  bot.update_message(chat_id, message_id, 'Осталось {} секунды\n{}'.format(secs_left, render_progressbar(time, secs_left)))
  if secs_left == 0:
    bot.send_message(chat_id, 'Время вышло')

def reply(text):
  time = parse(text)
  message_id = bot.send_message(chat_id, 'Осталось {} секунды\n{}'.format(time, render_progressbar(time, time)))
  bot.create_countdown(time, notify_progress, message_id=message_id, time=time)

bot.wait_for_msg(reply)