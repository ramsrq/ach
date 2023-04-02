import board
import displayio
import terminalio
from adafruit_display_text import label

class OLED:
    
    def __init__(self, display, title = board.board_id, WIDTH = 128, HEIGHT = 64):
        
        # displayio.release_displays()
        
        # i2c = busio.I2C (scl = scl, sda = sda) 
        # display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
        # self.display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

        #WIDTH = 128
        #HEIGHT = 64
        BORDER = 1

        # Make the display context
        self.display = display
        self.splash = displayio.Group()
        self.display.show(self.splash)

        color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        self.splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
        self.splash.append(inner_sprite)

        # Draw a label
        x0 = 5
        y0 = 9
        
        x = x0
        y = y0 + ( 0 * 14 )
        title_label = label.Label(terminalio.FONT, x = x, y = y)
        title_label.text = title
        self.splash.append(title_label)
        
        x = x0
        y = y0 + ( 1 * 14 )
        self.line1_label = label.Label(terminalio.FONT, x = x, y = y)
        self.line1_label.text = ""
        self.splash.append(self.line1_label)

        x = x0
        y = y0 + ( 2 * 14 )
        self.line2_label = label.Label(terminalio.FONT, x = x, y = y)
        self.line2_label.text = ""
        self.splash.append(self.line2_label)

        x = x0
        y = y0 + ( 3 * 14 )
        self.line3_label = label.Label(terminalio.FONT, x = x, y = y)
        self.line3_label.text = ""
        self.splash.append(self.line3_label)

        self.display.show(self.splash)
        self.display.refresh()

    def oled_print(self, text):
        
        self.line1_label.text = self.line2_label.text
        self.line2_label.text = self.line3_label.text
        self.line3_label.text = text
        
        self.display.show(self.splash)
        self.display.refresh()
        