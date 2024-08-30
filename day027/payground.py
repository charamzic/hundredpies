class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
        self.year = kwargs.get("year")
        self.price = kwargs.get("price")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"


car = Car(make="Toyota", model="Corolla", color="Red", seats=4, year=2019, price=20000)
print(car.__str__())
