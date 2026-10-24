# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum

# print(add(1,2,3,4,5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car = Car(make= "NISSAN", model= "GT")

print(my_car.make)