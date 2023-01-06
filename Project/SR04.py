import RPi.GPIO as GPIO
import time

def main():
    PinTrig=23
    PinEcho=24
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PinTrig, GPIO.OUT)
    GPIO.setup(PinEcho, GPIO.IN)
    
    startTime=0
    stopTime=0
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