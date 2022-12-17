"""Модуль парсит товары из группы ВК, помещает их в словать и возвращает этот словарь."""
import vk_api
import my_vk_token
import time

session = vk_api.VkApi(token=my_vk_token.token)
vk = session.get_api()
my_vk_id = my_vk_token.my_vk_id  # мой id хранится в my_token
my_group_id = 215973925
my_owner_group_id = -215973925
heliy78_gpoup_id = -176444976


def normal_price(s) -> int:
    """Получает цену из VK Api и возвращает её"""
    if len(s) <= 5:
        return int(s[:-2])
    else:
        price0 = s.split()
        price = int(price0[0] + price0[1][:-2])
        return price


def market_get_goods_dict(group_id):
    '''парсим товары группы и добавляем их все в словарь {id_товара : ['Название_товара', цена товара]}'''
    ''''''
    ''' Если число товаров < 200 используется 1 запрос. Если >200 используются запросы по 200 и 1 запрос на оставшуюся часть'''
    goods_dict = {}
    goods_00 = session.method('market.get', {'owner_id': group_id, 'count': 5})
    count_of_goods = goods_00["count"]
    n = count_of_goods // 200
    np = count_of_goods % 200
    time.sleep(0.5)

    print("count_of_goods = ", count_of_goods, 'n = ', n, 'np = ', np)

    if count_of_goods <= 200:

        goods0 = session.method('market.get', {'owner_id': group_id, 'count': count_of_goods})

        for i in range(count_of_goods):
            price = normal_price(goods0['items'][i]['price']['text'])
            goods_dict[goods0['items'][i]['id']] = [goods0['items'][i]['title'], price]
    else:
        for i in range(n):
            shift = i * 200
            goods0 = session.method('market.get', {'owner_id': group_id, 'count': 200, 'offset': shift})
            for j in range(200):
                price = normal_price(goods0['items'][j]['price']['text'])
                goods_dict[goods0['items'][j]['id']] = [goods0['items'][j]['title'],
                                                        price]  # key словаря = id товара; value = [название товара, цена товара]

        shift = n * 200
        goods0 = session.method('market.get', {'owner_id': group_id, 'count': np, 'offset': shift})
        for i in range(np):
            price = normal_price(goods0['items'][i]['price']['text'])
            goods_dict[goods0['items'][i]['id']] = [goods0['items'][i]['title'],
                                                    price]

    return goods_dict


def create_backup_goods_dict(dict: dict) -> dict:
    """Возвращает словарь товаров из ВК. {название_товара:цена}"""
    new_dict = {}

    for i in dict.values():
        new_dict[i[0]] = i[1]

    return new_dict


def create_backup_goods_dict_id(dict: dict) -> dict:
    """Возвращает словарь товаров из ВК. {название_товара:цена}"""
    new_dict = {}

    for i in dict.keys():
        new_dict[dict[i][0]] = i

    return new_dict


def change_VK_price(group_id: int, dict_name: dict, dict_id: dict):
    """ Меняет цены в группе ВК. dict_name = DB_functions.final_price_dict, dict_id = DB_functions.backup_dict_id"""
    for i in dict_name.keys():
        time.sleep(1)
        item_id = dict_id[i]
        price = dict_name[i]
        if price > 0:
            session.method('market.edit', {'owner_id': group_id, 'item_id': item_id, 'price': price})
            print(f'{i} цена именена на {price}')
