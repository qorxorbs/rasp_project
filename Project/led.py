import RPi.GPIO as GPIO
import time
pin_num=[14,15,18]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
k='0'

def main():
    GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)
    # for i in range:
    #     GPIO.output(pin_num, 0)
    #     GPIO.output(pin_num[i], 1)
    #     time.sleep(2)
    
    
    k=input("R,G,B 중 하나를 입력하세요")
    if(k=='r'):
        GPIO.output(pin_num, 0)
        GPIO.output(pin_num[0], 1)
    elif(k=='g'):
        GPIO.output(pin_num, 0)
        GPIO.output(pin_num[1], 1)
    elif(k=='b'):
        GPIO.output(pin_num, 0)
        GPIO.output(pin_num[2], 1)
    else:
        GPIO.output(pin_num, 1)


while True:
    if __name__ == '__main__':
        main()
        time.sleep(2)