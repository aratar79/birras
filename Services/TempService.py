# imports raspberry
# from w1thermsensor import W1ThermSensor
# install the w1thermsensor package to be able to import the library
# pi@raspberrypi:~$ sudo pip3 install w1thermsensor
# for the sensor to work you need to enable One-Wire on the raspberry pi, 
# instructions on this link: https://blog.330ohms.com/2020/06/17/como-habilitar-la-comunicacion-1-wire-en-raspberry-pi/
# configuration on this link: https://es.pinout.xyz/pinout/1_wire or this: https://pypi.org/project/w1thermsensor/
from Services.FakeDataService import FakeDataService
class TempService:

    def __init__(self):
        self.fakedata = FakeDataService()

    def config(self):
        pass

    def get_data(self):
        # sensor = W1ThermSensor()
        # temperature = sensor.get_temperature()
        # return temperature / 1000
        return self.fakedata.fake_data_float()