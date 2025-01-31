#################################################################
# author: alina.zabolotnaia@gmail.com
#

def get_speed(i_distance, i_time):
    print(f'Рассчитаем скорость движения по параметрам:\n')
    print(f'- расстояние (км.)   : {i_distance}')
    print(f'- время в пути (час) : {i_time}')
    return i_distance/i_time


if __name__ == '__main__':
    v_distance = float(input('Введите расстояние:'))
    v_time = float(input('Введите время в пути:'))
    print(f'Скорость движения = {get_speed(v_distance, v_time)} км/ч')
