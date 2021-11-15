import time
from threading import Thread

def car_1(speed, pilot):
    route = 0
    while route <= 500:
        print(f'The {pilot} is in {route} miles...')
        route += speed
        time.sleep(0.5)
    print(f'    End for {pilot}...')

if __name__ == "__main__":
    
    t_car_1 = Thread(target=car_1, args=[25, 'Michaek Schumacher'])
    t_car_2 = Thread(target=car_1, args=[20, 'Rubinho Barrichello'])
    t_car_3 = Thread(target=car_1, args=[50, 'Airton Senna'])

    t_car_1.start()
    t_car_2.start()
    t_car_3.start()
