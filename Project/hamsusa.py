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

def main():
    k=input("1: 거리측정, 2: 문열기")
    if(k=="1"):
        SR04()
    elif(k=="2"):
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

if __name__ == '__main__':
    main()