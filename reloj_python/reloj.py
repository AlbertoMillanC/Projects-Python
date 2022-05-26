import time
from time import strftime
import turtle

wn = turtle.Screen()
wn.title("Reloj")
wn.bgcolor("SlateGray3")
wn.setup(700, 400)
turtle.hideturtle()
style = "Courier", 30

while True:
    wn.update()
    turtle.write(strftime('%Hh %Mm %Ss'), font=style, align="right")
    time.sleep(0.1)
    turtle.clear()