import time

NUMBER_CARS_TO_PRODUCE = 5
TIME_PAINT_PROCESS = 4
TIME_TIRE_PROCESS = 1
TIME_INTERIOR_PROCESS = 4


def production_line_with_principle():
    print("Se inicia la línea de ensamblaje")
    for current_car in range(NUMBER_CARS_TO_PRODUCE):
        format_process_message(True, 'ensamblaje del carro', current_car)
        paint_process(current_car)
        tire_process(current_car)
        interior_process(current_car)
        format_process_message(False, 'ensamblaje del carro', current_car)
    print("Se finaliza la línea de ensamblaje")


def paint_process(current_car: int):
    format_process_message(True, 'pintura de la carrocería', current_car)
    time.sleep(TIME_PAINT_PROCESS)
    format_process_message(False, 'pintura de la carrocería', current_car)


def tire_process(current_car: int):
    format_process_message(True, 'ensamble de los neumáticos', current_car)
    for current_tire in range(4):
        format_process_message(True, 'Ensamble del neumático {}'.format(str(current_tire + 1)), current_car, '\t')
        time.sleep(TIME_TIRE_PROCESS)
    format_process_message(False, 'ensamble de los neumáticos', current_car)


def interior_process(current_car: int):
    format_process_message(True, 'ensamble del interior', current_car)
    time.sleep(TIME_INTERIOR_PROCESS)
    format_process_message(True, 'ensamble del interior', current_car)


def format_process_message(is_start: bool, process: str, current_car: int, tab=''):
    if is_start:
        print(tab + 'Inicia' + ' proceso de ' + process + ', Carro: ' + str(current_car + 1))
    else:
        print(tab + 'Finaliza' + ' proceso de ' + process + ', Carro: ' + str(current_car + 1))


if __name__ == "__main__":
    production_line_with_principle()
