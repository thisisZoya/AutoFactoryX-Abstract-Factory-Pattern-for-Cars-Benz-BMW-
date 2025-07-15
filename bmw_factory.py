from interfaces import CarFactory
from bmw_models import BMWSUV, BMWCoupe

class BMWFactory(CarFactory):
    def create_suv(self):
        return BMWSUV()

    def create_coupe(self):
        return BMWCoupe()