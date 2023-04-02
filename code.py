import board
from scripts.achv5 import ACH
from scripts.utils import Definitions
from scripts.utils import CustomPrint

board_id = board.board_id
customPrint = CustomPrint()

if board_id == Definitions.RASPBERRY_PI_PICO_ID or \
   board_id == Definitions.WAVESHARE_RP2040_ZERO_ID:
    print("id:" + board_id)
    ACH.start(customPrint) 
else:
    print("Unknown board: " + board_id)

