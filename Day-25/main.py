import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # the path to the gif file
screen.addshape(image)  # this adds a new shape to the turtle
turtle.shape(image)


# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor) # this tracks the coordinates of where you click on the screen


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct",
                                    prompt="What is another State's name").title()

    if answer_state == "Exit":
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)

        # doing the above code using list comprehension
        missing_state = [state for state in all_states if state not in guessed_state]

        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    # if answer_state is one of the states in 50_states.csv
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()  # create a turtle that writes the name at the x and y cor
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(answer_state)  # OR t.write(state_data.state.item())
