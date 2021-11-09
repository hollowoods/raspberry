import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
Switch= 11
LED1 = 3
LED2 = 5
LED3 = 7
Flag=0
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
while True:
   # Flag=0 
# GPIO.input(Switch)와 GPIO.HIGH를 AND 연산으로 변경 가능
    if (GPIO.input(Switch) == GPIO.HIGH and Flag==0):
        print("Button was pushed!")
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.HIGH)
        GPIO.output(LED3, GPIO.HIGH)
        Flag=1
        #sleep(1)
    elif (GPIO.input(Switch) == GPIO.HIGH and Flag==1):
        print("LED OFF")
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW) 
        GPIO.output(LED3, GPIO.LOW)
        Flag=0
    sleep(1)
       
