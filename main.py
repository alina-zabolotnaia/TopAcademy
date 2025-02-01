#################################################################
# author: alina.zabolotnaia@gmail.com
import home_work_1, home_work_2

if __name__ == '__main__':
    print('- - - - - - - - - - - - - HOME WORK #1 - - - - - - - - - - - - - ')
    v_distance = float(input('Введите значение расстояния (км): '))
    v_time = float(input('Введите затраченное время в пути (часы): '))
    print(f'Расчетная скорость движения = {home_work_1.get_speed(v_distance, v_time)} км/ч')

    print('\n- - - - - - - - - - - - - HOME WORK #2 - - - - - - - - - - - - - ')
    print(f'Вызываем метод расчета miles to km {home_work_2.miles_to_km_converter()}')
