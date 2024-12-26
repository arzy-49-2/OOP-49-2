from lessons.lesson8 import cursor, connect


def create_users_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_view AS
        SELECT fio, age, hobby
        FROM users
        WHERE age < 26
    """)
    connect.commit()
    print("Представление user_view создано")

def get_young_users():
    cursor.execute('SELECT * FROM user_view')
    young_users = cursor.fetchall()
    print("Молодые пользователи (моложе 30 лет):")
    for user in young_users:
        print(f"FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")

create_users_view()
get_young_users