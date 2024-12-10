import turtle

# Configuración de la ventana
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Esto mejora la velocidad del juego al no actualizar la pantalla automáticamente

# Jugador izquierdo (paleta)
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Jugador derecho (paleta)
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Pelota
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15  # Velocidad de la pelota en el eje X
ball.dy = 0.15  # Velocidad de la pelota en el eje Y

# Velocidades de las paletas (inicialmente 20)
paddle_speed = 20

# Mover la velocidad de la paleta a la parte baja
speed_display = turtle.Turtle()
speed_display.color("white")
speed_display.penup()
speed_display.hideturtle()
speed_display.goto(0, -250)  # Posicionando en la parte baja
speed_display.write(f"Paddle Speed: {paddle_speed}  ¦  'h' : Instrucciones", align="center", font=("Courier", 18, "normal"))

# Movimiento de la paleta izquierda
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += paddle_speed
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= paddle_speed
    left_paddle.sety(y)

# Movimiento de la paleta derecha
def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += paddle_speed
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        y -= paddle_speed
    right_paddle.sety(y)

# Funciones para ajustar la velocidad
def increase_speed():
    global paddle_speed
    paddle_speed += 5
    update_speed_display()

def decrease_speed():
    global paddle_speed
    if paddle_speed > 5:
        paddle_speed -= 5
    update_speed_display()

# Actualizar la pantalla con el nuevo valor de la velocidad
def update_speed_display():
    speed_display.clear()
    speed_display.write(f"Paddle Speed: {paddle_speed}  ¦  'h' : Instrucciones", align="center", font=("Courier", 18, "normal"))

# Asignar las teclas a las funciones
window.listen()
window.onkey(left_paddle_up, "w")
window.onkey(left_paddle_down, "s")
window.onkey(right_paddle_up, "Up")
window.onkey(right_paddle_down, "Down")
window.onkey(increase_speed, "i")  # Tecla "i" para aumentar la velocidad
window.onkey(decrease_speed, "k")  # Tecla "k" para disminuir la velocidad

# Puntuación
left_score = 0
right_score = 0

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

# Actualización de la puntuación
def update_score():
    score_display.clear()
    score_display.write(f"Left: {left_score}  Right: {right_score}", align="center", font=("Courier", 24, "normal"))

# Mostrar instrucciones
def show_instructions():
    global instructions
    instructions = turtle.Turtle()
    instructions.color("white")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -200)  # Ajustando la posición de las instrucciones en la parte baja
    instructions.write("INSTRUCCIONES:\n\n"
                        "1. Usa las teclas 'W' y 'S' para mover la paleta izquierda.\n"
                        "2. Usa las teclas de flecha 'Arriba' y 'Abajo' para mover la paleta derecha.\n"
                        "3. Usa 'I' para aumentar la velocidad de las paletas.\n"
                        "4. Usa 'K' para disminuir la velocidad de las paletas.\n"
                        "5. La velocidad de la pelota aumenta con el tiempo.\n"
                        "6. El juego termina cuando alguien gana 5 puntos.\n"
                        "7. Para salir, presiona 'Esc'.", align="center", font=("Courier", 14, "normal"))

# Función para cerrar las instrucciones
def hide_instructions():
    instructions.clear()  # Solo borra las instrucciones sin afectar el resto del juego

# Asignar las teclas para mostrar y ocultar las instrucciones
window.onkey(show_instructions, "h")  # 'h' para mostrar instrucciones
window.onkey(hide_instructions, "Escape")  # 'Esc' para cerrar instrucciones

# Ciclo principal del juego
while True:
    window.update()

    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Colisiones con los bordes superior e inferior
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Colisión con las paletas
    if (ball.xcor() > 340 and ball.xcor() < 350) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue")
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red")
        ball.dx *= -1

    # Si la pelota sale por el lado izquierdo
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score += 1
        update_score()

    # Si la pelota sale por el lado derecho
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score += 1
        update_score()
