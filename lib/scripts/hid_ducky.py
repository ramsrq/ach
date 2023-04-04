import time
import usb_hid
import secrets
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode_win_la import Keycode
from adafruit_hid.keyboard_layout_win_la import KeyboardLayout

class HID_Ducky:
    
    def start():
    
        keyboard = Keyboard(usb_hid.devices)
        layout = KeyboardLayout(keyboard)

        print("HID_Ducky")
        time.sleep(1)
        
        print("ENTER")
        keyboard.send(Keycode.ENTER)
        time.sleep(5)

        print("CTRL + ALT + SUP")
        keyboard.press(Keycode.CONTROL, Keycode.LEFT_ALT, Keycode.DELETE)
        keyboard.release_all()
        time.sleep(10)
        
        print("PASSWORD")
        password = secrets.password
        layout.write(password)
        time.sleep(1)
        
        print("ENTER")
        keyboard.send(Keycode.ENTER)
        time.sleep(1)
        