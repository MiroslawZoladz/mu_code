from microbit import *
import random

x = y = 0
X = random.randint(1,4)
Y = random.randint(1,4)
B=[0,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,0]
b=0


while(True):
    display.set_pixel(x , y, 0)
    if button_a.was_pressed():
        x = (x+1)% 5
    if button_b.was_pressed():
        y = (y+1)% 5

    b = (b+1)%20
    display.set_pixel(x , y, 5)
    display.set_pixel(X, Y, B[b])
    if (x == X) and (y == Y):
        for i in range(15):
            display.set_pixel(x, y, 9)
            sleep(70)
            display.set_pixel(x, y, 0)
            sleep(70)
        X = random.randint(1,4)
        Y = random.randint(1,4)

    sleep(100)







