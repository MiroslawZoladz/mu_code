from microbit import *
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

class Motor:
	def __init__(self,IN1,IN2,PWM):
		self.PWM=PWM
		self.IN1=IN1
		self.IN2=IN2

	def run(self,speed):
		self.PWM.write_analog(abs(speed))
		self.IN1.write_digital(speed>0)
		self.IN2.write_digital(speed<0)

class Chasis:		
	def _init_(self):
		self.motors=(Motor(pin13,pin12,pin8)
					,Motor(pin13,pin12,pin8) )
	def go(self,motor_index,speed):
		self.motors[motor_index].run(speed)
