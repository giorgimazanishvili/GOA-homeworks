#turtle

#left() - მარცხნივ
#right() - მარჯვნივ
#forward() - წინ წასვლა 
#penup() - ფანქრის აღება
#goto() - 
#pendown()

from turtle import *
speed(6)
#square
fillcolor("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

penup()
goto(20 , 110)
pendown()

#windows

fillcolor("brown")
begin_fill()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

penup()
goto(120,110)
pendown()

fillcolor("brown")
begin_fill()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

penup()
goto(70,0)
pendown()


#roof
penup()
goto(0,200)
pendown()
right(225)
forward(142)
right(90)
forward(142)

penup()
goto(0,0)
pendown()

left(135)
forward(230)
left(90)
forward(200)
left(90)
forward(230)
left(90)
forward(200)

penup()
goto(-20 , 110)
pendown()

#windows

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

penup()
goto(-120,110)
pendown()

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

penup()
goto(-70,0)
pendown()
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)

penup()
goto(-400,0)
pendown()

left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

penup()
goto(-380 , 110)
pendown()

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

penup()
goto(-280 , 110)
pendown()


left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

#roof
penup()
goto(-400,200)
pendown()
right(225)
forward(142)
right(90)
forward(142)


penup()
goto(-200,227)
pendown()
left(100)
forward(180)
right(112)
forward(180)























exitonclick()
