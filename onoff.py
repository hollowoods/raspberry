import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import I2C_driver as LCD
from time import *
from time import sleep
Switch1= 12
Switch2= 18
Switch3= 16
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
    GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    while True:
# GPIO.input(Switch)와 GPIO.HIGH를 AND 연산으로 변경 가능
        if (GPIO.input(Switch1) == GPIO.HIGH):
            mylcd.lcd_clear()
            print("Button was pushed!")
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW) 
            GPIO.output(LED3, GPIO.LOW)
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'T', fill="white", font=proportional(CP437_FONT))               
                mylcd.lcd_display_string("Right",1)
            mylcd.lcd_clear()
            sleep(1)

        elif (GPIO.input(Switch2) == GPIO.HIGH):
            mylcd.lcd_clear() 
            print("F on")
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'F', fill="white", font=proportional(CP437_FONT))
            for i in range(100):
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.HIGH) 
                GPIO.output(LED3, GPIO.HIGH)
                sleep(0.1)
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW) 
                GPIO.output(LED3, GPIO.LOW)
                sleep(0.1)
            sleep(1)
        elif (GPIO.input(Switch3) == GPIO.HIGH):
            mylcd.lcd_clear() 
            print("L on")
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW) 
            GPIO.output(LED3, GPIO.LOW)
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'L', fill="white", font=proportional(CP437_FONT))
            mylcd.lcd_display_string("Room Light ON",1)
            sleep(1)
        elif (GPIO.input(Switch3) == GPIO.LOW,GPIO.input(Switch2) == GPIO.LOW,GPIO.input(Switch3) == GPIO.LOW):
            mylcd.lcd_clear() 
            print("Nothing")
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW) 
            GPIO.output(LED3, GPIO.LOW)
            with canvas(virtual) as draw:
                text(draw, (0, 1), ' ', fill="white", font=proportional(CP437_FONT))
            sleep(1)

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
