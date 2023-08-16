import turtle

# Pencereyi açma
wn = turtle.Screen()
wn.bgcolor("white")

# Kalem ayarları
kalem = turtle.Turtle()
kalem.speed(4)
kalem.color("black")

# Yüz çizimi
kalem.penup()
kalem.goto(0, -100)
kalem.pendown()
kalem.circle(100)

# Sol göz çizimi
kalem.penup()
kalem.goto(-40, 30)
kalem.pendown()
kalem.circle(20)

# Sağ göz çizimi
kalem.penup()
kalem.goto(40, 30)
kalem.pendown()
kalem.circle(20)

# Göz bebekleri çizimi
kalem.penup()
kalem.goto(-30, 50)
kalem.pendown()
kalem.dot(10)

kalem.penup()
kalem.goto(30, 50)
kalem.pendown()
kalem.dot(10)

# Ağız çizimi (gülümseme)
kalem.penup()
kalem.goto(-30, -20)
kalem.pendown()
kalem.setheading(-60)
kalem.circle(30, 120)

# Burun çizimi
kalem.penup()
kalem.goto(0, 10)
kalem.pendown()
kalem.setheading(90)
kalem.forward(20)
kalem.right(90)
kalem.forward(20)
kalem.right(90)
kalem.forward(20)

# Saç çizimi
kalem.penup()
kalem.goto(60, -150)
kalem.pendown()
kalem.setheading(180)
kalem.forward(140)

# Diyaridem yazısı
kalem.penup()
kalem.goto(-10, -150)
kalem.pendown()
kalem.color("black")
kalem.write("Diyaridem", align="center", font=("Arial", 16, "bold"))

# Pencereyi kapatmak için bekletme
turtle.done()
