import RPi.GPIO as GPIO
import time
import I2C_driver as LCD
k=""
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
m=""
PWMpin= 18
GPIO.setup(PWMpin, GPIO.OUT) 
Servo=GPIO.PWM(PWMpin, 50) 
Servo.start(0)
mylcd.lcd_clear()

def main():
    k=input("1: 거리측정, 2: 문열기")
    if(k=="1"):
        seg_num(k)
        SR04()
    elif(k=="2"):
        seg_num(k)
        servo()
        mylcd.lcd_display_string("open",1)
        time.sleep(1)
        mylcd.lcd_clear()
        mylcd.lcd_display_string("1",1)
        time.sleep(1)
        mylcd.lcd_display_string("2",1)
        time.sleep(1)
        mylcd.lcd_display_string("close",1)
        time.sleep(1)
        mylcd.lcd_clear() 
    GPIO.cleanup()
    

def servo():
    duty_ratio= 3
    Servo.ChangeDutyCycle(duty_ratio)
    mylcd.lcd_display_string("num=0",1)
    mylcd.lcd_display_string("duty_ratio= 3",2)
    time.sleep(2)
    duty_ratio= 10
    Servo.ChangeDutyCycle(duty_ratio)
    mylcd.lcd_display_string("num=0",1)
    mylcd.lcd_display_string("duty_ratio= 3",2)
    time.sleep(2)
    

def seg_num(k):
    if(k=="0"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[0][m])
            time.sleep(2)
    elif(k=="1"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[1][m])
       
    elif(k=="2"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[2][m])
    elif(k=="3"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[3][m])
    elif(k=="4"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[4][m])
    elif(k=="5"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[5][m])
    elif(k=="6"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[6][m])
    elif(k=="7"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[7][m])
    elif(k=="8"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[8][m])
    elif(k=="9"):
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
    GPIO.cleanup()
        
if __name__ == '__main__':
    main()