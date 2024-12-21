class Cage:
    def __init__(self, food_stock, water_stock):
        self.food_stock = food_stock
        self.water_stock = water_stock
    
    def feed(self, animal):
        if self.food_stock > 0:
            animal.eat()
            self.food_stock -= 1
            print(f"поел. остаток: {self.food_stock}.")
        else:
            print("Нет пищи в клетке!")
    
    def give_water(self, animal):
        if self.water_stock > 0:
            animal.drink()
            self.water_stock -= 1
            print(f"попил. остаток: {self.water_stock}.")
        else:
            print("Нет воды в клетке!")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
    
    def eat(self):
        self.health = min(100, self.health + 10)
        print(f"{self.name} поел. здорровье: {self.health}.")
    
    def drink(self):
        self.health = min(100, self.health + 5)
        print(f"{self.name} попил воды и восстановил здоровье. здоровье: {self.health}.")
    
    def check_health(self):
        print(f"Здоровье животного {self.name}: {self.health}.")
    
    def is_alive(self):
        if self.health <= 0:
            print(f"{self.name} погибло!")
            return False
        return True

cage = Cage(5, 3)
leo = Animal("Leo", 3)

for day in range(7):
    print(f"День {day + 1}")
    leo.check_health()
    cage.feed(leo)
    cage.give_water(leo)
    if not leo.is_alive():
        break
