## constants.py
import board
import time
import busio
import digitalio
import displayio
import adafruit_displayio_ssd1306
from scripts.oled import OLED

class Definitions:
    
    RASPBERRY_PI_PICO_ID = "raspberry_pi_pico"
    WAVESHARE_RP2040_ZERO_ID = "waveshare_rp2040_zero"
    PIMORONI_BADGER2040_ID = "pimoroni_badger2040"
    
    OFF = (0, 0, 0)
    WHITE = (255,255,255)
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)

class Led:
    
    def __init__ (self, brightness = 0.05):
        
        board_id = board.board_id
        if board_id == Definitions.RASPBERRY_PI_PICO_ID:
            self.led = digitalio.DigitalInOut(board.LED)
            self.led.direction = digitalio.Direction.OUTPUT
        elif board_id == Definitions.WAVESHARE_RP2040_ZERO_ID:
            import neopixel 
            ORDER = neopixel.RGB
            pixel_pin = board.NEOPIXEL
            self.pixel = neopixel.NeoPixel(pixel_pin, 1, brightness = brightness, pixel_order = ORDER)
        
    def led_on(self, color = Definitions.WHITE):
        
        board_id = board.board_id
        if board_id == Definitions.RASPBERRY_PI_PICO_ID:
            self.led.value = True
        elif board_id == Definitions.WAVESHARE_RP2040_ZERO_ID:
            self.pixel[0] = color
            
    def led_off(self):
        
        board_id = board.board_id
        if board_id == Definitions.RASPBERRY_PI_PICO_ID:
            self.led.value = False
        elif board_id == Definitions.WAVESHARE_RP2040_ZERO_ID:
            self.pixel[0] = Definitions.OFF

class CustomButton:
        
    def __init__(self, default_button_pin = board.GP13):
        
        board_id = board.board_id
        
        if board_id == Definitions.RASPBERRY_PI_PICO_ID:
            
            button_ref_board_pin = board.GP14
            button_board_pin = default_button_pin
            # button_board_pin = board.GP7 # rpipico without OLED
            # button_board_pin = board.GP13 # rpipico without OLED
                
        elif board_id == Definitions.WAVESHARE_RP2040_ZERO_ID:
            
            button_ref_board_pin = board.GP12
            button_board_pin = board.GP10
            
        refrence = digitalio.DigitalInOut(button_ref_board_pin)
        refrence.direction = digitalio.Direction.OUTPUT
        refrence.value = False
        
        self.button_pin = digitalio.DigitalInOut(button_board_pin)
        self.button_pin.pull = digitalio.Pull.UP
        
    def get_button(self):
        
        from adafruit_debouncer import Button
        button_pin = self.button_pin
        button = Button(button_pin, long_duration_ms=3000)
        return button

    def get_debouncer(self):
        
        from adafruit_debouncer import Debouncer
        button_pin = self.button_pin
        debouncer = Debouncer(button_pin)
        return debouncer

    def get_button_pin(self):
        return self.button_pin

class CustomPrint:
    
    OLED_PRINT = False
    
    def __init__ (self):

        board_id = board.board_id
        if board_id == Definitions.RASPBERRY_PI_PICO_ID:
            try:
                WIDTH = 128
                HEIGHT = 64
                
                displayio.release_displays()
                
                self.i2c = busio.I2C (scl = board.GP17, sda = board.GP16) 
                self.display_bus = displayio.I2CDisplay(self.i2c, device_address=0x3C)
                display = adafruit_displayio_ssd1306.SSD1306(self.display_bus, width=WIDTH, height=HEIGHT)

                self.OLED_PRINT = True
                # self.oled = OLED(display)
                print("OLED display attached")
                
            except Exception:
                print("NO display attached") 


    def custom_print(self, text):
        
        if self.OLED_PRINT:
            # self.oled.oled_print(text)
            pass; 
        print(text)
    