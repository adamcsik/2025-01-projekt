# 4. alkalom
'''
def negyszog(a, b):
    ker = 2 * a + 2 * b
    ter = a * b
    alakzat = "téglalap"
    if a == b:
        alakzat = "négyzet"
    return ker, ter, alakzat


def szamolas(*args):
    osszeg = sum(args)
    legnagyobb = max(args)
    return osszeg, legnagyobb


if __name__ == "__main__":
    sorozat = [1,2,"három",4,5]
    for elem in sorozat:
        print(elem)

    for i in range(1, 11, 3):
        print(i)

    for _ in range(10):
        print("Nem leszek rossz!")


    print("Összeg:", szamolas(1, 2, 3, 4, 5)[0])
    print("A legnagyobb érték:", szamolas(1, 2, 3, 4, 5)[1])

    eredmeny = negyszog(4, 4)
    print("Kerület:", eredmeny[0])
    print("Terület:", eredmeny[1])
    print("Alakzat:", eredmeny[2])
'''

import turtle
import random

def negyzet():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(5)

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def pont(x , y):
    turtle.goto(x, y)
    turtle.dot(10, "black")

def dobas():
    turtle.clear()
    turtle.hideturtle()
    negyzet()
    szam = random.randint(1, 6)
    turtle.penup()

    if szam == 1:
        pont(0,0)
    elif szam == 2:
        pont(-30, 30)
        pont(30, -30)
    elif szam == 3:
        pont(-30, 30)
        pont(30, -30)
        pont(0, 0)

ablak = turtle.Screen()

dobas()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye,"Escape")

turtle.listen()
turtle.mainloop()


