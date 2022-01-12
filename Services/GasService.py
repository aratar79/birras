# imports raspberry
# from w1thermsensor import W1ThermSensor
# install the w1thermsensor package to be able to import the library
# sudo pip3 install adafruit-circuitpython-ccs811
import busio
import adafruit_ccs811
from board import board

class GasService:

        def __init__(self):
           self.i2c = board.I2C()
           self.ccs =  adafruit_ccs811.CCS811(i2c)


        def get_data_co2(self):
            return self.css.eco2
        def get_data_tvoc(self):
            return self.css.tvoc