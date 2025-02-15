class Car:

    Total_Account = 0

    def __init__(self, __brand, __model):
        self.__brand = __brand
        self.model = __model
        Car.Total_Account += 1

    def fullname(self):
        return f"{self.__brand} {self.model}"

    def get_brnd(self):
        return self.__brand

    def Fuel(self):
        return "This Fuel is a car"

    @staticmethod
    def static():
        return "This is a static method"
    
    
    @property
    def notchange(self):
      return self.__brand


class On_more_add(Car):
    def __init__(self, __band, model, color):
        super().__init__(__band,model)
        self.color = color

    def Electric(self):
        return "This Electric is a car"
    
    def getdata(self):
        return f"{self.fullname()} {self.color}"


# add_more_car = On_more_add("Tesla", "Model S", "Red")
# # print(add_more_car.get_brnd())
# print(isinstance(add_more_car, Car))
# print(isinstance(add_more_car, On_more_add))


class bettery:
    def bettery_into(self):
        return "This is a bettery"
    
    
class Engine:
    def Engine(self):
        return "This is a Engine"
    
class combilne(bettery, Engine,Car):
    pass


test=combilne("Tesla", "Model S")
print(test.bettery_into())
print(test.Engine())


    
    
 
    







































# print("----------------------------------------")


# carfun = Car("Tesla", "Model S")
# print(carfun.Fuel())


# carfun1 = Car("Tesla", "Model S")
# carfun1.__brand="Toyota"
# print(carfun1.notchange)


# print("----------------------------------------")
# print(Car.Total_Account)


# carfun = Car("Tesla", "Model S")
# print(carfun.static())
