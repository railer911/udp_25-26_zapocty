import turtle
import random

turtle.colormode(255)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

enko = 10     
velkost = 500      
turtle.speed(0)
turtle.color(r,g,b)
turtle.hideturtle()
turtle.tracer(True)

def paskal(n):
    trojuholnik = []
    for i in range(n):
        rad = [1]
        if trojuholnik:
            last = trojuholnik[-1]
            rad += [last[j] + last[j+1] for j in range(len(last)-1)]
            rad.append(1)
        trojuholnik.append(rad)

    turtle.penup()
    turtle.goto(-velkost / 2, velkost / 2)
    turtle.pendown()

    for rad in trojuholnik:
        turtle.penup()
        turtle.forward((n - len(rad)) * 20)
        turtle.pendown()
        for cislo in rad:
            turtle.write(cislo, align="center", font=("Courier New", 15, "normal"))
            turtle.penup()
            turtle.forward(40)
            turtle.pendown()
        turtle.penup()
        turtle.backward(len(rad) * 40 + (n - len(rad)) * 20)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.pendown()

def kk(poradie, dlzka):
    if poradie == 0:
        turtle.forward(dlzka)
    else:
        dlzka /= 3
        kk(poradie - 1, dlzka)
        turtle.left(60)
        kk(poradie - 1, dlzka)
        turtle.right(120)
        kk(poradie - 1, dlzka)
        turtle.left(60)
        kk(poradie - 1, dlzka)

def kv(poradie, dlzka):
    for _ in range(3):
        kk(poradie, dlzka)
        turtle.right(120)

def hilbert_L(n, krok):
    if n == 0:
        return
    turtle.right(90)
    hilbert_P(n-1, krok)
    turtle.forward(krok)
    turtle.left(90)
    hilbert_L(n-1, krok)
    turtle.forward(krok)
    hilbert_L(n-1, krok)
    turtle.left(90)
    turtle.forward(krok)
    hilbert_P(n-1, krok)
    turtle.right(90)

def hilbert_P(n, krok):
    if n == 0:
        return
    turtle.left(90)
    hilbert_L(n-1, krok)
    turtle.forward(krok)
    turtle.right(90)
    hilbert_P(n-1, krok)
    turtle.forward(krok)
    hilbert_P(n-1, krok)
    turtle.right(90)
    turtle.forward(krok)
    hilbert_L(n-1, krok)
    turtle.left(90)
def main():
    print("Vyber úlohu:")
    print("1-Pascalov trojuholník")
    print("2-Von Kochova krivka")
    print("3-Von Kochova vločka")
    print("4-Hilbertova krivka")

    choice = int(input("zadaj cislo ulohy: "))
    n = int(input(f"Zadaj max riadkov (<={enko}): "))

    if n > enko:
        print("N prilis vysoke!")
        return

    turtle.clear()
    turtle.penup()
    turtle.goto(-velkost/2, 0)
    turtle.pendown()

    if choice == 1:
        paskal(n)
    elif choice == 2:
        kk(n, velkost)
    elif choice == 3:
        kv(n, velkost)
    elif choice == 4:
        typ = input("Zadaj typ (P / L): ").upper()
        step = velkost / (2 ** n)
        if typ == "P":
            hilbert_P(n, step)
        else:
            hilbert_L(n, step)

    turtle.tracer(True)
    turtle.done()

main()