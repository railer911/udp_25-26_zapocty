import math
import turtle

def lambert(lon, lat):
    lon = math.radians(lon)
    lat = math.radians(lat)

    denom = 1 + math.cos(lat) * math.cos(lon)

    if denom <= 0:
        raise ValueError

    k = math.sqrt(2 / denom)
    x = k * math.cos(lat) * math.sin(lon)
    y = k * math.sin(lat)

    return x, y

def stereographic(lon, lat):
    lon = math.radians(lon)
    lat = math.radians(lat)

    k = 2 / (1 + math.cos(lat) * math.cos(lon))
    x = k * math.cos(lat) * math.sin(lon)
    y = k * math.sin(lat)

    return x, y

def draw(transform):
    t = turtle.Turtle()
    t.speed(10)
    t.hideturtle()

    SCALE = 180

    for lon in range(u_min, u_max + 1, step):
        first = True
        for lat in range(v_min, v_max + 1, sampling):
            x, y = transform(lon, lat)
            x, y = x * SCALE, y * SCALE

            if first:
                t.penup()
                t.goto(x, y)
                t.pendown()
                first = False
            else:
                t.goto(x, y)

    for lat in range(v_min, v_max + 1, step):
        first = True
        for lon in range(u_min, u_max + 1, sampling):
            x, y = transform(lon, lat)
            x, y = x * SCALE, y * SCALE

            if first:
                t.penup()
                t.goto(x, y)
                t.pendown()
                first = False
            else:
                t.goto(x, y)

screen = turtle.Screen()
screen.setup(900, 700)

u_min = int(input("Min. dĺžka: "))
u_max = int(input("Max. dĺžka: "))
v_min = int(input("Min. šírka: "))
v_max = int(input("Max. šírka: "))

step = int(input("Krok siete: "))
sampling = int(input("Hustota vzorkovania: "))

print("1 - Lambertovo azimutálne")
print("2 - Stereografické azimutálne")
print("3 - Koniec")

choice = input("Voľba: ")

if choice == "1":
    draw(lambert)
if choice == "2":
    draw(stereographic)
if choice == "3":
    print("KONIEC")
else:
    print("zla volba")

screen.mainloop()
