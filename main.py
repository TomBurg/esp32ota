# Test OTA routines

from machine import RTC
import machine
import network
import time
#import utime
#from machine import Pin, I2C
#from neopixel import NeoPixel
from ssd1306 import SSD1306
from ssd1306 import SSD1306_I2C
from ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/TomBurg/esp32ota')
    o.download_and_install_update_if_available('wifi-ssid', 'wifi-password')


def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    time.sleep(1)

def boot():
    download_and_install_update_if_available()
    start()


boot()