from turtle import Turtle

FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-230, 260)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level {self.level}",align="center",font=FONT)

    def update_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)