#################################################################
# author: alina.zabolotnaia@gmail.com
import home_work_1

if __name__ == '__main__':
    print('- - - - - - - - - - - - - HOME WORK #1 - - - - - - - - - - - - - ')
    v_distance = float(input('Введите расстояние:'))
    v_time = float(input('Введите время в пути:'))
    print(f'Скорость движения = {home_work_1.get_speed(v_distance, v_time)} км/ч')
