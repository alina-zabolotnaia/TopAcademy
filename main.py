#################################################################
# author: alina.zabolotnaia@gmail.com
import homework_1, homework_2

if __name__ == '__main__':
    print('- - - - - - - - - - - - - HOME WORK #1 - - - - - - - - - - - - - ')
    v_distance = float(input('Введите значение расстояния (км): '))
    v_time = float(input('Введите затраченное время в пути (часы): '))
    print(f'Расчетная скорость движения = {homework_1.get_speed(v_distance, v_time)} км/ч')

    print('\n- - - - - - - - - - - - - HOME WORK #2 - - - - - - - - - - - - - ')
    v_miles_distance = int(input('Введите количество миль (miles): '))
    print(f'Количество километров в {v_miles_distance} милях = {homework_2.miles_to_km_converter(v_miles_distance)} (км.)')
