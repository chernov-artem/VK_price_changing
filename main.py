"""Программа для изменения цен на товары в группе ВК.
Позволяет автоматически изменить цены на товары в случае подорожания какого-либо компонента товара.

Зачем эта программа:
Пример из жизни: группа по доставке шаров с гелием. В группе 1000+ товаров, каждый товар представляет собой
комбинацию из разных шаров(латексные, фольгированные, шары-цифры, большие шары и пр.)
Гелий дорожает на 40% -> вручную меняем цены на 1000 товаров
Гелий снова дорожает на 15% -> снова меняем товары
В результате за период 5 месяцев гелий сначала подорожал до 300% потом цена вернулась к прежним значениям.
Никто не стал вручную пересчитывать цены много раз - всё продавцы шаров просто писали "цены не актуальны - уточняйте"
Это вызывало недовольство клиентов.

С этой программой достаточно просто поменять цены на каждый вид шаров и она поменяет цены на все товары в группе.
Перед этим нужно внести данные по составу каждого набора в БД через графический интерфейс программы.

https://vk.com/muffin_programs_for_business

"""
import DB_functions as db
import get_group_dict
import copy
import GUI

old_price_G = {}
backup_dict_id_G = {}
backup_dict_G = {}


def finish():
    '''Тут начинается 2 автоматическая часть'''
    global final_price_dict
    # ШАГ 5.4 меняем цены в market_main
    db.change_table_main_price()
    # ШАГ 5.5 создаем словарь new_price
    new_price = db.select_name_and_price()
    print('backup_dict_id = ', backup_dict_id_G)
    print('backup_dict = ', backup_dict_G)
    print('old =', old_price_G)  # удалить потом
    print('new = ', new_price)  # удалить потом
    # ШАГ 6.1 создаём словарь с товарами, в который поменялись цены dict_new_price_goods
    dict_new_price_goods = db.compare_dict(old_price_G, new_price)
    print(dict_new_price_goods)
    # Шаг 6.2 созадаем словарь final_price_dict в который будут добавлены товары, цена на которые поменялись
    final_price_dict = db.compare_final_price(backup_dict_G, new_price)
    print("backup_dict_G = ", backup_dict_G)
    print("new_price = ", new_price)
    print('final_price_dict = ', final_price_dict)

    # Шаг 7 запускаем функцию изменения товаров в самой группе ВК
    '''GUI будет вызываться отдельной кнопкой'''
    get_group_dict.change_VK_price(get_group_dict.my_owner_group_id, final_price_dict, backup_dict_id_G)
    print('\33[31mРабота программы окончена\33[0m')


def main():
    # ШАГ 0 создаём 4 таблицы(IF NOT EXISTS)
    db.start()

    # ШАГ 1 получаем товары с группы вк
    temp_list = get_group_dict.market_get_goods_dict(
        get_group_dict.my_owner_group_id)

    # Шаг 1.1 Создаем бэкап-словарь товаров из группы ВК
    global backup_dict
    global backup_dict_G
    global backup_dict_id
    global old_price_G
    global backup_dict_id_G
    backup_dict0 = copy.deepcopy(temp_list)  # получаем копию списка товаров

    # Шаг 1.2 Приводим словарь к виду {"название товара":цена}
    backup_dict = get_group_dict.create_backup_goods_dict(backup_dict0)
    backup_dict_G = copy.deepcopy(backup_dict)
    backup_dict_id = get_group_dict.create_backup_goods_dict_id(backup_dict0)
    backup_dict_id_G = copy.deepcopy(backup_dict_id)

    # ШАГ 2 удаляем всё из таблицы market_vk и наполняем новыми данными
    db.bd_update_vk_first(temp_list)

    # ШАГ 3 создаём список новых товаров
    a = db.create_list_of_missing_goods()
    print('a = ', a)

    # проверка новых товаров другой функцией
    a1 = db.create_list_of_missing_goods2()
    print('a1 = ', a1)

    # удаляем ранее переименованные товары
    db.delete_renamed_goods()
    print('Переименованные товары удалены')

    # ШАГ 4 вносим новые товары в market_main
    b = db.bd_update(a)

    # ШАГ 5 вносим изменения в market_main
    # Шаг 5.1 создаем словарь old_price куда записывам название товара и его цену из market_main
    old_price = db.select_name_and_price()
    old_price_G = copy.deepcopy(old_price)
    ''' Тут заканчивается 1 автоматическая часть'''

    # Вызываем GUI
    GUI.gui_start()
    # Шаг 5.2 Через интерфейс вносим измениния в count_goods( меняем количество единиц товара в товаре(n1, n2 и т.д.))
    # ШАГ 5.3 Через интерфейс вносим изменения в таблицу price.
    finish()


if __name__ == "__main__":
    main()
