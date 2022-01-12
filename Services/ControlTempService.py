import configparser
import RP1.GPIO as gp

class ControlTempService:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.stable_temp = float(self.config.get('BEERSETTINGS', 'STABLE_TEMP'))
        gp.setmode(gp.BOARD)
        gp.setup(18,GPIO.OUT)
        gp.setup(23,GPIO.OUT)
        gp.setup(24,GPIO.OUT)
        gp.setup(25,GPIO.OUT)

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
        gp.output(18, True)

    def heat(self):
        gp.output(23, True)

    def off(self):
        gp.output(18, True)
        gp.output(23, True)

    def start_fan(self):
        gp.output(24, True)
        gp.output(25, True)

    def stop_fan(self):
        gp.output(24, False)
        gp.output(25, False)
