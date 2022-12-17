"""Модуль содержит фунции для работы с Sqlite"""

import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()


def start():
    """Создает 4 таблицы, если они ещё не созданы"""
    sql.execute('''CREATE TABLE IF NOT EXISTS market_main( 
                id INTEGER,
                item_name TEXT,
                price INTEGER
        )''')
    db.commit()

    sql.execute('''CREATE TABLE IF NOT EXISTS market_vk(
                    id INTEGER,
                    item_name TEXT,
                    price INTEGER
            )''')
    db.commit()

    sql.execute('''CREATE TABLE IF NOT EXISTS count_goods(
                       item_name TEXT,
                       n1 INTEGER DEFAULT 0 NOT NULL,
                       n2 INTEGER DEFAULT 0 NOT NULL,
                       n3 INTEGER DEFAULT 0 NOT NULL,
                       n4 INTEGER DEFAULT 0 NOT NULL,
                       n5 INTEGER DEFAULT 0 NOT NULL,
                       n6 INTEGER DEFAULT 0 NOT NULL,
                       n7 INTEGER DEFAULT 0 NOT NULL,
                       n8 INTEGER DEFAULT 0 NOT NULL,
                       n9 INTEGER DEFAULT 0 NOT NULL,
                       n10 INTEGER DEFAULT 0 NOT NULL,
                       n11 INTEGER DEFAULT 0 NOT NULL,
                       n12 INTEGER DEFAULT 0 NOT NULL,
                       n13 INTEGER DEFAULT 0 NOT NULL,
                       n14 INTEGER DEFAULT 0 NOT NULL,
                       n15 INTEGER DEFAULT 0 NOT NULL                  
               )''')
    db.commit()
    # проверяем наличие таблицы price. Если её нет, создаём таблицу и добавляем туда 1 запись
    sql.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='price';''')
    r = sql.fetchall()
    if r != []:
        print('таблица price уже существует')
    else:
        sql.execute('''CREATE TABLE IF NOT EXISTS price(
                                   id INTEGER,
                                   p1 INTEGER,
                                   p2 INTEGER,
                                   p3 INTEGER,
                                   p4 INTEGER,
                                   p5 INTEGER,
                                   p6 INTEGER,
                                   p7 INTEGER,
                                   p8 INTEGER,
                                   p9 INTEGER,
                                   p10 INTEGER,
                                   p11 INTEGER,
                                   p12 INTEGER,
                                   p13 INTEGER,
                                   p14 INTEGER,
                                   p15 INTEGER                  
                           )''')
        db.commit()
        print('таблица price создана')

        sql.execute(
            f"""INSERT INTO price (id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15)
         VALUES (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);""")
        print('в таблицу price добавлена первая запись. Все p == 0')
    db.commit()

    # проверяем наличие таблицы names. Если её нет, создаём таблицу и добавляем туда 1 запись
    sql.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='names';''')
    r = sql.fetchall()
    if r != []:
        print('таблица names уже существует')
    else:
        sql.execute('''CREATE TABLE IF NOT EXISTS names(
                                       id INTEGER,
                                       p1 TEXT,
                                       p2 TEXT,
                                       p3 TEXT,
                                       p4 TEXT,
                                       p5 TEXT,
                                       p6 TEXT,
                                       p7 TEXT,
                                       p8 TEXT,
                                       p9 TEXT,
                                       p10 TEXT,
                                       p11 TEXT,
                                       p12 TEXT,
                                       p13 TEXT,
                                       p14 TEXT,
                                       p15 TEXT                  
                               )''')
        db.commit()
        print('таблица price создана')

        sql.execute(
            f"""INSERT INTO names (id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15)
             VALUES (1, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15");""")
        print('в таблицу names добавлена первая запись.')
    db.commit()


def bd_update_vk_first(dict: dict):
    """Удаляет все старые данные из таблицы market_vk и наполняет её актуальными данными"""
    sql.execute('''DELETE FROM market_vk;''')
    db.commit()
    print('\33[31mтаблица market_vk потёрта\33[0m')
    for i in dict.keys():
        sql.execute(
            '''INSERT INTO market_vk (id, item_name, price) VALUES ({0}, "{1}", {2});'''.format(i, dict[i][0],
                                                                                                dict[i][1])

        )
    db.commit()
    print('БД \33[34mVK\33[0m обновлена')


def create_list_of_missing_goods() -> list:
    """Возвращает список товаров, которых нет в market_main"""
    sql.execute(
        '''SELECT item_name FROM market_vk'''
    )
    row_market = sql.fetchall()
    sql.execute(
        '''SELECT item_name FROM market_main'''
    )
    row_main = sql.fetchall()
    names_vk, names_main = [], []
    for i in row_market:
        names_vk.append(i[0])
    for i in row_main:
        names_main.append(i[0])
    temp_list = []

    for i in range(len(names_vk)):
        if names_vk[i] not in names_main:
            temp_list.append(names_vk[i])

    return temp_list


def create_list_of_missing_goods2() -> list:
    """Делает то же самое, что и create_list_of_missing_goods но посредством SQL запроса"""
    sql.execute(
        '''SELECT market_vk.item_name, market_vk.price
        FROM market_vk
        LEFT OUTER JOIN market_main ON market_vk.item_name=market_main.item_name
        WHERE market_main.item_name IS NULL
        '''
    )
    temp_list = sql.fetchall()

    return temp_list


