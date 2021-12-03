import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime
import I2C_driver as LCD
from time import *
import random
import time
switch1 = 12
switch2 = 18
switch3 = 16
switch4 = 11
PLED = 32
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
GPIO.setup(switch1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PLED, GPIO.OUT, initial=GPIO.LOW)


def main():
    abc=[1,2,3]
    mylcd = LCD.lcd()
    number=0
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    GPIO.setup(PLED, GPIO.OUT)

    PWM_LED= GPIO.PWM(PLED, 50)
    PWM_LED.start(0)
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        if(GPIO.input(switch1)== GPIO.HIGH):
            print("Button was pushed!")
            n=random.choice(abc)
            number += n
            if number >=10:
                mylcd.lcd_clear()
                mylcd.lcd_display_string("TOUCH sensor",1)
           
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)
        
        if(GPIO.input(switch1)== GPIO.LOW):
            print("Button was NOTpushed!")
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)
                
        if(GPIO.input(switch2)== GPIO.HIGH):
            print("Button was pushed!")
            n=random.choice(abc)
            number += n
            if number >=10:
                mylcd.lcd_clear()
                mylcd.lcd_display_string("FLAME sensor",1)
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)
#             for i in range(10):
#                 GPIO.output(LED1,GPIO.HIGH)
#                 sleep(0.5)
#                 GPIO.output(LED1,GPIO.LOW)
#                 sleep(0.5)
                
        if(GPIO.input(switch2)== GPIO.LOW):
            print("Button was NOTpushed!")
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)
                
        if(GPIO.input(switch3)== GPIO.HIGH):
            print("Button was pushed!")
            n=random.choice(abc)
            number += n
            if number >=10:
                mylcd.lcd_clear()
                mylcd.lcd_display_string("LIGHT sensor",1)
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)
                
        if(GPIO.input(switch3)== GPIO.LOW):
            print("Button was NOTpushed!")
            mylcd.lcd_clear()
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)

        if(GPIO.input(switch4)== GPIO.HIGH):
            print("Button was pushed!")
            n=random.choice(abc)
            number += n
            if number >=10:
                mylcd.lcd_clear()
                mylcd.lcd_display_string("BUTTON",1)
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)

        if(GPIO.input(switch4)== GPIO.LOW):
            print("Button was NOTpushed!")
            mylcd.lcd_clear()
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(number), fill="white", font=proportional(CP437_FONT))
            sleep(1)
        if number >= 10:
            for duty in range(100, -1, -5):
                PWM_LED.ChangeDutyCycle(duty)
                sleep(0.1)
            
        
    

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
