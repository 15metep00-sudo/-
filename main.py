# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import telebot;
bot = telebot.TeleBot('8664368206:AAEZA4NqoTa1U8H728M_OgF8VJ-_oA7XRVQ');

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
   bot.send_message(m.chat.id, 'меня зовут Аружан я учусь на третьем курсе  в политехническом колледже  мой номер 87085554447 мне нравится рисовать')
bot.polling(none_stop=True, interval=0)