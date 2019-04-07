from microbit import *
import radio

PWMA = pin8
AIN1 = pin13
AIN2 = pin12
PWMB = pin16
BIN1 = pin14
BIN2 = pin15

radio.on()

while(True):
    msg = radio.receive()
    if msg:
        tokens = list()
        for token in msg.split():
            tokens.append(int(token))

        AIN1.write_digital(tokens[0])
        AIN2.write_digital(tokens[1])

        BIN1.write_digital(tokens[2])
        BIN2.write_digital(tokens[3])

        PWMA.write_analog(tokens[4])
        PWMB.write_analog(tokens[5])
