import RPi.GPIO as GPIO 
import time 

def main():
    pin_num=[10,9,11,5,6,13,19,26]
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    k=""
    GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(pin_num, 0)

      # A B C D E F G DP
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
    print('Wating for 1 sec') 
    # time.sleep(1) 
    
    k=input("숫자 입력")
    if(k=="0"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[0][m])
        duty_ratio= 3
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="1"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[1][m])
        duty_ratio= 4
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="2"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[2][m])
        duty_ratio= 5
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="3"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[3][m])
        duty_ratio= 6
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="4"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[4][m])
        duty_ratio= 7
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="5"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[5][m])
        duty_ratio= 8
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="6"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[6][m])
        duty_ratio= 9
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="7"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[7][m])
        duty_ratio= 10
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="8"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[8][m])
        duty_ratio= 11
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    elif(k=="9"):
        for m in range(0,8,1):
            GPIO.output(pin_num[m], fnd[9][m])
        duty_ratio= 12
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
    else:
        for m in range(0,8,1):
            GPIO.output(pin_num[m], 0)
        duty_ratio= 3
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
        print("다른거 입력함")
    Servo.stop()
    # print('Rotating at interval of 0-12 degrees')
    # while duty_ratio <= MaxDuty:
    #     Servo.ChangeDutyCycle(duty_ratio)
    #     time.sleep(2)
    #     duty_ratio+= 1
        
    # if duty_ratio == MaxDuty:
    #     duty_ratio= 0
    #     Servo.ChangeDutyCycle(duty_ratio)
    
    # Servo.stop()
    # GPIO.cleanup()
    # print('Everythings cleanup')

while True:
    if __name__ == '__main__':
        main()
        