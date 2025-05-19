from blink import Neo, LED
from time import sleep
import machine
import time


led = LED(16)
led.blink(3, 200, 500)

led = LED("LED")
led.blink(3, 200, 500)

neo_string = NeoString(1,4)
neo_led1 = NeoLED(neo_string,1)
neo_led1.set_color((0,100,0))
neo_led1.blink(4,500,1500)
neo_led2 = NeoLED(neo_string,0)
#neo1.set_color((0,100,0))
neo_led2.blink(4, 1000,1000)

