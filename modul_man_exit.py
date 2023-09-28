import tkinter
from tkinter import *
from tkinter import ttk

from data_func import func_modul_1, func_modul_2, command_exit


# Функция расчета наличия/отсутствия технической возможности предотвратить наезд на пешехода
def command_print():

    global run_man
    speed_car = float(text_speed_car.get())
    speed_man = float(text_speed_man.get())
    time_1 = float(text_time_1.get())
    time_2 = float(text_time_2.get())
    time_3 = float(text_time_3.get())
    car_deceleration = float(text_car_deceleration.get())
    length_car = float(text_length_car.get())
    width_car = float(text_width_car.get())
    distance_from_site = float(text_distance_from_site.get())
    l_up = float(text_l_up.get())
    distance_car = float(text_distance_car.get())
    distance_man = float(text_distance_man.get())
    alfa = float(text_alfa.get())
    if run_man.get() == modul_1:
        # Функция расчета тех. возможности когда пешеход удаляется и строит график перемещений
        result = func_modul_1(speed_car=speed_car, speed_man=speed_man, time_1=time_1, time_2=time_2, time_3=time_3,
                              car_deceleration=car_deceleration, length_car=length_car,
                              width_car=width_car, distance_from_site=distance_from_site, l_up=l_up,
                              distance_car=distance_car, distance_man=distance_man, alfa=alfa)
    elif run_man.get() == modul_2:
        # Функция расчета тех. возможности когда пешеход приближается и строит график перемещений
        result = func_modul_2(speed_car=speed_car, speed_man=speed_man, time_1=time_1, time_2=time_2, time_3=time_3,
                              car_deceleration=car_deceleration, length_car=length_car,
                              width_car=width_car, distance_from_site=distance_from_site, l_up=l_up,
                              distance_car=distance_car, distance_man=distance_man, alfa=alfa)
    answer_lbl['text'] = result[0]
    tree.delete(*tree.get_children())
    value = zip(result[1], result[2], result[3], result[4], result[5], result[6])
    for i in value:
        tree.insert('', END, values=i)
    image_plot.delete("all")
    img_2 = tkinter.PhotoImage(file="saved_figure.png")
    image_plot.create_image(0, 0, anchor="nw", image=img_2)
    image_plot.image = img_2


# Создание окна программы
window = Tk()
window.title("Выход пешехода из полосы движения ТС (альфа-версия)")
window.geometry("1105x720+200+30")

# Блок исходных данных
frame_1 = ttk.Frame(relief=SUNKEN, borderwidth=5)
new_data = ttk.Label(master=frame_1, text="Исходные данные:")
new_data.grid(column=1, row=0)

# Установка значений по умолчанию
spinbox_var_speed_car = StringVar(value='0.00')
spinbox_var_speed_man = StringVar(value='0.00')
spinbox_var_t_1 = StringVar(value='0.00')
spinbox_var_t_2 = StringVar(value='0.00')
spinbox_var_t_3 = StringVar(value='0.00')
spinbox_var_car_deceleration = StringVar(value='0.00')
spinbox_var_length_car = StringVar(value='0.00')
spinbox_var_width_car = StringVar(value='0.00')
spinbox_var_distance_from_site = StringVar(value='0.00')
spinbox_var_l_up = StringVar(value='1.00')
spinbox_var_distance_car = StringVar(value='0.00')
spinbox_var_distance_man = StringVar(value='0.00')
spinbox_var_alfa = StringVar(value='0.00')

lbl_speed_car = ttk.Label(master=frame_1, text="Скорость движения ТС в МВО, км/ч")
lbl_speed_car.grid(column=0, row=1)
symbol_speed_car = ttk.Label(master=frame_1, text="Va")
symbol_speed_car.grid(column=1, row=1)
text_speed_car = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_speed_car)
text_speed_car.grid(column=2, row=1)

