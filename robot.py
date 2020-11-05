from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

LF=18
LB=23
RF=24
RB=25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)
GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.output(LF , 0)
GPIO.output(RF , 0)
GPIO.output(LB, 0)
GPIO.output(RB, 0)
print "Done"

a=1
@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    GPIO.output(LF , 0)
    GPIO.output(LB , 0)
    GPIO.output(RF , 1)
    GPIO.output(RB , 0)
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   GPIO.output(LF , 1)
   GPIO.output(LB , 0)
   GPIO.output(RF , 0)
   GPIO.output(RB , 0)
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   GPIO.output(LF , 1)
   GPIO.output(LB , 0)
   GPIO.output(RF , 1)
   GPIO.output(LB , 0)
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   GPIO.output(LF , 0)
   GPIO.output(LB , 1)
   GPIO.output(RF , 0)
   GPIO.output(RB , 1)
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(LF , 0)
   GPIO.output(LB , 0)
   GPIO.output(RF , 0)
   GPIO.output(RB , 0)
   return  'true'

if __name__ == "__main__":
 print "Start"
 app.run(host='192.168.29.176',port=5010)
