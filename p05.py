# Objektumok
import turtle

class Teglalap():
    alakzat = "téglalap"
    def __init__(self, alap = 10, magassag = 5):
        self.alap = alap
        self.magassag = magassag

    def adatok(self):
        print(f"A {self.alakzat} alapja = {self.alap}")
        print(f"A {self.alakzat} magassága = {self.magassag}")

    def kerulet(self):
        return 2 * self.alap + 2 * self.magassag

    def terulet(self):
        return self.alap * self.magassag


class Negyzet(Teglalap):
    alakzat = "négyzet"
    def __init__(self, alap = 5):
        super().__init__()
        self.alap = alap
        self.magassag = alap

    def adatok(self):
        return print(f"A {self.alakzat} alapja = {self.alap}")

class Haromszog(Teglalap):
    alakzat = "derékszögű háromszög"
    def __init__(self, alap = 10, magassag = 5):
        super().__init__()
        self.alap = alap
        self.magassag = magassag

    def terulet(self):
        return (self.alap * self.magassag) / 2


class MozgoPont(turtle.Turtle):
    def __init__(self, szin, x, y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(5)
        self.goto(x, y)
        self.sebesseg = sebesseg

    def inditas(self):
        self.forward(self.sebesseg)


'''tegla = Teglalap(20, 15)
tegla.adatok()
print("A kerülete = ", tegla.kerulet())
print("A területe = ", tegla.terulet())
print()

negy = Negyzet(8)
negy.adatok()
print("A kerülete = ", negy.kerulet())
print("A területe = ", negy.terulet())
print()

harom = Haromszog()
harom.adatok()
print("A területe = ", harom.terulet())'''