lbl_speed_man = ttk.Label(master=frame_1, text="Скорость движения пешехода, км/ч")
lbl_speed_man.grid(column=0, row=2)
symbol_speed_man = ttk.Label(master=frame_1, text="Vп")
symbol_speed_man.grid(column=1, row=2)
text_speed_man = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_speed_man)
text_speed_man.grid(column=2, row=2)

lbl_time_1 = ttk.Label(master=frame_1, text="Время реакции водителя в данной дорожной ситуации, с")
lbl_time_1.grid(column=0, row=3)
symbol_time_1 = ttk.Label(master=frame_1, text="t1")
symbol_time_1.grid(column=1, row=3)
text_time_1 = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_t_1)
text_time_1.grid(column=2, row=3)

lbl_time_2 = ttk.Label(master=frame_1, text="Время запаздывания срабатывания тормозного привода автомобиля, с")
lbl_time_2.grid(column=0, row=4)
symbol_time_2 = ttk.Label(master=frame_1, text="t2")
symbol_time_2.grid(column=1, row=4)
text_time_2 = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_t_2)
text_time_2.grid(column=2, row=4)

lbl_time_3 = ttk.Label(master=frame_1, text="Время нарастания замедления автомобиля, с")
lbl_time_3.grid(column=0, row=5)
symbol_time_3 = ttk.Label(master=frame_1, text="t3")
symbol_time_3.grid(column=1, row=5)
text_time_3 = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_t_3)
text_time_3.grid(column=2, row=5)

lbl_car_deceleration = ttk.Label(master=frame_1, text="Замедление автомобиля, м/с^2")
lbl_car_deceleration.grid(column=0, row=6)
symbol_car_deceleration = ttk.Label(master=frame_1, text="j")
symbol_car_deceleration.grid(column=1, row=6)
text_car_deceleration = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                    textvariable=spinbox_var_car_deceleration)
text_car_deceleration.grid(column=2, row=6)

lbl_length_car = ttk.Label(master=frame_1, text="Габаритная длина автомобиля, м")
lbl_length_car.grid(column=0, row=7)
symbol_length_car = ttk.Label(master=frame_1, text="La")
symbol_length_car.grid(column=1, row=7)
text_length_car = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_length_car)
text_length_car.grid(column=2, row=7)

lbl_width_car = ttk.Label(master=frame_1, text="Габаритная ширина автомобиля, м")
lbl_width_car.grid(column=0, row=8)
symbol_width_car = ttk.Label(master=frame_1, text="Ba")
symbol_width_car.grid(column=1, row=8)
text_width_car = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_width_car)
text_width_car.grid(column=2, row=8)

lbl_distance_from_site = ttk.Label(master=frame_1, text="Удаление места наезда от боковой поверхности автомобиля, м")
lbl_distance_from_site.grid(column=0, row=9)
symbol_distance_from_site = ttk.Label(master=frame_1, text="Lya")
symbol_distance_from_site.grid(column=1, row=9)
text_distance_from_site = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                      textvariable=spinbox_var_distance_from_site)
text_distance_from_site.grid(column=2, row=9)

lbl_l_up = ttk.Label(master=frame_1, text="Поперечный размер пространства, занимаемого движущимся пешеходом, м")
lbl_l_up.grid(column=0, row=10)
symbol_l_up = ttk.Label(master=frame_1, text="lyп")
symbol_l_up.grid(column=1, row=10)
text_l_up = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_l_up)
text_l_up.grid(column=2, row=10)

lbl_distance_car = ttk.Label(master=frame_1, text="Удаление автомобиля от места наезда в  МВО, м")
lbl_distance_car.grid(column=0, row=11)
symbol_distance_car = ttk.Label(master=frame_1, text="Sa")
symbol_distance_car.grid(column=1, row=11)
text_distance_car = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_distance_car)
text_distance_car.grid(column=2, row=11)

