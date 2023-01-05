import RPi.GPIO as GPIO
import time
pin_num=[14,15,18,23,24,16,20,21]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
k=""
GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(pin_num, 0)
# for i in range(0,8,1):
#     GPIO.output(pin_num[i], 1)
#     time.sleep(1)
#     GPIO.output(pin_num, 0)

 
# def short_num(k):
    # if (k=="0"):
    #     GPIO.output(pin_num[0]|pin_num[1]|pin_num[2]|pin_num[3]|pin_num[4]|pin_num[5], 1)
    # elif (k =="1"):
    #     GPIO.output(pin_num[1]|pin_num[2], 1)
    # elif (k =="2"):
    #     GPIO.output(pin_num[0]|pin_num[1]|pin_num[3]|pin_num[4]|pin_num[6], 1)
    # elif (k =="3"):
    #     GPIO.output(pin_num[0]|pin_num[1]|pin_num[2]|pin_num[3]|pin_num[6], 1)
    # elif (k =="4"):
    #     GPIO.output(pin_num[1]|pin_num[2]|pin_num[5]|pin_num[6], 1)    
    # elif (k =="5"):
    #     GPIO.output(pin_num[0]|pin_num[2]|pin_num[3]|pin_num[5]|pin_num[6], 1)
    # elif (k =="6"):
    #     GPIO.output(pin_num[0]|pin_num[2]|pin_num[3]|pin_num[4]|pin_num[5]|pin_num[6], 1)
    # elif (k =="7"):
    #     GPIO.output(pin_num[0]|pin_num[1]|pin_num[2]|pin_num[5], 1)
    # elif (k =="8"):
    #     GPIO.output(pin_num[0]|pin_num[1]|pin_num[2]|pin_num[3]|pin_num[4]|pin_num[5]|pin_num[6], 1)  
    # elif (k =="9"):
    #     GPIO.output(pin_num[0]|pin_num[1]|pin_num[2]|pin_num[3]|pin_num[5]|pin_num[6], 1) 
        
        
k=input("숫자 입력")
if (k=="0"):
    GPIO.output(pin_num[0] or pin_num[1] or pin_num[2] or pin_num[3] or pin_num[4] or pin_num[5], 1)
elif (k =="1"):
    GPIO.output(pin_num[1]or pin_num[2], 1)
elif (k =="2"):
    GPIO.output(pin_num[0]or pin_num[1]or pin_num[3]or pin_num[4]or pin_num[6], 1)
elif (k =="3"):
    GPIO.output(pin_num[0]or pin_num[1]or pin_num[2]or pin_num[3]or pin_num[6], 1)
elif (k =="4"):
    GPIO.output(pin_num[1]or pin_num[2]or pin_num[5]or pin_num[6], 1)    
elif (k =="5"):
    GPIO.output(pin_num[0]or pin_num[2]or pin_num[3]or pin_num[5]or pin_num[6], 1)
elif (k =="6"):
    GPIO.output(pin_num[0]or pin_num[2]or pin_num[3]or pin_num[4]or pin_num[5]or pin_num[6], 1)
elif (k =="7"):
    GPIO.output(pin_num[0]or pin_num[1]or pin_num[2]or pin_num[5], 1)
elif (k =="8"):
    GPIO.output(pin_num[0]or pin_num[1]or pin_num[2]or pin_num[3]or pin_num[4]or pin_num[5]or pin_num[6], 1)  
elif (k =="9"):
    GPIO.output(pin_num[0]or pin_num[1]or pin_num[2]or pin_num[3]or pin_num[5]or pin_num[6], 1)
time.sleep(1)
