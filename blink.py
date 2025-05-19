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
        
        self._valueChanger = ValueChange(self, n, on_time, off_time)
        
        
class LED(OutputDevice):
    
    def __init__(self, pin):
        self._pin_num = pin
        self._pin = Pin(pin, Pin.OUT)
        
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
        
class Neo(OutputDevice):

    def __init__(self, pin, index):
        self._pin_num = pin
        self._led_index = index
        
        self._color = (30,30,30)
        
        self._neo = NeoPixel(Pin(pin), 4)
        
    def on(self):
        self._neo[self._led_index] = self._color
        self._neo.write()
        
    def off(self):
        self._neo[self._led_index] = (0,0,0)
        self._neo.write()    
      
    def toggle(self):
        if self._neo[self._led_index] == (0,0,0):
            self.on()
        else:
            self.off()
            
    def set_color(self, color):
        self._color = color
