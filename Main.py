import telebot
from telebot import types
import wikipedia

wikipedia.set_lang("ru")
bot = telebot.TeleBot("Token")


@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_wikipedia = types.KeyboardButton("Wikipedia")
    button_gpt = types.KeyboardButton("GPT")
    keyboard.add(button_wikipedia, button_gpt)
    bot.send_message(message.chat.id,
                     "Привет! Я бот Википедии. Чтобы получить информацию "
                     "из Википедии, нажми кнопку 'Wikipedia'.\n"
                     "Чтобы воспользоваться GPT помощником, нажми кнопку 'GPT'.",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "GPT")
def gpt_message(message):
    bot.send_message(message.chat.id, "1. ChatGPT+-4 \n"
                                      "Описание:\n"
                                      "Способен обрабатывать и переводить текст, а "
                                      "также находить и исправлять ошибки в программном коде или писать его с нуля, а также многое другое. \n"
                                      "@Assistant_Chat_GPT_bot \n"
                                      "Лимиты: Лимитов нет. \n"
                                      "Цена:Бесплатный. \n "
                                      
                                      "2. Chat4Turbo \n"
                                      "Описание: \n "
                                      "Может предлагать рецепты, делать за вас домашние задания, придумывать посты для соц сетей. \n"
                                      "@chat_gpt_bro_bot\n"
                                      "Лимиты: Лимитов нет.\n"
                                      "Цена: Бесплатный. \\n"
                                      
                                      "3. Jarvis IT Assistant \n"
                                      "Описание: \n"
                                      "Обладает функциями погоды, новостей, шуток, времени, цитат и многим другим. \n"
                                      "@Jarvis_IT_Assistant_bot \n"
                                      "Лимиты: Лимитов нет. \n"
                                      "Цена: Бесплатный. \n"
                                      
                                      "4. ЧатGPT 4-TURBO OPENAI \n"
                                      "Описание: \n"
                                      "Предоставляет помощь с ответами на вопросы, переводом и генерацией текста, а также многое другое. \n"
                                      "@pro_ai_bot \n"
                                      "Лимиты: Лимитов нет. \n"
                                      "Цена: Бесплатный. \n"

                                      "5.Центр поддержки клиентов ОАО «РЖД» \n"
                                      "Описание: \n"
                                      "Предоставляет информацию о поездках, дополнительных услугах и сервисах ОАО «РЖД». \n"
                                      "@RZDOfficialBot \n"
                                      "Лимиты: Лимитов нет. \n"
                                      "Цена: Бесплатный. \n"

                     )



@bot.message_handler(func=lambda message: True)
def wiki_search(message):
    try:
        query = message.text  # запрос
        summary = wikipedia.summary(query)
        bot.send_message(message.chat.id, summary)
    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options[:5])
        bot.send_message(message.chat.id, f"Уточните ваш запрос, возможно вы имели в виду: {options}")
    except wikipedia.exceptions.PageError:
        bot.send_message(message.chat.id, "По вашему запросу ничего не найдено.")


bot.polling()
