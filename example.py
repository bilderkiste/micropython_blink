from blink import NeoString, NeoLED, LED
import time
import machine


led = LED(16)
led.blink(3, 200, 500)

led = LED("LED")
led.blink(-1, 200)

neo_string = NeoString(1,4)
neo_led1 = NeoLED(neo_string,0)
neo_led1.set_color((0,100,0))
neo_led1.blink(6,100,1500)
neo_led2 = NeoLED(neo_string,1)
neo_led2.set_color((0,0,100))
neo_led2.blink(4)
