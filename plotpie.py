import turtle as turtle
import math
import time

time.sleep(5)
turtle.hideturtle()
turtle.speed(100)


class MoonCake:
    def __init__(self, name: str):
        self.name = name

    # 绘制月饼的外部花边
    def external_pattern(self, r: int, n: int):
        turtle.penup()
        turtle.goto(0, -r)
        turtle.pendown()

        round_r = math.sin(math.pi / n) * r

        for i in range(n):
            turtle.penup()
            turtle.home()
            turtle.seth((360 / n) * i)
            turtle.fd(r)
            turtle.left((360 / n) * 0.5)
            turtle.pendown()
            turtle.color('#F0BE7C')
            turtle.begin_fill()
            turtle.circle(round_r, 180)
            turtle.end_fill()

    # 绘制月饼内部的纹理
    def internal_pattern(self):
        turtle.color('#F5E16F')
        turtle.goto(0, -180)
        for _ in range(8):
            turtle.begin_fill()
            turtle.circle(60, 120)
            turtle.left(180)
            turtle.circle(60, 120)
            turtle.end_fill()

    # 半径、线条大小和颜色
    def draw_circle(self, r: int, pensize: int, color1: str, color2: str):
        turtle.penup()
        turtle.goto(0, -r)
        turtle.seth(0)
        turtle.pendown()
        turtle.pensize(pensize)
        turtle.color(color1, color2)
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

    """
    def draw(self):
        turtle.title("2023年双节高速堵爆了！！！")
        self.external_pattern(200, 12)
        self.draw_circle(200, 10, '#F0BE7C', '#F0BE7C')
        self.draw_circle(180, 10, '#F8CD32', '#FBA92D')
        self.internal_pattern()
        self.write_text(-105, -60)
        turtle.done()
    """

    def write_text(self):
        turtle.penup()
        turtle.goto(0, -80)
        turtle.pendown()
        turtle.color('Gold')
        turtle.write(self.name, align="center", font=("华文隶书", 54, "bold"))

    def draw(self):
        turtle.title("2023年双节高速堵爆了！！！")
        self.external_pattern(200, 12)
        self.draw_circle(200, 10, '#F0BE7C', '#F0BE7C')
        self.draw_circle(180, 10, '#F8CD32', '#FBA92D')
        self.internal_pattern()
        self.write_text()
        time.sleep(5)  # Pause for 5 seconds after the entire drawing is complete
        turtle.done()

MoonCake('中秋节\n快乐吖').draw()
if __name__ == '__main__':
    MoonCake('中秋节\n快乐吖').draw()

