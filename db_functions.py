import sqlite3 as sql
# import datetime

# получение всех данных из каждой таблицы
def get_first_dish_list():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""select ingredient, name, url
                        from first_dish
                        """)
        return curs.fetchall()

def get_second_dish_list():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""select ingredient, name, url
                        from second_dish
                        """)
        return curs.fetchall()

def get_deserts_list():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""select ingredient, name, url
                        from deserts
                        """)
        return curs.fetchall()

def get_snacks_list():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""select ingredient, name, url
                        from snacks
                        """)
        return curs.fetchall()

def get_drinks_list():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""select ingredient, name, url
                        from drinks
                        """)
        return curs.fetchall()

# извлечение рандомной записи из каждой таблицы
def rnd_first_dish():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""SELECT *
                        from first_dish
                        order by random()
                        LIMIT 1;
                        """)
        return curs.fetchall()

def rnd_second_dish():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""SELECT *
                        from second_dish
                        order by random()
                        LIMIT 1;
                        """)
        return curs.fetchall()

def rnd_deserts():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""SELECT *
                        from deserts
                        order by random()
                        LIMIT 1;
                        """)
        return curs.fetchall()

def rnd_snacks():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""SELECT *
                        from snacks
                        order by random()
                        LIMIT 1;
                        """)
        return curs.fetchall()

def rnd_drinks():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""SELECT *
                        from drinks
                        order by random()
                        LIMIT 1;
                        """)
        return curs.fetchall()
