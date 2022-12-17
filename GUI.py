from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

import main
from get_group_dict import change_VK_price
from get_group_dict import my_owner_group_id

from main import old_price_G
from main import backup_dict_G
from main import backup_dict_id_G

db = sqlite3.connect('server.db')
sql = db.cursor()

def read_names():
    """ Возвращает имена из таблицы names"""
    sql.execute('''SELECT p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15 FROM names WHERE id = 1''')
    res = sql.fetchall()
    return res

def show_name():
    """ Возвращает список имен из таблицы market_main"""
    sql.execute('''SELECT item_name FROM market_main''')
    list0 = sql.fetchall()
    list = []
    for i in list0:
        list.append(i[0])
    return list

def read_p_names():
    """ Вставляет имена из таблицы names при нажатии на кнопку 'показать имена' """
    clear3()
    sql.execute('''SELECT p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15 FROM names WHERE id=1''')
    names_res = sql.fetchall()[0]
    n1 = names_res[0]
    n2 = names_res[1]
    n3 = names_res[2]
    n4 = names_res[3]
    n5 = names_res[4]
    n6 = names_res[5]
    n7 = names_res[6]
    n8 = names_res[7]
    n9 = names_res[8]
    n10 = names_res[9]
    n11 = names_res[10]
    n12 = names_res[11]
    n13 = names_res[12]
    n14 = names_res[13]
    n15 = names_res[14]
    names_n1.insert(1, n1)
    names_n2.insert(1, n2)
    names_n3.insert(1, n3)
    names_n4.insert(1, n4)
    names_n5.insert(1, n5)
    names_n6.insert(1, n6)
    names_n7.insert(1, n7)
    names_n8.insert(1, n8)
    names_n9.insert(1, n9)
    names_n10.insert(1, n10)
    names_n11.insert(1, n11)
    names_n12.insert(1, n12)
    names_n13.insert(1, n13)
    names_n14.insert(1, n14)
    names_n15.insert(1, n15)


def read_p_price():
    """ Вставляет цены при нажатии на кнопку 'показать цены' """
    clear2()
    sql.execute('''SELECT p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15 FROM price WHERE id=1''')
    price_res = sql.fetchall()[0]
    pp1 = price_res[0]
    pp2 = price_res[1]
    pp3 = price_res[2]
    pp4 = price_res[3]
    pp5 = price_res[4]
    pp6 = price_res[5]
    pp7 = price_res[6]
    pp8 = price_res[7]
    pp9 = price_res[8]
    pp10 = price_res[9]
    pp11 = price_res[10]
    pp12 = price_res[11]
    pp13 = price_res[12]
    pp14 = price_res[13]
    pp15 = price_res[14]
    p1.insert(1, pp1)
    p2.insert(1, pp2)
    p3.insert(1, pp3)
    p4.insert(1, pp4)
    p5.insert(1, pp5)
    p6.insert(1, pp6)
    p7.insert(1, pp7)
    p8.insert(1, pp8)
    p9.insert(1, pp9)
    p10.insert(1, pp10)
    p11.insert(1, pp11)
    p12.insert(1, pp12)
    p13.insert(1, pp13)
    p14.insert(1, pp14)
    p15.insert(1, pp15)


def save_p_price():
    """ При нажатии на кнопку 'сохранить цены'
    считывает цены из форм ввода p1-p15 и сохраняет значения в таблице price """
    sql.execute(
        f'''UPDATE price SET (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15) = 
        ({p1.get()}, {p2.get()}, {p3.get()}, {p4.get()}, {p5.get()}, {p6.get()}, {p7.get()}, {p8.get()},
        {p9.get()}, {p10.get()}, {p11.get()}, {p12.get()}, {p13.get()}, {p14.get()}, {p15.get()} ) WHERE id = 1''')
    db.commit()
    label_fr2_price_info['text'] = 'Цены сохранены'
    sql.execute('''select * from price''')
    ddd = sql.fetchall()
    print(ddd)

