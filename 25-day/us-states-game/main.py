import turtle
import pandas
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

data = pandas.read_csv("50_states.csv")
data_states = data.state.to_list()


guessed_states = []
while len(guessed_states) < 50:

    answer = screen.textinput(f"{len(guessed_states)}/50 states guessed correctly", "Name a state").title()

    if answer == "Exit":
        not_guessed = []
        for state in data_states:
            if state not in guessed_states:
                not_guessed.append(state)
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("new_csv.csv")

        break

    if answer in data_states:
        guessed_states.append(answer)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        attr = data[data.state == answer]
        # tim.goto(int(attr.x), int(attr.y)) or
        tim.goto(int(attr.x.iloc[0]), int(attr.y.iloc[0]))
        tim.write(answer)

