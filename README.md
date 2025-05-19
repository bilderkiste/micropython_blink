# micropython_blink
A blinking library for Micropython for usual LED's on a GPIO and addressable WS2812 based LED's.

I wrote this library for my Rasperry Pico Pi with RP2040 processor.

How to use the library with usual LED. Negative repetitions blink forever.


'''python
from blink import LED's
import machine

led = LED(16) # params Pin Number
led.blink(3, 200, 500) # params repetitions, on time in milliseconds, off time in milliseconds

led = LED("LED")
led.blink(-2, 200, 500)
'''
How to use the library with WS2812 based LED's.

'''python
from blink import NeoLED, NeoString
import machine
'''
