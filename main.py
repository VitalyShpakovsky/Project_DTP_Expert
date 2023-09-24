from math import cos, sin, pi


def modul_1():
    print('Модуль 1')

    # Исходные данные

    speed_car = round(float(input("Введите скорость автомобиля, км/ч ")), 2)  # скорость движения автомобиля
    speed_man = round(float(input("Введите скорость пешехода, км/ч ")), 2)  # скорость движения пешехода
    t_1 = round(float(input("Введите время реакции водителя, с ")), 2)  # время реакции водителя
    t_2 = round(float(input("Введите время запаздывания срабатывания тормозного привода автомобиля, с ")), 2)  # время запаздывания срабатывания тормозного привода автомобиля
    t_3 = round(float(input("Введите время нарастания замедления автомобиля, с ")), 2)  # время нарастания замедления автомобиля
    car_deceleration = round(float(input("Введите замедление автомобиля, м/с^2 ")), 2)  # замедление автомобиля
    length_car = round(float(input("Введите габаритную длину автомобиля, м ")), 2)
    width_car = round(float(input("Введите габаритную ширину автомобиля, м ")), 2)
    distance_from_site = round(float(input("Введите удаления места наезда от боковой поверхности автомобиля, м ")), 2)
    l_up = round(float(input("Введите поперечный размер пространства, занимаемого движущимся пешеходом, м ")), 2)
    distance_car = round(float(input("Введите удаления автомобиля от места наезда в  МВО, м ")), 2)
    distance_man = round(float(input("Введите  путь пройденный пешеходом с МВО до момента наезда, м ")), 2)
    alfa = round(float(input("Введите угол под которым пешеход пересекает полосу движения автомобиля, град ")), 2)

    # Расчетные исходные данные
    time_break = (t_1 + t_2 + (0.5 * t_3))
    time_stop_car = round((t_1 + t_2 + (0.5 * t_3)) + ((speed_car / 3.6) / car_deceleration), 8)
    print(time_stop_car)
    x_0 = round(distance_car - (distance_man * cos((alfa * pi) / 180)), 8)
    print(x_0)
    y_0 = round(-((distance_man * sin((alfa * pi) / 180)) + distance_from_site), 8)
    print(y_0)

    # Расчет
    time_i = 0
    distance_car_i = 0
    distance_man_i = 0
    speed_car_i = speed_car
    x_i = x_0
    y_i = y_0
    print('time_i =', time_i,
          'speed_car_i = ', speed_car_i,
          'speed_man_i = ', speed_man,
          'distance_car_i = ', distance_car_i,
          'distance_man_i = ', distance_man_i,
          'x_i = ', x_i,
          'y_i = ', y_i,
          'l_up = ', l_up,
          'y_i - l_up = ', y_i - l_up)
    while (x_i > 0) and (speed_car_i > 0):
        time_i = round((time_i + 0.01), 2)
        if time_i <= time_break:
            speed_car_i = speed_car
            distance_car_i = (speed_car_i / 3.6) * time_i
        else:
            speed_car_i = speed_car - (3.6 * car_deceleration * (time_i - time_break))
            distance_car_i = ((speed_car / 3.6) * time_break) + ((speed_car ** 2 - speed_car_i ** 2) / (25.92 * car_deceleration))
        distance_man_i = (speed_man / 3.6) * time_i
        x_i = (x_0 + distance_man_i * cos((alfa * pi) / 180)) - distance_car_i
        print(x_i)
        y_i = y_0 + (distance_man_i * sin((alfa * pi) / 180))
        print('time_i =', time_i,
              'speed_car_i = ', speed_car_i,
              'speed_man_i = ', speed_man,
              'distance_car_i = ', distance_car_i,
              'distance_man_i = ', distance_man_i,
              'x_i = ', x_i,
              'y_i = ', y_i,
              'l_up = ', l_up,
              'y_i - l_up = ', y_i - l_up)
    if (speed_car_i < 0) and (round(x_i, 2) > 0):
        print("Водитель автомобиля имел техническую возможность предотвратить наезд на пешехода.")
    else:
        if round(x_i, 2) <= 0 and y_i > l_up:
            print("Водитель автомобиля не имел техническую возможность предотвратить наезд на пешехода, "
                  "однако при своевременном применение водителем мер к торможению пешеход успевал покинуть "
                  "полосу движения автомобиля.")
        else:
            print('Водитель автомобиля не имел техническую возможность предотвратить наезд на пешехода')


def modul_2():
    print('Модуль 2')


print("Program DTP-Expert")
menu = input("Введите 1 - если пешеход удаляется, 2 - если пешеход приближается, 3 - для выхода из программы ")
while menu != '3':
    if menu == '1':
        modul_1()
        break
    elif menu == '2':
        modul_2()
        break
    else:
        print('Неправильный ввод. Попробуйте еще раз')
        menu = input("Введите 1 - если пешеход удаляется, 2 - если пешеход приближается, 3 - для выхода из программы ")
else:
    print('Программа завершена')
