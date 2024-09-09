import turtle
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# How to get location on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onclick(get_mouse_click_coor)

answer = screen.textinput("Guess the State", "Name a state")



turtle.mainloop()

