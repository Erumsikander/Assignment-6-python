
  # 3   -------- Public Variables and Methods ----------

class Car:

    def __init__(self , brand):
        self.brand = brand  #  instense variable

    def start(self):
        print(f"My Car {self.brand} Is Starting Now")

my_car = Car("Revo")
print(my_car.brand)
my_car.start()
