import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
pwm=GPIO.PWM(38, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(38, True)
    pwm.ChangeDutyCycle(duty)
    sleep(2)
    GPIO.output(38, False)

SetAngle (90)
SetAngle(0)
SetAngle(180)
SetAngle (0)
SetAngle (90)
SetAngle (0)
pwm.stop()
GPIO.cleanup()