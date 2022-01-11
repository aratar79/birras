# imports raspberry
# from w1thermsensor import W1ThermSensor
# install the w1thermsensor package to be able to import the library
# sudo pip3 install adafruit-circuitpython-ccs811
import busio
import adafruit_ccs811
from board import board

class GasService:

        #def __init__(self):
            #self.fakedata = FakeDataService()

        def config(self):
            pin = 17
            pin = 27
            # pass

        def get_data_co2(self):
            i2c_SCL = busio.I2C(board.SCL)
            eco2 = i2c_SCL.adafruit_ccs811()
        def get_data_tvoc(self):
            i2c_SDA = busio.I2C(board.SDA)
            tvoc = i2c_SDA.adafruit_ccs811()
        #def get_data_humidity(self):
            #return self.fakedata.fake_data_float()