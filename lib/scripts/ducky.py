import usb_hid
import secrets
import adafruit_ducky
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_la import KeyboardLayout

class Ducky:
    
    def start():
    
        keyboard = Keyboard(usb_hid.devices)
        layout = KeyboardLayout(keyboard)
        
        file = secrets.ducky_script
        duck = adafruit_ducky.Ducky(file, keyboard, layout)
        result = True
        while result is not False:
            result = duck.loop()
