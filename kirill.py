class Vehicle:
    __COLOR_VARIANTS = ['purple', 'pink', 'orange', 'brown', 'blue']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя поменять цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Kirill', 'Nissan GTR', 'Red', 600)

vehicle1.print_info()

vehicle1.set_color('BLUE')
vehicle1.set_color('Black')
vehicle1.owner = 'Stepan'

vehicle1.print_info()