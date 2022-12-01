from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)

for step in range(6):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)


write(0)
forward(100)
write(5)

write(0)
forward(20)
write(1)
forward(20)
write(2)
forward(20)
write(3)
forward(20)
write(4)
forward(20)
write(5)
forward(20)

Raphael = Turtle()
Raphael.color('red')
Raphael.shape('turtle')

Raphael.penup()
Raphael.goto(-160, 100)
Raphael.pendown()

Michelangelo = Turtle()
Michelangelo.color('orange')
Michelangelo.shape('turtle')

Michelangelo.penup()
Michelangelo.goto(-160, 10)
Michelangelo.pendown()

Donatello = Turtle()
Donatello.color('purple')
Donatello.shape('turtle')

Donatello.penup()
Donatello.goto(-160, 40)
Donatello.pendown()

Leonardo = Turtle()
Leonardo.color('blue')
Leonardo.shape('turtle')

Leonardo.penup()
Leonardo.goto(-160, 70)
Leonardo.pendown()

for turn in range(100):
    Raphael.forward(randint(1,5))
    Leonardo.forward(randint(1,5))
    Donatello.forward(randint(1,5))
    Michelangelo.forward(randint(1,5))