from math import cos, sin, pi
from matplotlib import pyplot as plt


def func_modul_1(speed_car, speed_man, t_1, t_2, t_3,
            car_deceleration, length_car, width_car,
            distance_from_site, l_up, distance_car, distance_man, alfa):
    print('Модуль 1')
    list_time_i = []
    list_distance_car = []
    list_x_i = []
    list_y_i = []
    list_l_up = []
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
    list_time_i.append(round(time_i, 2))
    list_distance_car.append(round(distance_car_i, 2))
    list_x_i.append(round(x_i, 2))
    list_y_i.append(round(y_i, 2))
    list_l_up.append(l_up)

    # print('time_i =', time_i,
    #       'speed_car_i = ', speed_car_i,
    #       'speed_man_i = ', speed_man,
    #       'distance_car_i = ', distance_car_i,
    #       'distance_man_i = ', distance_man_i,
    #       'x_i = ', x_i,
    #       'y_i = ', y_i,
    #       'l_up = ', l_up,
    #       'y_i - l_up = ', y_i - l_up)
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
        # print(x_i)
        y_i = y_0 + (distance_man_i * sin((alfa * pi) / 180))

        # print('time_i =', time_i,
        #       'speed_car_i = ', speed_car_i,
        #       'speed_man_i = ', speed_man,
        #       'distance_car_i = ', distance_car_i,
        #       'distance_man_i = ', distance_man_i,
        #       'x_i = ', x_i,
        #       'y_i = ', y_i,
        #       'l_up = ', l_up,
        #       'y_i - l_up = ', y_i - l_up)
        list_time_i.append(round(time_i, 2))
        list_distance_car.append(round(distance_car_i, 2))
        list_x_i.append(round(x_i, 2))
        list_y_i.append(round(y_i, 2))
        list_l_up.append(l_up)
    if (speed_car_i < 0) and (round(x_i, 2) > 0):
        # print(list_time_i)
        # plt.plot(list_time_i, list_x_i, "g-o")
        plt.plot([2, 4, 6, 8, 10], "g-o")
        # plt.plot(list_time_i, list_y_i)
        # plt.plot(list_time_i, list_distance_car)
        # plt.plot(list_time_i, l_up)
        # plt.show()
        return "Водитель автомобиля имел техническую возможность предотвратить наезд на пешехода."
    else:
        if round(x_i, 2) <= 0 and y_i > l_up:
            plt.plot(list_time_i, list_x_i)
            # plt.plot(list_time_i, list_y_i)
            # plt.plot(list_time_i, list_distance_car)
            # plt.plot(list_time_i, l_up)
            plt.show()
            return f"Водитель автомобиля не имел техническую возможность предотвратить наезд на пешехода," \
                   f" однако при своевременном применение водителем мер к торможению " \
                   f"пешеход успевал покинуть полосу движения автомобиля."
        else:
            plt.plot(list_time_i, list_x_i, label="Хi")
            plt.plot(list_time_i, list_y_i, label="Yi")
            plt.plot(list_time_i, list_distance_car, label="Sa")
            plt.plot(list_time_i, list_l_up, label="lуп")
            plt.xlabel("Время, с")
            plt.ylabel("Расстояние, м")
            plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),
                       ncols=4, mode="expand", borderaxespad=0.)

            plt.savefig('saved_figure.png', dpi=80)
            plt.clf()
            result = ["Водитель автомобиля не имел техническую возможность предотвратить наезд на пешехода",
                      list_time_i, list_distance_car,
                      list_x_i, list_y_i, list_l_up]
            return result


# func_modul_1(speed_car=60, speed_man=7, t_1=0.6, t_2=0.2, t_3=0.4,
#                               car_deceleration=5, length_car=4,
#                               width_car=1.7, distance_from_site=1, l_up=1,
#                               distance_car=30, distance_man=5, alfa=80)