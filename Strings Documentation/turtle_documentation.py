from turtle import *

screen = Screen()

# create turtle named adam
adam = Turtle(shape="turtle")
#change adam color
adam.color("purple")

# create turtle named eve
eve = Turtle(shape="turtle")
eve.color("red")



# #move adam forward
# adam.fd(400)
#
# #move adam backward
# adam.bk(800)

adam.goto(50, 50)
eve.goto(-50, -100)

screen.onclick(eve.goto)
screen.listen()
mainloop()