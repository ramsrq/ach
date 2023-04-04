import time
import board
import usb_hid
import secrets
from adafruit_datetime import datetime
from adafruit_hid.mouse import Mouse
from scripts.utils import Definitions
from scripts.utils import Led
from scripts.utils import CustomButton
from scripts.utils import CustomPrint
from scripts.hid_ducky import HID_Ducky

class ACH:
    
    def start(customPrint):
    
        led = Led()
        
        if customPrint.OLED_PRINT:
            custom_button = CustomButton(default_button_pin = board.GP7)
        else:
            custom_button = CustomButton()
            
        button = custom_button.get_button()
        
        mouse_move_delta = 5    
        mouse_move_delay = 30

        mouse = Mouse(usb_hid.devices)

        initial_delay = 1
        led.led_on(color = Definitions.WHITE)
        time.sleep(initial_delay)
        led.led_off()

        STOPED = 0
        RUNNING = 1
        status = RUNNING
        print("Status: RUNNING")
        
        second_prev = 0;

        while True:
            
            date_now = datetime.now()
            #hour_now = date_now.time().hour
            #minute_now = date_now.time().minute
            second_now = date_now.time().second

            if status == RUNNING:
                
                if second_prev != second_now:
                    
                    second_prev = second_now
                    
                    if second_now % mouse_move_delay == 0:
                        
                        print(str(date_now))
                        print("Mouse move")
                        
                        led.led_on(color = Definitions.BLUE)
                        mouse.move(mouse_move_delta, 0, 0)
                        time.sleep(0.1)
                        mouse.move(-1*mouse_move_delta, 0, 0)
                        
                    else:
                        led.led_on(color = Definitions.GREEN)
                        
                else:
                    led.led_off()
                
            if status == STOPED:
                led.led_on(color = Definitions.RED)
                
            button.update()
            short_count = button.short_count
            long_press = button.long_press

            if short_count == 1:
                
                print("short push") 
                if status != RUNNING:
                    status = RUNNING
                    print("Status: RUNNING")
                    
                elif status != STOPED:
                    status = STOPED
                    print("Status: STOPED")
                    
            if long_press:
                
                print("long_press: " + str(long_press))
                led.led_off()
                time.sleep(1)
                led.led_on(color = Definitions.PURPLE)
                time.sleep(5)

                HID_Ducky.start()
                
                status = RUNNING
                print("Status: RUNNING")
                                
            time.sleep(0.01)
