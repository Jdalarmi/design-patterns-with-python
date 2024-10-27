from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def specification(self) -> str:
        pass


class Car(Vehicle):
    def specification(self) -> str:
        return "This car is a GLI"
    

class Bike(Vehicle):
    def specification(self)-> str:
        return "This CJ Honda bike"
    
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()
    
class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()
    
class VehicleFactoryBuilder:
    @staticmethod
    def get_factory(type: str) -> VehicleFactory:
        if type == "car":
            return CarFactory()
        elif type == "bike":
            return BikeFactory()
        else:
            raise ValueError("Tipo de veículo desconhecido")

def client():
    type_car = "car"
    factory = VehicleFactoryBuilder.get_factory(type_car)
    car = factory.create_vehicle()
    print(car.specification())

if __name__ == "__main__":
    client() 