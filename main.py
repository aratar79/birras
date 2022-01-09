import configparser
import time
from Services.ApiService import ApiService
from Services.GasService import GasService
from Services.TempService import TempService
from Services.ControlTempService import ControlTempService


def main():

    apiSerivice = ApiService()
    tempService = TempService()
    gasService = GasService()
    controlTemp = ControlTempService()

    config = configparser.ConfigParser()
    config.read('config.ini')

    payload = {}
    counter = 0

    while (True):
        beerTemparture = tempService.get_data()
        controlTemp.run(float(beerTemparture))
        servicesData = [beerTemparture, gasService.get_data_co2(),
                        gasService.get_data_tvoc(), gasService.get_data_humidity()]
        for k, v in config.items('BEERVALUES'):
            payload[v] = servicesData[counter]
            print(counter)
            counter += 1
            if(int(counter) == int(len(servicesData))):
                counter = 0;

        #apiSerivice.post_request(payload)
        print(payload)
        time.sleep(1)


if __name__ == '__main__':
    main()