def delete_renamed_goods():
    """Удаляет из market_main переименованные товары"""
    sql.execute(
        '''SELECT market_main.item_name, market_main.price
        FROM market_main
        LEFT OUTER JOIN market_vk ON market_main.item_name=market_vk.item_name
        WHERE market_vk.item_name IS NULL
        '''
    )
    temp_list = sql.fetchall()
    for i in temp_list:
        item = i[0]
        sql.execute(f'''DELETE FROM market_main WHERE item_name = "{item}"''')
        db.commit()
        print(f'Товар {item} удален')


def bd_update(list: list):
    """Добавляет в БД товары, появившиеся в ВК"""

    # Выгружаем все товары из market_vk и добавляем их в список
    sql.execute('''SELECT * FROM market_vk''')
    all_goods_row = sql.fetchall()
    # добавляем в market_main все товары из list(там должны быть новые товары из market_vk {за поиск новых товаров отвечает функция create_list_of_missing_goods})
    for i in range(len(all_goods_row)):
        if all_goods_row[i][1] in list:
            id = all_goods_row[i][0]
            name = all_goods_row[i][1]
            price = all_goods_row[i][2]
            sql.execute(
                f'''INSERT INTO market_main (id, item_name, price) VALUES ({id}, "{name}", {price});'''
            )
            db.commit()

    print('[INFO] Таблица \33[34mmarket_main\33[0m обновлена')


def select_name_and_price() -> dict:
    """Получаем словарь item_name:price из market_main"""
    dict = {}
    sql.execute(
        'SELECT item_name, price FROM market_main'
    )
    result = sql.fetchall()
    for i in range(len(result)):
        dict[result[i][0]] = result[i][1]

    return dict


def change_table_main_price():
    """Меняем цены в таблице market_main"""
    sql.execute('''SELECT market_main.item_name, count_goods.n1, count_goods.n2, count_goods.n3, count_goods.n4,
     count_goods.n5, count_goods.n6, count_goods.n7, count_goods.n8, count_goods.n9, count_goods.n10, count_goods.n11,
      count_goods.n12, count_goods.n13, count_goods.n14, count_goods.n15 FROM market_main
       JOIN count_goods ON market_main.item_name = count_goods.item_name''')
    main_vk_list = sql.fetchall()
    sql.execute('SELECT p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15 FROM price WHERE id=1')
    price_list = sql.fetchall()
    p1 = price_list[0][0]
    p2 = price_list[0][1]
    p3 = price_list[0][2]
    p4 = price_list[0][3]
    p5 = price_list[0][4]
    p6 = price_list[0][5]
    p7 = price_list[0][6]
    p8 = price_list[0][7]
    p9 = price_list[0][8]
    p10 = price_list[0][9]
    p11 = price_list[0][10]
    p12 = price_list[0][11]
    p13 = price_list[0][12]
    p14 = price_list[0][13]
    p15 = price_list[0][14]
    print('md=', main_vk_list)
    print('pl = ', price_list, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15)
    print(main_vk_list[0][1], main_vk_list[0][2])
    for i in range(len(main_vk_list)):
        n1 = main_vk_list[i][1]
        n2 = main_vk_list[i][2]
        n3 = main_vk_list[i][3]
        n4 = main_vk_list[i][4]
        n5 = main_vk_list[i][5]
        n6 = main_vk_list[i][6]
        n7 = main_vk_list[i][7]
        n8 = main_vk_list[i][8]
        n9 = main_vk_list[i][9]
        n10 = main_vk_list[i][10]
        n11 = main_vk_list[i][11]
        n12 = main_vk_list[i][12]
        n13 = main_vk_list[i][13]
        n14 = main_vk_list[i][14]
        n15 = main_vk_list[i][15]
        new_price = p1 * n1 + p2 * n2 + p3 * n3 + p4 * n4 + p5 * n5 + p6 * n6 + p7 * n7 + p8 * n8 + p9 * n9 + \
                    p10 * n10 + p11 * n11 + p12 * n12 + p13 * n13 + p14 * n14 + p15 * n15
        print('new_price = ', new_price, '\33[31mitem_name =\33[0m', main_vk_list[i][0])
        sql.execute(f'UPDATE market_main set price={new_price} where item_name="{main_vk_list[i][0]}"')
        db.commit()


def compare_dict(dict_old: dict, dict_new: dict) -> dict:
    """Сравнивает между собо старый и новый словари. Помещает новые товары в словарь и возращает его"""
    dict_new2 = {}
    for i in dict_old.keys():
        if dict_old[i] != dict_new[i]:
            dict_new2[i] = dict_new[i]
    return dict_new2


def compare_final_price(dict_old: dict, dict_new: dict) -> dict:
    """Сравнивает между собо старый и новый словари. Помещает новые товары в словарь и возращает его"""
    dict_new2 = {}
    for i in dict_old.keys():
        if dict_old[i] != dict_new[i]:
            dict_new2[i] = dict_new[i]

    return dict_new2


