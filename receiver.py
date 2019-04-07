from microbit import *
import radio

Dir = [
    'forward',
    'backward',
]

class Motor():
    def __init__(self):
        self.PWMA = pin8
        self.AIN1 = pin13
        self.AIN2 = pin12
        self.PWMB = pin16
        self.BIN1 = pin14
        self.BIN2 = pin15
        self.S0 = pin0
        self.S1 = pin1
        self.S2 = pin2
        self.S0.set_analog_period(20)
        self.S1.set_analog_period(20)
        self.S2.set_analog_period(20)

    def MotorRun(self, motor, index, speed):
        if(speed > 16):
            return
        speed = speed * 64 - 1

        if(motor == 0):
            self.PWMA.write_analog(speed)
            if(index == Dir[0]):
                self.AIN1.write_digital(0)
                self.AIN2.write_digital(1)
            else:
                self.AIN1.write_digital(1)
                self.AIN2.write_digital(0)
        else:
            self.PWMB.write_analog(speed)
            if(index == Dir[0]):
                self.BIN1.write_digital(0)
                self.BIN2.write_digital(1)
            else:
                self.BIN1.write_digital(1)
                self.BIN2.write_digital(0)

    def MotorStop(self, motor):
        if (motor == 0):
            self.PWMA.write_analog(0)
        else:
            self.PWMB.write_analog(0)

Motor = Motor()
radio.on()

speed = 12

while(True):
    msg = radio.receive()
    if msg is None:
        pass
    elif msg == '-':
        Motor.MotorStop(0)
        Motor.MotorStop(1)
    elif msg == 'up':
        Motor.MotorRun(0, 'forward', speed)
        Motor.MotorRun(1, 'forward', speed)
    elif msg == 'down':
        Motor.MotorRun(0, 'backward', speed)
        Motor.MotorRun(1, 'backward', speed)
    elif msg == 'right':
        Motor.MotorRun(1, 'forward', speed)
    elif msg == 'left':
        Motor.MotorRun(0, 'forward', speed)

# display.clear()
# display.set_pixel(key_2_led[msg], 0, 9)