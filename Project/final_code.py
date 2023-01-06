import RPi.GPIO as GPIO
import time
import I2C_driver as LCD
from Adafruit_BME280 import *

mylcd = LCD.lcd()
PinTrig=23
PinEcho=24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PinTrig, GPIO.OUT)
GPIO.setup(PinEcho, GPIO.IN)
startTime=0
stopTime=0
pin_num=[10,9,11,5,6,13,19,26]
GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(pin_num, 0)
mylcd = LCD.lcd()
fnd = [(1,1,1,1,1,1,0,0), #0
    (0,1,1,0,0,0,0,0), #1
    (1,1,0,1,1,0,1,0), #2
    (1,1,1,1,0,0,1,0), #3 
    (0,1,1,0,0,1,1,0), #4
    (1,0,1,1,0,1,1,0), #5
    (1,0,1,1,1,1,1,0), #6
    (1,1,1,0,0,1,0,0), #7
    (1,1,1,1,1,1,1,0), #8
    (1,1,1,1,0,1,1,0)] #9
    
duty_ratio= 0
MaxDuty= 12

PWMpin= 18
GPIO.setup(PWMpin, GPIO.OUT) 
Servo=GPIO.PWM(PWMpin, 50) 
Servo.start(0)
mylcd.lcd_clear()
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
k_last=100

def main():
    startTime=0
    stopTime=0
    global k_last
    j=""
    m=0
    k=""
    q=0
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()
    degrees=round(degrees, 2)
    k=degrees
    degrees=str(degrees)
    
    mylcd.lcd_display_string(degrees,1)
    
    k=int(k)
    k_last=int(k_last)
    q=k-k_last
    if(k>=25):
        servo(degrees)
    if(q>0.5):
        seg_warning()
    
    k_last=k
    

def servo(degrees):
    for i in range(0,3,1):
        duty_ratio= 3
        Servo.ChangeDutyCycle(duty_ratio)
        mylcd.lcd_display_string(degrees,1)
        mylcd.lcd_display_string("duty_ratio= 3 ",2)
        time.sleep(1)
        duty_ratio= 10
        Servo.ChangeDutyCycle(duty_ratio)
        mylcd.lcd_display_string("duty_ratio= 10",2)
        time.sleep(1)
    duty_ratio= 3
    Servo.ChangeDutyCycle(duty_ratio)
    mylcd.lcd_clear()
    
def seg_warning():
    for i in range(0,3,1):
        j="8"  
        seg_num(j)
        time.sleep(0.5)
        j="f"  
        seg_num(j)
        time.sleep(0.5)

def seg_num(j):
    if(j=="0"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[0][m])
            time.sleep(2)
    elif(j=="1"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[1][m])
       
    elif(j=="2"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[2][m])
    elif(j=="3"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[3][m])
    elif(j=="4"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[4][m])
    elif(j=="5"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[5][m])
    elif(j=="6"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[6][m])
    elif(j=="7"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[7][m])
    elif(j=="8"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[8][m])
    elif(j=="9"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[9][m])
    else:
        for m in range(0,8,1):
            GPIO.output(pin_num[m], 0)

def SR04():
    while True:
            GPIO.output(PinTrig, False)
            time.sleep(2)
            # trigger
            print ('Calculating Distance. 1 nanosec pulse')
            GPIO.output(PinTrig, True)
            time.sleep(0.00001)
            GPIO.output(PinTrig, False)
            # echo
            while GPIO.input(PinEcho) == 0:
                startTime = time.time()
            while GPIO.input(PinEcho) == 1:
                stopTime = time.time()
            
            Time_interval= stopTime - startTime
            Distance = Time_interval * 17000
            Distance = round(Distance, 2)
            print ('Distance => ', Distance, 'cm')
    # GPIO.cleanup()

while True:        
    if __name__ == '__main__':
        main()