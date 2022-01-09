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
            self.stop_fan()
        else:
            self.off()
            self.stop_fan()

    def cool(self):
        pass

    def heat(self):
        pass

    def off(self):
        pass

    def start_fan(self):
        pass

    def stop_fan(self):
        pass
