# База данных
import sqlite3

# Подключение к БД
conn = sqlite3.connect('delivery.db', check_same_thread=False)
# Python + SQL
sql = conn.cursor()


# Создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER, name TEXT, number TEXT);')
# Создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pr_des TEXT, pr_price REAL, pr_count INTEGER, '
            'pr_photo TEXT);')
# Создание таблицы корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart '
            '(user_id INTEGER, user_product TEXT, user_pr_quantity INTEGER);')


## Методы для пользователя ##
# Регистрация
def register(user_id, user_name, user_number):
    sql.execute('INSERT INTO users VALUES(?, ?, ?);',
                (user_id, user_name, user_number))
    # Фиксируем изменения
    conn.commit()


# Проверка пользователя на наличие в БД
def check_user(user_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (user_id,)).fetchone():
        return True
    else:
        return False
