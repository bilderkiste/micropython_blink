from machine import Timer, Pin
from neopixel import NeoPixel

class ValueChange:
    
    def __init__(self, output_device, n, on_time, off_time):
        self._output_device = output_device
        
        self._n = n
        if self._n > 0:
            self._n *= 2
  
        self._on_time = on_time
        self._off_time = off_time
        
        self._timer = Timer()
        
        self._set_value()
            
    def _set_value(self, timer_obj=None):
        if self._n == 0:
            return
        
        # Counter for infity blinking
        if self._n == -1:
            self._n -= 1
        elif self._n == -2:
            self._n += 1
        
        if self._n % 2 == 0:
            ms = self._on_time
        else:
            ms = self._off_time
        
        if self._n > 0:
            self._n -= 1
            
        self._output_device.toggle()
        self._timer.init(period=ms, mode=Timer.ONE_SHOT, callback=self._set_value)
        
    def stop(self):
        self._n = 0

class OutputDevice:
    """
    Abstract base class for output devices.
    """
    
    def __init__(self):
        #self.off()
        pass
    
    def is_active(self):
        pass
    
    def on(self):
        pass
        
    def off(self):
        pass
        
    def toggle(self):
        pass
    
    def stop(self):
        self._valueChanger.stop()
        self.off()
        
    def blink(self, n=-1, on_time=1000, off_time=None):
        self.off()
        
        off_time = on_time if off_time is None else off_time
        
        # Parameter n<1 are not allowed. Set parameter to -1.
        if n < -1 : n = -1
        
        self._valueChanger = ValueChange(self, n, on_time, off_time)
        
        
class LED(OutputDevice):
    """
    Represents an LED.
    
    :param int pin
    The pin where the LED is connected to.
    """   
    
    def __init__(self, pin):
        self._pin_num = pin
        self._pin = Pin(pin, Pin.OUT)
        super().__init__()
        
    def is_active(self):
        if self._pin.value():
            return True
        else:
            return False
    
    def on(self):
        self._pin.on()
        
    def off(self):
        self._pin.off()
        
    def toggle(self):
        self._pin.toggle()
        
class NeoString():
    """
    Represents an RGB LED string with WS2812 controlled LED's.
    
    :param int pin
    The pin where the LED string is connected to.
    
    :param int length
    The length of the LED string.
    """

    def __init__(self, pin, length):
        self._neo_string = NeoPixel(Pin(pin), length)
  
    def get(self):
        return self._neo_string
     
class NeoLED(OutputDevice):
    """
    Represents an RGB LED (Neopixel) with WS2812 controller in a LED string.
    
    :param object neostring
    The LED string the LED ist beloning to.
    
    :param int index
    The index of the assigned LED. Must be between 0 and length-1.
    """
    
    def __init__(self, neo_string, index):
        self._led_index = index
        self._neo = neo_string
        self._color = (30,30,30)
        
        super().__init__()
        
    def on(self):
        self._neo.get().__setitem__(self._led_index, self._color)
        self._neo.get().write()
        
    def off(self):
        self._neo.get().__setitem__(self._led_index, (0,0,0))
        self._neo.get().write()    
      
    def toggle(self):
        if self._neo.get().__getitem__(self._led_index) == (0,0,0):
            self.on()
        else:
            self.off()
            
    def set_color(self, color):
        self._color = color
