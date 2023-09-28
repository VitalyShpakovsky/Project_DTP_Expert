from tkinter import *
from tkinter import ttk

from data_func import click_man_exit, click_speed_car


# Создание окна программы
start_window = Tk()
start_window.title("Приложение DTP-Expert (альфа-версия)")
start_window.geometry("1105x720+200+30")

modul_man_exit = ttk.Button(text="Расчет выхода пешехода из полосы движения ТС",
                            command=click_man_exit, padding=(5, 5))
modul_man_exit.pack()
modul_speed = ttk.Button(text="Расчет скорости с разрывами в следе", command=click_speed_car, padding=(5, 5))
modul_speed.pack()


start_window.mainloop()
