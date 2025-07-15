from abc import ABC, abstractmethod

class SUV(ABC):
    @abstractmethod
    def drive(self):
        pass

class Coupe(ABC):
    @abstractmethod
    def drive(self):
        pass

class CarFactory(ABC):
    @abstractmethod
    def create_suv(self) -> SUV:
        pass

    @abstractmethod
    def create_coupe(self) -> Coupe:
        pass
