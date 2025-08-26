from machine import SPI,Pin
from st7735.viet_font import viet_font_12x20
from st7735 import TFT   

spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(26), mosi=Pin(27), miso=None)
dc = 21
rst = 20
cs = 22
tft = TFT(spi, dc, rst, cs)   # khởi tạo theo mạch của bạn
tft.initr()
tft.fill(TFT.BLACK)

tft.text((0, 0), "Xin chào Việt Nam", TFT.WHITE, viet_font_12x20)
tft.text((0, 40), "Ă Â Ê Ô Ơ Ư ă â ê ô ơ ư", TFT.YELLOW, viet_font_12x20)

