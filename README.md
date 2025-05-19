# micropython_blink
A blinking library for Micropython for usual LED's on a GPIO and addressable WS2812 based LED's.

I wrote this library for my Rasperry Pico Pi with RP2040 processor.

How to use the library with usual LED.


```python
from blink import LED's
import machine

# initialize LED on GPIO 16
led = LED(16) # params GPIO Number
led.blink(3, 200, 500) # params int repetitions (optional), int on time in milliseconds (ms) (optional), int off time in milliseconds (optional)

# initialize On-Board LED 
led = LED("LED")
# Blink forever with 200ms on and 200ms off
led.blink(-2, 200)
```

How to use the library with WS2812 based LED's.

```python
from blink import NeoLED, NeoString
import machine

# initialize the Neopixel string
neo_string = NeoString(1,4) # params int GPIO Number, number int of LED's in the string
# initialize the second LED in the string
neo_led1 = NeoLED(neo_string,1) # params object NeoString, int index of LED 
neo_led1.set_color((0,100,0)) # params tupel (byte, byte, byte) (green, red, blue) set the color of the led 
neo_led1.blink(2) # blink two times with 1 second on and 1 second off
```
Negative repetitions blink forever. No params blink forever for one second on and one second off.
