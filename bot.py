# Алгоритмы бота
import telebot
import buttons as bt
import database as db

# Создаем объект бота
bot = telebot.TeleBot('TOKEN')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_message(msg):
    user_id = msg.from_user.id
    check = db.check_user(user_id)

    if check:
        bot.send_message(user_id, 'Здравствуйте! Добро пожаловать!')
    else:
        bot.send_message(user_id, 'Здравствуйте! Давайте начнем регистрацию!\n'
                                  'Введите свое имя')
        # Переход на этап получения имени
        bot.register_next_step_handler(msg, get_name)


# Этап получения имени
def get_name(msg):
    user_id = msg.from_user.id
    user_name = msg.text

    bot.send_message(user_id, 'Отлично! Теперь отправьте номер!',
                     reply_markup=bt.num_button())
    # Переход на этап получения номера
    bot.register_next_step_handler(msg, get_number, user_name)


def get_number(msg, user_name):
    user_id = msg.from_user.id

    # Если пользователь отправил номер по кнопке
    if msg.contact:
        user_number = msg.contact.phone_number
        db.register(user_id, user_name, user_number)
        bot.send_message(user_id, 'Регистрация прошла успешно!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    # Если пользователь отправил номер не по кнопке
    else:
        bot.send_message(user_id, 'Отправьте номер через кнопку!')
        # Возврат на этап получения номера
        bot.register_next_step_handler(msg, get_number, user_name)


# Запуск бота
bot.polling()
