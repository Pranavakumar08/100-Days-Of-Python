from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_no = random.randint(1,6)
        if random_no == 1:    # This condition is written so that lesser cars are created because without this, after every update, a car will be cerated.
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=3)
            car.color(random.choices(COLORS))
            car.penup()
            car.start_y = random.randint(-250,250)
            car.goto(300,car.start_y)
            self.cars_list.append(car)

    def move(self):
        for car in self.cars_list:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x,car.start_y)

    def update_speed(self):
        self.move_speed += MOVE_INCREMENT