lbl_distance_man = ttk.Label(master=frame_1, text="Путь пройденный пешеходом с МВО до момента наезда, м")
lbl_distance_man.grid(column=0, row=12)
symbol_distance_man = ttk.Label(master=frame_1, text="Sп")
symbol_distance_man.grid(column=1, row=12)
text_distance_man = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_distance_man)
text_distance_man.grid(column=2, row=12)

lbl_alfa = ttk.Label(master=frame_1, text="Угол под которым пешеход пересекает полосу движения автомобиля, град")
lbl_alfa.grid(column=0, row=13)
symbol_alfa = ttk.Label(master=frame_1, text=f"{chr(945)}")
symbol_alfa.grid(column=1, row=13)
text_alfa = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_alfa)
text_alfa.grid(column=2, row=13)

# Блок выбора направления движения пешехода
frame_2 = ttk.Frame(relief=SUNKEN, borderwidth=5)
lbl_direction_of_movement = ttk.Label(master=frame_2, text="Направление движения пешехода")
lbl_direction_of_movement.grid(column=0, row=0, sticky=N)
run_man = StringVar(value="Не выбрано")
modul_1 = "Пешеход удаляется"
modul_2 = "Пешеход приближается"
btn_1 = ttk.Radiobutton(master=frame_2, text="Пешеход удаляется", value=modul_1, variable=run_man)
btn_2 = ttk.Radiobutton(master=frame_2, text="Пешеход приближается", value=modul_2, variable=run_man)
btn_1.grid(column=0, row=1, sticky=NW)
btn_2.grid(column=0, row=2, sticky=NW)

# Блок кнопки запуска расчета и вывода результате
frame_3 = ttk.Frame(relief=SUNKEN, borderwidth=5)
btn_start = ttk.Button(master=frame_2, text="Расчет", command=command_print)
btn_start.grid(column=0, row=3, sticky=N)
answer_lbl = ttk.Label(master=frame_2, text='Здесь будет результат расчета', foreground="red", width=73,
                       wraplength=200, anchor='center', justify=CENTER)
answer_lbl.grid(column=0, row=4, sticky="we")

# Блок вывода построенного графика перемещений
frame_4 = ttk.Frame(relief=SUNKEN, borderwidth=5)
image_plot = tkinter.Canvas(master=frame_4, bg='white', height=384, width=512)
image_plot.pack()

# Блок вывода таблицы исходных данных на основании которых построен график
frame_5 = ttk.Frame(relief=SUNKEN, borderwidth=5)
# определяем столбцы
columns = ("time", "speed", "Sa", "Xi", "Yi", "l_up")
# Создаем таблицу вывода данных расчета
tree = ttk.Treeview(master=frame_5, columns=columns, show="headings")
tree.grid(column=0, row=0, sticky="nsew")

# определяем заголовки
tree.heading("time", text="Ti")
tree.heading("speed", text="Va")
tree.heading("Sa", text="Sa")
tree.heading("Xi", text="ΔXi")
tree.heading("Yi", text="ΔYi")
tree.heading("l_up", text="lуп")

tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=70)
tree.column("#3", stretch=NO, width=70)
tree.column("#4", stretch=NO, width=70)
tree.column("#5", stretch=NO, width=70)
tree.column("#6", stretch=NO, width=70)

# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(master=frame_5, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")

btn_stop = ttk.Button(master=frame_5, text="Выход в главное меню", command=command_exit)
btn_stop.grid(column=0, row=1, sticky=N)


# Компоновка блоков в окне
frame_1.grid(column=0, row=0, padx=5, pady=5, sticky='nw')
frame_2.grid(column=1, row=0, padx=5, pady=5, sticky='nswe')
frame_3.grid(column=1, row=1, padx=5, pady=5, sticky='nswe')
frame_4.grid(column=0, row=1, padx=5, pady=5, sticky='we')
frame_5.grid(column=1, row=1, padx=5, pady=5, sticky='nw', rowspan=2)

window.mainloop()
