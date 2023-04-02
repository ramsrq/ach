import time
import board
import storage
import usb_cdc
from scripts.utils import Definitions
from scripts.utils import Led
from scripts.utils import CustomButton
from scripts.utils import CustomPrint

led = Led(brightness = 1)
customPrint = CustomPrint()
if customPrint.OLED_PRINT:
    custom_button = CustomButton(default_button_pin = board.GP7)
else:
    custom_button = CustomButton()

# custom_button = CustomButton()
button_pin = custom_button.get_button_pin()

is_pressed = not button_pin.value 
print("boot.py")
print("Button is pressed?")
print(str(is_pressed))

if not is_pressed:
    storage.disable_usb_drive()
    usb_cdc.disable()
    print("Disabling USB drive")
    
else:
    led.led_on(color = Definitions.RED)
    time.sleep(0.5)
    led.led_off()
    time.sleep(0.5)
    
    led.led_on(color = Definitions.GREEN)
    time.sleep(0.5)
    led.led_off()
    time.sleep(0.5)

    led.led_on(color = Definitions.BLUE)
    time.sleep(0.5)
    led.led_off()
    time.sleep(0.5)
    
    print("USB drive enabled")
