import tkinter
import os
from tkinter import *
from tkinter import ttk


def click_man_exit():
    os.system('python modul_man_exit.py')


# Создание окна программы
start_window = Tk()
start_window.title("Приложение DTP-Expert (альфа-версия)")
start_window.geometry("1105x720+200+30")

modul_man_exit = ttk.Button(text="Расчет выхода пешехода из полосы движения ТС",
                            command=click_man_exit, padding=(5, 5))
modul_man_exit.pack()
modul_speed = ttk.Button(text="Расчет скорости", padding=(5, 5))
modul_speed.pack()
modul_time = ttk.Button(text="Расчет времени", padding=(5, 5))
modul_time.pack()
modul_distance = ttk.Button(text="Расчет расстояния", padding=(5, 5))
modul_distance.pack()


start_window.mainloop()
