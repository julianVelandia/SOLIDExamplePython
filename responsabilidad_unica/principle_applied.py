import time

NUMBER_CARS_TO_PRODUCE = 5
TIME_PAINT_PROCESS = 4
TIME_TIRE_PROCESS = 1
TIME_INTERIOR_PROCESS = 4


def production_line():
    print("Se inicia la línea de ensamblaje")
    for current_car in range(NUMBER_CARS_TO_PRODUCE):
        print("Se inicia le ensamblaje del carro: {}".format(str(current_car + 1)))
        print("Inicia proceso de pintura de la carrocería, Carro: {}".format(str(current_car + 1)))
        time.sleep(TIME_PAINT_PROCESS)
        print("Finaliza proceso de pintura de la carrocería, Carro: {}".format(str(current_car + 1)))
        print("Inicia proceso de ensamble de los neumáticos, Carro: {}".format(str(current_car + 1)))
        for current_tire in range(4):
            print("\t Ensamble del neumático {}, del Carro: {}".format(str(current_tire + 1), str(current_car + 1)))
            time.sleep(TIME_TIRE_PROCESS)
        print("Finaliza proceso de ensamble de los neumáticos, Carro: {}".format(str(current_car + 1)))

        print("Inicia proceso de ensamble del interior, Carro: {}".format(str(current_car + 1)))
        time.sleep(TIME_INTERIOR_PROCESS)
        print("Finaliza proceso de ensamble del interior, Carro: {}".format(str(current_car + 1)))
        print("Se finaliza le ensamblaje del carro: {}".format(str(current_car + 1)))




if __name__ == "__main__":
    production_line()
