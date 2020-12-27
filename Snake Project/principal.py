import turtle
import time
import random

# Configuración ventana
w = turtle.Screen()
w.title("Snake Game")
w.bgcolor("black")
w.setup(width = 600, height = 600)
w.tracer(0)
posponer = 0.1

# Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,random.randint(-280,280))

# Segmentos / cuerpo serpiente
segmentos = []

# Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
# Teclado
w.listen()
w.onkeypress(arriba, "Up")
w.onkeypress(abajo, "Down")
w.onkeypress(izquierda, "Left")
w.onkeypress(derecha, "Right")

while True:
    w.update()
    #Colisiones comida
    if cabeza.distance(comida) < 20: # Snake es de 20x20 pixeles
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        nuevo_semgento = turtle.Turtle()
        nuevo_semgento.speed(0)
        nuevo_semgento.shape("square")
        nuevo_semgento.color("grey")
        nuevo_semgento.penup()
        segmentos.append(nuevo_semgento)

    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    mov()
    time.sleep(posponer)
turtle.done()
#input("Press any key to exit ...")
