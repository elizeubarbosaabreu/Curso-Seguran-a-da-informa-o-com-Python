import time
from threading import Thread

def car_1(speed):
    route = 0
    while route <= 100:
        print(f'The <car number 1> is in {route} Km...')
        route += speed
        time.sleep(1)
    print('    End for <car number 1>')
        
def car_2(speed):
    route = 0
    while route <= 100:
        print(f'The <car number 2> is in {route} Km...')
        route += speed
        time.sleep(1)
    print('    End for <car number 2>')

# car_1(10)
# car_2(25)

t_car_1 = Thread(target=car_1, args=[15])
t_car_2 = Thread(target=car_2, args=[25])

t_car_1.start()
t_car_2.start()
        