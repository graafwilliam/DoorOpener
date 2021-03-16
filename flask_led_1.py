import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

import os
from flask import Flask, render_template, request
app = Flask(__name__)

template_dir = os.path.abspath('../../templates')

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"


@app.route('/hello-template')
def hello_template(name=None):
    print(template_dir)
    return render_template('hello.html', name=name)


@app.route('/led',methods=['POST', 'GET'])
def led_control():
    if request.method == 'POST':

        led_switch = request.form['switch']

        if led_switch == 'on':
            GPIO.output(40, GPIO.HIGH)
            print("ON RECEIVED")

        if led_switch == 'off':
            GPIO.output(40, GPIO.LOW)
            print("OFF RECEIVED")

    led_state = GPIO.input(40)

    return render_template('flask_led_1.html', led_state=led_state)


if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)