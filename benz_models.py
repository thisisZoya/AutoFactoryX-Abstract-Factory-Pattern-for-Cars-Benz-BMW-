from interfaces import SUV, Coupe

class BenzSUV(SUV):
    def drive(self):
        return "Driving Benz SUV with luxury comfort!"

class BenzCoupe(Coupe):
    def drive(self):
        return "Driving Benz Coupe with sporty elegance!"


# === bmw_models.py ===
from interfaces import SUV, Coupe

class BMWSUV(SUV):
    def drive(self):
        return "Driving BMW SUV with dynamic power!"

class BMWCoupe(Coupe):
    def drive(self):
        return "Driving BMW Coupe with aggressive design!"