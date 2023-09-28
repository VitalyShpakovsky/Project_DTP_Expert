from tkinter import *
from tkinter import ttk

from data_func import command_exit


window_speed_car = Tk()
window_speed_car.title("Расчет скорости движения ТС с разрывами в следе (альфа-версия)")
window_speed_car.geometry("1105x720+200+30")

frame_1 = ttk.Frame(relief=SUNKEN, borderwidth=5)
new_data = ttk.Label(master=frame_1, text="Исходные данные:")
new_data.grid(column=0, row=0)


spinbox_time_3 = StringVar(value='0.00')
lbl_time_3 = ttk.Label(master=frame_1, text=f"Время нарастания замедления ТС, с")
lbl_time_3.grid(column=0, row=1, sticky='w')
symbol_time_3 = ttk.Label(master=frame_1, text="t3")
symbol_time_3.grid(column=1, row=1)
text_time_3 = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,  textvariable=spinbox_time_3)
text_time_3.grid(column=2, row=1)


spinbox_time_p = StringVar(value='0.00')
lbl_time_p = ttk.Label(master=frame_1, text=f"Время растормаживания ТС, с")
lbl_time_p.grid(column=0, row=2, sticky='w')
symbol_time_p = ttk.Label(master=frame_1, text="tp")
symbol_time_p.grid(column=1, row=2)
text_time_p = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,  textvariable=spinbox_time_p)
text_time_p.grid(column=2, row=2)


spinbox_var_car_deceleration = StringVar(value='0.00')
lbl_car_deceleration = ttk.Label(master=frame_1, text="Замедление автомобиля, м/с^2")
lbl_car_deceleration.grid(column=0, row=3, sticky='w')
symbol_car_deceleration = ttk.Label(master=frame_1, text="j")
symbol_car_deceleration.grid(column=1, row=3)
text_car_deceleration = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                    textvariable=spinbox_var_car_deceleration)
text_car_deceleration.grid(column=2, row=3)


spinbox_car_base = StringVar(value='0.00')
lbl_car_base = ttk.Label(master=frame_1, text=f"База ТС, м")
lbl_car_base.grid(column=0, row=4, sticky='w')
symbol_car_base = ttk.Label(master=frame_1, text="L")
symbol_car_base.grid(column=1, row=4)
text_car_base = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,  textvariable=spinbox_car_base)
text_car_base.grid(column=2, row=4)


spinbox_third_braking_mark = StringVar(value='0.00')
lbl_third_braking_mark = ttk.Label(master=frame_1, text=f"Длина третьего участка следа торможения, м")
lbl_third_braking_mark.grid(column=0, row=5, sticky='w')
symbol_third_braking_mark = ttk.Label(master=frame_1, text="Р3")
symbol_third_braking_mark.grid(column=1, row=5)
text_third_braking_mark = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                      textvariable=spinbox_third_braking_mark)
text_third_braking_mark.grid(column=2, row=5)


spinbox_second_brake_break = StringVar(value='0.00')
lbl_second_brake_break = ttk.Label(master=frame_1, text=f"Длина второго участка разрыва следа торможения, м")
lbl_second_brake_break.grid(column=0, row=6, sticky='w')
symbol_second_brake_break = ttk.Label(master=frame_1, text="R23")
symbol_second_brake_break.grid(column=1, row=6)
text_second_brake_break = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                      textvariable=spinbox_second_brake_break)
text_second_brake_break.grid(column=2, row=6)


spinbox_second_braking_mark = StringVar(value='0.00')
lbl_second_braking_mark = ttk.Label(master=frame_1, text=f"Длина второго участка следа торможения, м")
lbl_second_braking_mark.grid(column=0, row=7, sticky='w')
symbol_second_braking_mark = ttk.Label(master=frame_1, text="Р2")
symbol_second_braking_mark.grid(column=1, row=7)
text_second_braking_mark = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                       textvariable=spinbox_second_braking_mark)
text_second_braking_mark.grid(column=2, row=7)


spinbox_first_brake_break = StringVar(value='0.00')
lbl_first_brake_break = ttk.Label(master=frame_1, text=f"Длина первого участка разрыва следа торможения, м")
lbl_first_brake_break.grid(column=0, row=8, sticky='w')
symbol_first_brake_break = ttk.Label(master=frame_1, text="R12")
symbol_first_brake_break.grid(column=1, row=8)
text_first_brake_break = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                     textvariable=spinbox_first_brake_break)
text_first_brake_break.grid(column=2, row=8)


spinbox_first_braking_mark = StringVar(value='0.00')
lbl_first_braking_mark = ttk.Label(master=frame_1, text=f"Длина первого участка следа торможения, м")
lbl_first_braking_mark.grid(column=0, row=9, sticky='w')
symbol_first_braking_mark = ttk.Label(master=frame_1, text="Р1")
symbol_first_braking_mark.grid(column=1, row=9)
text_first_braking_mark = ttk.Spinbox(master=frame_1, width=10, from_=0.00, to=300,
                                      textvariable=spinbox_first_braking_mark)
text_first_braking_mark.grid(column=2, row=9)


btn_start = ttk.Button(master=frame_1, text="Расчет")
btn_start.grid(column=0, row=10, sticky=N)

btn_stop = ttk.Button(master=frame_1, text="Выход в главное меню", command=command_exit)
btn_stop.grid(column=0, row=11, sticky=N)


frame_1.grid(column=0, row=0, padx=5, pady=5, sticky="nw", columnspan=2)

window_speed_car.mainloop()
