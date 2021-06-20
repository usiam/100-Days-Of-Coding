def add(*args): # args get stored as a tuple
    tot = 0
    for n in args:
        tot += n
    return tot
print(add(1, 2, 3, 4, 5, 6))


class Car:
    def __init__(self, **kwargs): # kwargs get stored as a dictionary
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.seats = kwargs.get('seats')

car = Car(make="Nissan", model="GTR", seats=4)
print(car.seats)
