import random

class FakeDataService:

    def __init__(self):
        pass

    def fake_data_int(self):
        result = random.randint(-10, 50)
        return result

    def fake_data_float(self):
        result = random.randint(-100, 500)
        return result / 100