import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

MATRIX = [['1', '2', '3', 'A'],
          ['4', '5', '6', 'B'],
          ['7', '8', '9', 'C'],
          ['*', '0', '#', 'D']]

ROW = [7, 11, 13, 15]
COL = [12, 16, 18, 22]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

password = 1234
attempt = ""
try:
    while (True):
        for j in range(4):
            GPIO.output(COL[j], 0)

            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    time.sleep(0.01)
                    while (GPIO.input(ROW[i]) == 0):
                        pass
                    attempt += MATRIX[i][j]
                    if len(attempt) == len(password):
                        if attempt == password:
                            print ("Password OK")
                            # This is where you unlock the door.
                            #
                        else:
                            print("Password incorrect")
                        attempt = ""
            time.sleep(0.50)

            GPIO.output(COL[j], 1)
except KeyboardInterrupt:
    GPIO.cleanup()