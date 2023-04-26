class Car:
    no_of_wheels=4
    no_of_objects=0

    def __init__(self, model, brand, year) -> None:
        self.model=model
        self.brand=brand
        self.year=year
        Car.no_of_objects += 1
        
        
    def start_engine(self):
        print(self.brand + " revving!")
    def details(self):
        print("class attribute=", Car.no_of_objects)
        print("object attribute=", self.no_of_objects)

class Electric_Car(Car):
    engine_power=120
    def __init__(self, power, model, brand, year):
        self.power=power
        super().__init__(model, brand, year)
    def start_engine(self):
        print(self.brand+"starts with the power of ", self.power)
        super().start_engine()
    def details(self):
        print("power =", self.power)
        super().details()        
    def charge(self):
        self.power=self.power+5
        print("charged power =", self.power)

class Super_Car(Electric_Car):
    def train(self, AI):
        self.AI=AI
        print("trained")
    pass
        