from tkinter import *
from tkinter import ttk

from data_func import func_modul_1
from my import App


def command_print():

    global run_man
    global frame_5
    speed_car = float(text_speed_car.get())
    speed_man = float(text_speed_man.get())
    t_1 = float(text_t_1.get())
    t_2 = float(text_t_2.get())
    t_3 = float(text_t_3.get())
    car_deceleration = float(text_car_deceleration.get())
    length_car = float(text_length_car.get())
    width_car = float(text_width_car.get())
    distance_from_site = float(text_distance_from_site.get())
    l_up = float(text_l_up.get())
    distance_car = float(text_distance_car.get())
    distance_man = float(text_distance_man.get())
    alfa = float(text_alfa.get())
    if run_man.get() == modul_1:
        result = func_modul_1(speed_car=speed_car, speed_man=speed_man, t_1=t_1, t_2=t_2, t_3=t_3,
                              car_deceleration=car_deceleration, length_car=length_car,
                              width_car=width_car, distance_from_site=distance_from_site, l_up=l_up,
                              distance_car=distance_car, distance_man=distance_man, alfa=alfa)
    elif run_man.get() == modul_2:
        pass
    answer_lbl = ttk.Label(master=frame_4, text=result[0], background="red")
    answer_lbl.grid(column=0, row=0, sticky="we")
    colums = ("time", "Sa", "Xi", "Yi", "l_up")
    tree = ttk.Treeview(master=frame_5, columns=colums, show="headings")
    tree.pack(fill=BOTH, expand=1)
    tree.heading("time", text="Ti")
    tree.heading("Sa", text="Sa")
    tree.heading("Xi", text="ΔXi")
    tree.heading("Yi", text="ΔYi")
    tree.heading("l_up", text="lуп")

    tree.column("#1", stretch=NO, width=70)
    tree.column("#2", stretch=NO, width=70)
    tree.column("#3", stretch=NO, width=70)
    tree.column("#4", stretch=NO, width=70)
    tree.column("#5", stretch=NO, width=70)

    value = zip(result[1], result[2], result[3], result[4], result[5])
    for i in value:
        tree.insert('', END, values=i)


window = Tk()
window.title("Приложение DTP-Expert (альфа-версия)")
window.geometry("1024x640")


frame_1 = ttk.Frame(relief=SUNKEN, borderwidth=5)
new_data = ttk.Label(master=frame_1, text="Исходные данные:")
new_data.grid(column=1, row=0)

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

lbl_t_1 = ttk.Label(master=frame_1, text="Время реакции водителя в данной дорожной ситуации, с")
lbl_t_1.grid(column=0, row=3)
symbol_t_1 = ttk.Label(master=frame_1, text="t1")
symbol_t_1.grid(column=1, row=3)
text_t_1 = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_t_1)
text_t_1.grid(column=2, row=3)

lbl_t_2 = ttk.Label(master=frame_1, text="Время запаздывания срабатывания тормозного привода автомобиля, с")
lbl_t_2.grid(column=0, row=4)
symbol_t_2 = ttk.Label(master=frame_1, text="t2")
symbol_t_2.grid(column=1, row=4)
text_t_2 = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_t_2)
text_t_2.grid(column=2, row=4)

lbl_t_3 = ttk.Label(master=frame_1, text="Время нарастания замедления автомобиля, с")
lbl_t_3.grid(column=0, row=5)
symbol_t_3 = ttk.Label(master=frame_1, text="t3")
symbol_t_3.grid(column=1, row=5)
text_t_3 = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300, textvariable=spinbox_var_t_3)
text_t_3.grid(column=2, row=5)

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

frame_3 = ttk.Frame(relief=SUNKEN, borderwidth=5)
btn_start = ttk.Button(master=frame_2, text="Расчет", command=command_print)
btn_start.grid(column=0, row=3, sticky=N)

frame_4 = ttk.Frame(relief=SUNKEN, borderwidth=5)
frame_5 = ttk.Frame(relief=SUNKEN, borderwidth=5)
# image_grafik = tkinter.Canvas(master=frame_4, bg='white', height=384, width=512)
# img_1 = tkinter.PhotoImage(file="new_figure.png")
# img_2 = tkinter.PhotoImage(file="saved_figure.png")
# image = image_grafik.create_image(0, 0, anchor="nw", image=img_1)
# image_grafik.grid(column=0, row=1, sticky="we")


frame_1.grid(column=0, row=0, padx=5, pady=5, sticky=NW)
frame_2.grid(column=1, row=0, padx=5, pady=5, sticky=NW)
frame_3.grid(column=1, row=1, padx=5, pady=5, rowspan=1)
frame_4.grid(column=0, row=1, padx=5, pady=5, sticky='we')
frame_5.grid(column=1, row=1, padx=5, pady=5, sticky='we', rowspan=2)


window.mainloop()
