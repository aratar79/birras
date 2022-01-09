# imports raspberry
from Services.FakeDataService import FakeDataService

class GasService:

        def __init__(self):
            self.fakedata = FakeDataService()

        def config(self):
            pass

        def get_data_co2(self):
            return self.fakedata.fake_data_float()
        def get_data_tvoc(self):
            return self.fakedata.fake_data_int()
        def get_data_humidity(self):
            return self.fakedata.fake_data_float()