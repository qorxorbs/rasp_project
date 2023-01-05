import RPi.GPIO as GPIO
import time
          # A B C D E F G DP
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


for i in range(0,10,1):
    for m in range(0,8,1):
        GPIO.output(pin_num[m], fnd[i][m])
    time.sleep(0.3)
    
    
k=input("숫자 입력")
if(k=="0"):
    for m in range(0,8,1):
        GPIO.output(pin_num[m], fnd[0][m])
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
        GPIO.output(pin_num[m], fnd[8][m])
else:
    for m in range(0,8,1):
        GPIO.output(pin_num[m], 0)