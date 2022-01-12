import configparser
#import RP1.GPIO as gp

class ControlTempService:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.stable_temp = float(self.config.get('BEERSETTINGS', 'STABLE_TEMP'))
        #gp.setmode(gp.BOARD)
        #gp.setup(12,gp.OUT)
        #gp.setup(32,gp.OUT)

    def run(self, temp):
        if(temp > self.stable_temp):
            self.cool()
            self.start_fan()
        elif(temp < self.stable_temp):
            self.heat()
            self.start_fan()
        else:
            self.off()
            self.stop_fan()

    def cool(self):
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.IN)
    def heat(self):
        GPIO.setup(18,GPIO.IN)
        GPIO.setup(23,GPIO.OUT)

    def off(self):
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)

    def start_fan(self):
        GPIO.setup(24,GPIO.IN)
        GPIO.setup(25,GPIO.IN)

    def stop_fan(self):
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
