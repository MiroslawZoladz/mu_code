from microbit import *
import radio

    # '0 1 0 1 700 715': pin1, #f
    # '1 0 1 0 700 720': pin2, #b
    # '0 1 1 0 550 550': pin5, #r
    # '1 0 0 1 550 550': pin0  #l

pins_ = {
    '0 1 0 1 540 550': pin1, #f
    '1 0 1 0 550 550': pin2, #b
    '0 1 0 0 500 500': pin5, #r
    '0 0 0 1 500 500': pin0  #l
}

radio.on()

for k in pins_:
    pins_[k].set_pull(pin0.PULL_UP)

while(True):
    for k in pins_:
        if not pins_[k].read_digital():
            radio.send(k)
            break
    else:
        radio.send('0 0 0 0 0 0')

    sleep(100)