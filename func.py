from checks import *
from functools import reduce
from calculator import *

# def add(update, context):
#     arg = context.args
#     if checks_for_digit(arg) == False:
#         context.bot.send_message(update.effective_chat.id, "Некоррекнтный ввод, дай цифры")
#     elif not arg:
#         context.bot.send_message(update.effective_chat.id, "Как-то нечего считать")
#     else:
#         x = lambda a,b: int(a)+int(b)
#         g = reduce(x, arg)
#         arg = " + ".join(list(map(str, arg)))
#         context.bot.send_message(update.effective_chat.id, f"{arg} = {g}")
    


def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет, я калькулятор, что хочешь посчитать? Как пользоваться тут /info")



def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Введи уравнение одной строкой пример: 5+2-1")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    elif checks_for_produkt(text) == True and check_for_logic(text) == True:
        result = start_modul(text)
        context.bot.send_message(update.effective_chat.id, f"{text} = {result}")
    else: context.bot.send_message(update.effective_chat.id, "Не понятное уравнение")

def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Такой команды нет')


