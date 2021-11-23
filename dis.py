import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import I2C_driver as LCD
from time import *
from time import sleep
Switch= 11
LED1 = 33
LED2 = 35
LED3 = 37
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
from time import sleep, strftime
from datetime import datetime
mylcd = LCD.lcd()
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
def main():
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
    Flag=0
    count=0
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    while True:
# GPIO.input(Switch)와 GPIO.HIGH를 AND 연산으로 변경 가능
        if (GPIO.input(Switch) == GPIO.HIGH and Flag==0):
            print("Button was pushed!")
            if (count==0):
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)
                sleep(0.5)
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED3, GPIO.LOW)
                sleep(0.5)
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.HIGH)
                sleep(0.5)
                count= count + 1
            elif(count==1):
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)
                sleep(0.5)
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED3, GPIO.LOW)
                sleep(0.5)
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.HIGH)
                sleep(0.5)
                count= count + 1
            else:
                count=0

            with canvas(virtual) as draw:
                text(draw, (0, 1), '<', fill="white", font=proportional(CP437_FONT))               
                mylcd.lcd_display_string("Right",1)

                Flag=1

                

        elif (GPIO.input(Switch) == GPIO.HIGH and Flag==1):
            print("LED OFF")
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'X', fill="white", font=proportional(CP437_FONT))
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW) 
                GPIO.output(LED3, GPIO.LOW)
                mylcd.lcd_clear()
                Flag=0
        sleep(1)
       
'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
