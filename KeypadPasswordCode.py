import RPi.GPIO as GPIO
import time
from time import sleep

#GPIO Setup
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

# set gpio for servo
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(5)
GPIO.setup(38, GPIO.OUT)
pwm=GPIO.PWM(38, 50)
pwm.start(0)
#set gpio for key pad
# THIS OS
rowsPins = [12,16,18,22]
colsPins = [19,15,13,11]


for j in range(4):
    GPIO.setup(colsPins[j], GPIO.OUT)
    GPIO.output(colsPins[j], 1)

for i in range(4):
    GPIO.setup(rowsPins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(38, True)
    pwm.ChangeDutyCycle(duty)
    sleep(2)
    GPIO.output(38, False)

def open_door():
    SetAngle(90)
    print("Opening the door!")

def close_door():
    SetAngle(0)
    print("Closing the door!")
#Function to check keypad input!
def check_keypad(length):

    MATRIX = [["1","2","A","3"],
              ["4","5","6","B"],
              ["7","8","9","C"],
              ["*","0","#","D"]]
    result = ""
    while(True):
        for j in range(4):
            GPIO.output(colsPins[j], 0)

            for i in range(4):
                if GPIO.input(rowsPins[i]) == 0:
                    time.sleep(0.02)
                    result = result + MATRIX[i][j]
                    while(GPIO.input(rowsPins[i]) == 0):
                          time.sleep(0.02)

            GPIO.output(colsPins[j], 1)
            if len(result) >= length:
                return result

def accept_code():
    doorstatus = False
    while True:
        # password
        password = "6" "D" "9" "*"
        length = len(password)

        #Password From KeyPad
        print("Please Enter User Password: ")
        result = check_keypad(length)


        #Password Check
        if result == password:
            print("Password Correct ")
            pwm.ChangeDutyCycle(10)
            if doorstatus==False:
                open_door()
                doorstatus=True
            elif doorstatus==True:
                close_door()
                doorstatus=False

        else:
            print("Password incorrect")



accept_code()