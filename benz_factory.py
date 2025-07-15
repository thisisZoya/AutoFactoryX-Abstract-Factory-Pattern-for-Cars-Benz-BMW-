from interfaces import CarFactory
from benz_models import BenzSUV, BenzCoupe

class BenzFactory(CarFactory):
    def create_suv(self):
        return BenzSUV()

    def create_coupe(self):
        return BenzCoupe()