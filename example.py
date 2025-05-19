from blink import Neo
from time import sleep
import machine
import time

led = LED(16)
led.blink(3, 200, 500)

neo2 = Neo(1,0)
neo2.blink(7, 400, 200)

neo1 = Neo(1, 1)
neo1.set_color((0,30,100))
neo1.blink(-1, 100, 200)

time.sleep(5)
neo1.stop()
neo2.set_color((20,0,0))
neo2.blink(7, 400, 200)
time.sleep(5)
neo1.set_color((0,30,0))
neo1.blink(-1, 100, 1000)
