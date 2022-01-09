import configparser
import time
from Services.ApiService import ApiService

def main():
    
    apiSerivice = ApiService()

    config = configparser.ConfigParser() 
    config.read('config.ini') 

    payload = {}

    while (True):

        for k, v in config.items('BEERVALUES'): 
            payload[v] = apiSerivice.fake_data()

        apiSerivice.post_request(payload)   
        time.sleep(1)

if __name__ == '__main__':
    main()
