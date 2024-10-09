# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hisrt.jpg', 40)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)
#
#
# print(rgb_colors)


# -------------------------------------------------------------------------------------------------------------------#

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.hideturtle()
tim.penup()
tim.speed("fastest")

tim.setheading(225)

tim.forward(300)

tim.setheading(0)


colors_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5),
          (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),
          (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8),
          (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62),
          (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157),
          (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]

no_of_dots = 100


for dot_count in range(1, no_of_dots+1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
