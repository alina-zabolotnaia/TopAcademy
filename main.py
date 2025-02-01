#################################################################
# author: alina.zabolotnaia@gmail.com
import homework_1, homework_2

if __name__ == '__main__':
    print('- - - - - - - - - - - - - HOMEWORK #1 - - - - - - - - - - - - - ')
    v_distance = float(input('Введите значение расстояния (км): '))
    v_time = float(input('Введите затраченное время в пути (часы): '))
    print(f'Расчетная скорость движения = {homework_1.get_speed(v_distance, v_time)} км/ч')

    print('\n- - - - - - - - - - - - - HOMEWORK #2 - - - - - - - - - - - - - ')
    ## количество раз программа запросит ввести количество миль
    number_of_iterations = 5

    ## счетчик итераций
    iteration_counter = 1

    ## счетчик для расчета среднего значения миль
    avr_miles_distance = 0

    ## счетчик для расчета среднего значения километров
    avr_km_distance = 0

    print(f'Введите количество миль (miles) {number_of_iterations} раз')
    while iteration_counter <= number_of_iterations:
        v_miles_distance = int(input(f'\n[Шаг №{iteration_counter}] введите количество миль (miles): '))
        v_km_distance = homework_2.miles_to_km_converter(v_miles_distance)
        print(f'Количество километров в {v_miles_distance} милях = {v_km_distance} (км.)')

        avr_miles_distance += v_miles_distance
        avr_km_distance += v_km_distance
        iteration_counter += 1

    print('\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    print(f'Среднее значение для "количества миль": {float(avr_miles_distance/number_of_iterations)}')
    print(f'Среднее значение для "количества км. ": {float(avr_km_distance/number_of_iterations)}')