def save_p_names():
    """ При нажатии на кнопку 'Сохранить имена'
    считывает значения с форм ввода names_n1-names_n15 и сохраняет их в таблице names """
    sql.execute(
        f'''UPDATE names SET (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15) = 
        ("{names_n1.get()}", "{names_n2.get()}", "{names_n3.get()}", "{names_n4.get()}", "{names_n5.get()}", "{names_n6.get()}", "{names_n7.get()}", "{names_n8.get()}",
        "{names_n9.get()}", "{names_n10.get()}", "{names_n11.get()}", "{names_n12.get()}", "{names_n13.get()}", "{names_n14.get()}", "{names_n15.get()}" ) WHERE id = 1''')
    db.commit()
    label_fr3_price_info['text'] = 'Имена сохранены'

def backup_p_names():
    """ При нажатии на кнопку 'вернуть как было'
     возвращает значения имен по умолчанию"""
    sql.execute(
        f'''UPDATE names SET (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15) = 
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ) WHERE id = 1''')
    db.commit()
    label_fr3_price_info['text'] = 'Имена по умолчанию'


def check_count(name):
    """Возвращает кортеж из count_goods. Если его не существует, возвращает имя и нули"""
    sql.execute(f'''SELECT * FROM count_goods WHERE item_name ="{name}"''')
    res = sql.fetchone()
    if res == None:
        return (name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        return res


def btn_click():
    """При нажатии кнопки "сохранить" считывает значения из n-форм и записывает их в БД count_goods"""
    for i in lb.curselection():
        selection = lb.get(i)
    sql.execute('''SELECT item_name FROM count_goods WHERE item_name="{0}"'''.format(selection))
    res = sql.fetchone()
    # если значение уже есть в бд - делает апдейт, если нет - вставляет
    if res == None:
        sql.execute(
            '''INSERT INTO count_goods (item_name, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15)
             VALUES ("{0}", {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15});'''.format(
                selection, n1.get(), n2.get(), n3.get(), n4.get(), n5.get(), n6.get(), n7.get(), n8.get(), n9.get(),
                n10.get(), n11.get(), n12.get(), n13.get(), n14.get(), n15.get())
        )
        db.commit()
        msg_label['text'] = selection + ' сохранен'
    else:
        sql.execute(
            '''UPDATE count_goods SET (item_name, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15)
             = ("{0}", {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}) where item_name="{0}";'''.format(
                selection, n1.get(), n2.get(), n3.get(), n4.get(), n5.get(), n6.get(), n7.get(), n8.get(), n9.get(),
                n10.get(), n11.get(), n12.get(), n13.get(), n14.get(), n15.get())
        )
        db.commit()
        msg_label['text'] = selection + ' обновлен'

def clear():
    """ Очищает формы ввода n1-n15 на вкладке 1"""
    n1.delete(0, END)
    n2.delete(0, END)
    n3.delete(0, END)
    n4.delete(0, END)
    n5.delete(0, END)
    n6.delete(0, END)
    n7.delete(0, END)
    n8.delete(0, END)
    n9.delete(0, END)
    n10.delete(0, END)
    n11.delete(0, END)
    n12.delete(0, END)
    n13.delete(0, END)
    n14.delete(0, END)
    n15.delete(0, END)


def clear2():
    """ Очищает формы ввода p1-p15 на вкладке 2"""
    p1.delete(0, END)
    p2.delete(0, END)
    p3.delete(0, END)
    p4.delete(0, END)
    p5.delete(0, END)
    p6.delete(0, END)
    p7.delete(0, END)
    p8.delete(0, END)
    p9.delete(0, END)
    p10.delete(0, END)
    p11.delete(0, END)
    p12.delete(0, END)
    p13.delete(0, END)
    p14.delete(0, END)
    p15.delete(0, END)

def clear3():
    """ Очищает формы ввода names_n1-names_n15 на вкладке 3"""
    names_n1.delete(0, END)
    names_n2.delete(0, END)
    names_n3.delete(0, END)
    names_n4.delete(0, END)
    names_n5.delete(0, END)
    names_n6.delete(0, END)
    names_n7.delete(0, END)
    names_n8.delete(0, END)
    names_n9.delete(0, END)
    names_n10.delete(0, END)
    names_n11.delete(0, END)
    names_n12.delete(0, END)
    names_n13.delete(0, END)
    names_n14.delete(0, END)
    names_n15.delete(0, END)

def onSelect(val):
    """ При выборе товара из списка
     выводит его название, значение количества едениц n1-n15 в этом товаре и расчитывает цену товара"""

    clear()
    for i in lb.curselection():
        selection = lb.get(i)
        res = check_count(selection)
        goods_label['text'] = selection
        n1.insert(1, res[1])
        n2.insert(1, res[2])
        n3.insert(1, res[3])
        n4.insert(1, res[4])
        n5.insert(1, res[5])
        n6.insert(1, res[6])
        n7.insert(1, res[7])
        n8.insert(1, res[8])
        n9.insert(1, res[9])
        n10.insert(1, res[10])
        n11.insert(1, res[11])
        n12.insert(1, res[12])
        n13.insert(1, res[13])
        n14.insert(1, res[14])
        n15.insert(1, res[15])
    """Считываем значения из таблицы price чтобы вычислить цену конкретного товара"""
    sql.execute('''SELECT p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15 FROM price WHERE id=1''')
    price_res = sql.fetchall()[0]
    price = res[1] * price_res[0] + res[2] * price_res[1] + res[3] * price_res[2] + res[4] * price_res[3] + res[5] * \
            price_res[4] + res[6] * price_res[5] + res[7] * price_res[6] + res[8] * price_res[7] + res[9] * price_res[
                8] + res[10] * price_res[9] + res[11] * price_res[10] + res[12] * price_res[11] + res[13] * price_res[
                12] + res[14] * price_res[13] + res[15] * price_res[14]
    price_label['text'] = price

def gui_start():
    """ Запускает графический интерфейс"""

    frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame2.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame3.place(relx=0, rely=0, relwidth=1, relheight=1)

    '''Вкладка 1 "Главная"'''

    lb.place(relx=0.02, rely=0.07)
    btn.place(relx=0.66, rely=0.56, height=25, width=70)
    btn_change_price_vk.place(relx=0.47, rely=0.56, height=25, width=110)
    goods_label.place(relx=0.28, rely=0.06, height=20, width=65)
    msg_label.place(relx=0.61, rely=0.66, height=20, width=135)
    price_text_label.place(relx=0.24, rely=0.12, height=20, width=45)
    price_label.place(relx=0.31, rely=0.12, height=20, width=65)

    n1.place(relx=0.43, rely=0.06, height=20, width=35)
    label_n1.place(relx=0.43, rely=0.01)

    n2.place(relx=0.56, rely=0.06, height=20, width=35)
    label_n2.place(relx=0.56, rely=0.01)

    n3.place(relx=0.69, rely=0.06, height=20, width=35)
    label_n3.place(relx=0.69, rely=0.01)

    n4.place(relx=0.43, rely=0.16, height=20, width=35)
    label_n4.place(relx=0.43, rely=0.11)

    n5.place(relx=0.56, rely=0.16, height=20, width=35)
    label_n5.place(relx=0.56, rely=0.11)

    n6.place(relx=0.69, rely=0.16, height=20, width=35)
    label_n6.place(relx=0.69, rely=0.11)

    n7.place(relx=0.43, rely=0.26, height=20, width=35)
    label_n7.place(relx=0.43, rely=0.21)

    n8.place(relx=0.56, rely=0.26, height=20, width=35)
    label_n8.place(relx=0.56, rely=0.21)

    n9.place(relx=0.69, rely=0.26, height=20, width=35)
    label_n9.place(relx=0.69, rely=0.21)

    n10.place(relx=0.43, rely=0.36, height=20, width=35)
    label_n10.place(relx=0.43, rely=0.31)

    n11.place(relx=0.56, rely=0.36, height=20, width=35)
    label_n11.place(relx=0.56, rely=0.31)

    n12.place(relx=0.69, rely=0.36, height=20, width=35)
    label_n12.place(relx=0.69, rely=0.31)

    n13.place(relx=0.43, rely=0.46, height=20, width=35)
    label_n13.place(relx=0.43, rely=0.41)

    n14.place(relx=0.56, rely=0.46, height=20, width=35)
    label_n14.place(relx=0.56, rely=0.41)

    n15.place(relx=0.69, rely=0.46, height=20, width=35)
    label_n15.place(relx=0.69, rely=0.41)

    '''Вкладка 2 Цены'''

    p1.place(relx=0.18, rely=0.01, height=20, width=41)
    label_p1.place(relx=0.03, rely=0.01)

    p2.place(relx=0.18, rely=0.07, height=20, width=41)
    label_p2.place(relx=0.03, rely=0.07)

    p3.place(relx=0.18, rely=0.13, height=20, width=41)
    label_p3.place(relx=0.03, rely=0.13)

    p4.place(relx=0.18, rely=0.2, height=20, width=41)
    label_p4.place(relx=0.03, rely=0.2)

    p5.place(relx=0.18, rely=0.26, height=20, width=41)
    label_p5.place(relx=0.03, rely=0.26)

    p6.place(relx=0.39, rely=0.01, height=20, width=41)
    label_p6.place(relx=0.26, rely=0.01)

    p7.place(relx=0.39, rely=0.07, height=20, width=41)
    label_p7.place(relx=0.26, rely=0.07)

    p8.place(relx=0.39, rely=0.13, height=20, width=41)
    label_p8.place(relx=0.26, rely=0.13)

    p9.place(relx=0.39, rely=0.19, height=20, width=41)
    label_p9.place(relx=0.26, rely=0.19)

    p10.place(relx=0.39, rely=0.25, height=20, width=41)
    label_p10.place(relx=0.26, rely=0.25)

    p11.place(relx=0.69, rely=0.01, height=20, width=41)
    label_p11.place(relx=0.56, rely=0.01)

    p12.place(relx=0.69, rely=0.07, height=20, width=41)
    label_p12.place(relx=0.56, rely=0.07)

    p13.place(relx=0.69, rely=0.13, height=20, width=41)
    label_p13.place(relx=0.56, rely=0.13)

    p14.place(relx=0.69, rely=0.19, height=20, width=41)
    label_p14.place(relx=0.56, rely=0.19)

    p15.place(relx=0.69, rely=0.25, height=20, width=41)
    label_p15.place(relx=0.56, rely=0.25)

    btn_show_price.place(relx=0.03, rely=0.32, height=25, width=100)
    btn_save_price.place(relx=0.21, rely=0.32, height=25, width=100)

    label_fr2_price_info.place(relx=0.38, rely=0.32, height=25, width=100)

    '''Вкладка 3 Названия'''

    names_n1.place(relx=0.18, rely=0.01, height=20, width=41)
    label_names_n1.place(relx=0.03, rely=0.01)

    names_n2.place(relx=0.18, rely=0.07, height=20, width=41)
    label_names_n2.place(relx=0.03, rely=0.07)

    names_n3.place(relx=0.18, rely=0.13, height=20, width=41)
    label_names_n3.place(relx=0.03, rely=0.13)

    names_n4.place(relx=0.18, rely=0.2, height=20, width=41)
    label_names_n4.place(relx=0.03, rely=0.2)

    names_n5.place(relx=0.18, rely=0.26, height=20, width=41)
    label_names_n5.place(relx=0.03, rely=0.26)

    names_n6.place(relx=0.39, rely=0.01, height=20, width=41)
    label_names_n6.place(relx=0.26, rely=0.01)

    names_n7.place(relx=0.39, rely=0.07, height=20, width=41)
    label_names_n7.place(relx=0.26, rely=0.07)

    names_n8.place(relx=0.39, rely=0.13, height=20, width=41)
    label_names_n8.place(relx=0.26, rely=0.13)

    names_n9.place(relx=0.39, rely=0.19, height=20, width=41)
    label_names_n9.place(relx=0.26, rely=0.19)

    names_n10.place(relx=0.39, rely=0.25, height=20, width=41)
    label_names_n10.place(relx=0.26, rely=0.25)

    names_n11.place(relx=0.69, rely=0.01, height=20, width=41)
    label_names_n11.place(relx=0.56, rely=0.01)

    names_n12.place(relx=0.69, rely=0.07, height=20, width=41)
    label_names_n12.place(relx=0.56, rely=0.07)

    names_n13.place(relx=0.69, rely=0.13, height=20, width=41)
    label_names_n13.place(relx=0.56, rely=0.13)

    names_n14.place(relx=0.69, rely=0.19, height=20, width=41)
    label_names_n14.place(relx=0.56, rely=0.19)

    names_n15.place(relx=0.69, rely=0.25, height=20, width=41)
    label_names_n15.place(relx=0.56, rely=0.25)

    btn_show_names.place(relx=0.03, rely=0.32, height=25, width=100)
    btn_save_names.place(relx=0.21, rely=0.32, height=25, width=105)
    label_fr3_price_info.place(relx=0.44, rely=0.38, height=25, width=125)
    btn_default_names.place(relx=0.44, rely=0.32, height=25, width=120)

    root.mainloop()

def change_VK_prices():
    # main.finish()
    # print(main.old_price)
    # print(main.backup_dict)
    # print(main.backup_dict_id)
    # print(main.final_price_dict)
    # hui()
    # print(main.main().new_price)
    change_VK_price(my_owner_group_id)
    # pass


root = Tk()
root['bg'] = '#fafafa'
root.title('Название программы')
root.geometry('640x480')
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Главная')
tabControl.add(tab2, text='Цены')
tabControl.add(tab3, text='Названия')
tabControl.pack(expand=1, fill=BOTH)

frame = Frame(tab1, bg='#ededed')
frame2 = Frame(tab2, bg='#ededed')
frame3 = Frame(tab3, bg='#ededed')

colum_name = read_names()[0]
print(colum_name)
show_name()
list = show_name()

'''Вкладка 1 "Главная"'''

list_var = Variable(value=list)

lb = Listbox(frame, listvariable=list_var,
             exportselection=False)  # exportselection запрещает снимать выделение со списка

lb.bind('<<ListboxSelect>>', onSelect)
var = StringVar()
var1 = StringVar()
var_price = StringVar()

btn = Button(frame, text='сохранить', bg='white', command=btn_click)
btn_change_price_vk = Button(frame, text='Изменить цены ВК', bg='white', command=main.finish)

goods_label = Label(frame, bg='#fff')

msg_label = Label(frame, bg='#ededed')

price_text_label = Label(frame, text='Цена:')

price_label = Label(frame, text='price')

n1 = Entry(frame, bg='#fff')
label_n1 = Label(frame, text=colum_name[0], bg='#d5e0ed')

n2 = Entry(frame, bg='#fff')
label_n2 = Label(frame, text=colum_name[1], bg='#d5e0ed')

n3 = Entry(frame, bg='#fff')
label_n3 = Label(frame, text=colum_name[2], bg='#d5e0ed')

n4 = Entry(frame, bg='#fff')
label_n4 = Label(frame, text=colum_name[3], bg='#d5e0ed')

n5 = Entry(frame, bg='#fff')
label_n5 = Label(frame, text=colum_name[4], bg='#d5e0ed')

n6 = Entry(frame, bg='#fff')
label_n6 = Label(frame, text=colum_name[5], bg='#d5e0ed')

n7 = Entry(frame, bg='#fff')
label_n7 = Label(frame, text=colum_name[6], bg='#d5e0ed')

n8 = Entry(frame, bg='#fff')
label_n8 = Label(frame, text=colum_name[7], bg='#d5e0ed')

n9 = Entry(frame, bg='#fff')
label_n9 = Label(frame, text=colum_name[8], bg='#d5e0ed')

n10 = Entry(frame, bg='#fff')
label_n10 = Label(frame, text=colum_name[9], bg='#d5e0ed')

n11 = Entry(frame, bg='white')
label_n11 = Label(frame, text=colum_name[10], bg='#d5e0ed')

n12 = Entry(frame, bg='white')
label_n12 = Label(frame, text=colum_name[11], bg='#d5e0ed')

n13 = Entry(frame, bg='white')
label_n13 = Label(frame, text=colum_name[12], bg='#d5e0ed')

n14 = Entry(frame, bg='white')
label_n14 = Label(frame, text=colum_name[13], bg='#d5e0ed')

n15 = Entry(frame, bg='white')
label_n15 = Label(frame, text=colum_name[14], bg='#d5e0ed')

'''Вкладка 2 Цены'''

p1 = Entry(frame2, bg='#fff')
label_p1 = Label(frame2, text=colum_name[0], bg='#d5e0ed')

p2 = Entry(frame2, bg='#fff')
label_p2 = Label(frame2, text=colum_name[1], bg='#d5e0ed')

p3 = Entry(frame2, bg='#fff')
label_p3 = Label(frame2, text=colum_name[2], bg='#d5e0ed')

p4 = Entry(frame2, bg='#fff')
label_p4 = Label(frame2, text=colum_name[3], bg='#d5e0ed')

p5 = Entry(frame2, bg='#fff')
label_p5 = Label(frame2, text=colum_name[4], bg='#d5e0ed')

p6 = Entry(frame2, bg='#fff')
label_p6 = Label(frame2, text=colum_name[5], bg='#d5e0ed')

p7 = Entry(frame2, bg='#fff')
label_p7 = Label(frame2, text=colum_name[6], bg='#d5e0ed')

p8 = Entry(frame2, bg='#fff')
label_p8 = Label(frame2, text=colum_name[7], bg='#d5e0ed')

p9 = Entry(frame2, bg='#fff')
label_p9 = Label(frame2, text=colum_name[8], bg='#d5e0ed')

p10 = Entry(frame2, bg='#fff')
label_p10 = Label(frame2, text=colum_name[9], bg='#d5e0ed')

p11 = Entry(frame2, bg='white')
label_p11 = Label(frame2, text=colum_name[10], bg='#d5e0ed')

p12 = Entry(frame2, bg='white')
label_p12 = Label(frame2, text=colum_name[11], bg='#d5e0ed')

p13 = Entry(frame2, bg='white')
label_p13 = Label(frame2, text=colum_name[12], bg='#d5e0ed')

p14 = Entry(frame2, bg='white')
label_p14 = Label(frame2, text=colum_name[13], bg='#d5e0ed')

p15 = Entry(frame2, bg='white')
label_p15 = Label(frame2, text=colum_name[14], bg='#d5e0ed')

btn_show_price = Button(frame2, text='Показать цены', bg='#fff', command=read_p_price)

btn_save_price = Button(frame2, text='Сохранить цены', bg='#fff', command=save_p_price)

label_fr2_price_info = Label(frame2)

'''Вкладка 3 Названия'''

names_n1 = Entry(frame3, bg='#fff')
label_names_n1 = Label(frame3, text=colum_name[0], bg='#d5e0ed')

names_n2 = Entry(frame3, bg='#fff')
label_names_n2 = Label(frame3, text=colum_name[1], bg='#d5e0ed')

names_n3 = Entry(frame3, bg='#fff')
label_names_n3 = Label(frame3, text=colum_name[2], bg='#d5e0ed')

names_n4 = Entry(frame3, bg='#fff')
label_names_n4 = Label(frame3, text=colum_name[3], bg='#d5e0ed')

names_n5 = Entry(frame3, bg='#fff')
label_names_n5 = Label(frame3, text=colum_name[4], bg='#d5e0ed')

names_n6 = Entry(frame3, bg='#fff')
label_names_n6 = Label(frame3, text=colum_name[5], bg='#d5e0ed')

names_n7 = Entry(frame3, bg='#fff')
label_names_n7 = Label(frame3, text=colum_name[6], bg='#d5e0ed')

names_n8 = Entry(frame3, bg='#fff')
label_names_n8 = Label(frame3, text=colum_name[7], bg='#d5e0ed')

names_n9 = Entry(frame3, bg='#fff')
label_names_n9 = Label(frame3, text=colum_name[8], bg='#d5e0ed')

names_n10 = Entry(frame3, bg='#fff')
label_names_n10 = Label(frame3, text=colum_name[9], bg='#d5e0ed')

names_n11 = Entry(frame3, bg='white')
label_names_n11 = Label(frame3, text=colum_name[10], bg='#d5e0ed')

names_n12 = Entry(frame3, bg='white')
label_names_n12 = Label(frame3, text=colum_name[11], bg='#d5e0ed')

names_n13 = Entry(frame3, bg='white')
label_names_n13 = Label(frame3, text=colum_name[12], bg='#d5e0ed')

names_n14 = Entry(frame3, bg='white')
label_names_n14 = Label(frame3, text=colum_name[13], bg='#d5e0ed')

names_n15 = Entry(frame3, bg='white')
label_names_n15 = Label(frame3, text=colum_name[14], bg='#d5e0ed')

btn_show_names = Button(frame3, text='Показать имена', bg='#fff', command=read_p_names)

btn_save_names = Button(frame3, text='Сохранить имена', bg='#fff', command=save_p_names)

label_fr3_price_info = Label(frame3)

btn_default_names = Button(frame3, text='Вернуть как было', bg='#fff', command=backup_p_names)

