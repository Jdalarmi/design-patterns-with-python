from abc import ABC, abstractmethod


class Tires(ABC):
    @abstractmethod
    def type(self) -> str:
        pass


class Engine(ABC):
    @abstractmethod
    def horsepower(self) -> str:
        pass


class LuxuryTire(Tires):
    def type(self) -> str:
        return 'Luxury Michellin Tires'


class LuxuryEngine(Engine):
    def horsepower(self) -> str:
        return '350 HP Twin Turbo Engine'


class EconomyTire(Tires):
    def type(self) -> str:
        return 'Economy Hankook tires'

class EconomyEngine(Engine):
    def horsepower(self) -> str:
        return '100HP Fuel Efficient engine'


class VehicleFactory(ABC):
    @abstractmethod
    def create_tire(self) -> Tires:
        pass

    @abstractmethod
    def create_engine(self) -> Engine:
        pass


class LuxuryCarFactory(VehicleFactory):
    def create_tire(self) -> Tires:
        return LuxuryTire()

    def create_engine(self) -> Engine:
        return LuxuryEngine()


class EconomyCarFactory(VehicleFactory):
    def create_tire(self) -> Tires:
        return EconomyTire()

    def create_engine(self) -> Engine:
        return EconomyEngine()


def audi_assemble_car(factory: VehicleFactory):
    tire = factory.create_tire()
    engine = factory.create_engine()

    print(f'Create car with {tire.type()} and {engine.horsepower()}')

def chevrolet_assemble_car(factory: VehicleFactory):
    tire = factory.create_tire()
    engine = factory.create_engine()

    print(f'Create car with {tire.type()} and {engine.horsepower()}')


if __name__ == "__main__":
    print("Starting assembly Audi RS3")
    luxury_factory = LuxuryCarFactory()
    audi_assemble_car(luxury_factory)
    print()
    print("Starting assembly Onix")
    economy_factory = EconomyCarFactory()
    chevrolet_assemble_car(economy_factory)
