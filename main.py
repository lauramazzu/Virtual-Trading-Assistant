
from turtle import Screen
from user import Player
from messageboard import Messageboard
from user import DrawLine, Line, STARTING_POSITION
import difflib

#**------------------------------- **UI SET UP** --------------------------------**

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#273746")
screen.title("Breakfast Breakout ruler")

screen.tracer(0)
#screen.numinput("Breakfast Breakout virtual assistant", "Hi, I am your virtual trader assistant! Let's get this started")

laura = Player()
mess_board = Messageboard()
aim_line = DrawLine()
line_ = Line()
screen.listen()


screen.onkey(laura.go_up, "Up")


aim_line.drawline()
screen.update()
#**------------------------------- **FUNCTIONALITY** --------------------------------**

#This function is to prevent stopping the loop due to typos
def is_yes_fuzzy(reply):
    return difflib.get_close_matches(reply.lower().strip(), ["yes"], cutoff=0.6) != []


game_is_on = True
while game_is_on:
    skip_to_reply_5 = False
    laura.go_to_start()
    #for each condition, if not passed the turtle should 1.stop moving and 2. pop up text.

    mess_board.welcome()

    reply_0 = screen.textinput("Welcome👋", "Hi there, I am your virtual trader assistant💹🧠"
                                        "\nI am here to assist you in your trading journey."
                                        "\nAre you ready to work on today session? 🚀"
                                        "\nPlease pick up a commodity or stock index.").lower()
    #ask condition 1
    if is_yes_fuzzy(reply_0):
     mess_board.mess_clear()
     mess_board.yes()
     laura.disco_blink()
     screen.update()
    else:
        exit()


    #get rid of the message once you move on
    #ask conditions 2
    reply_1 = screen.textinput("1", "Are the moving averages of the daily graphs"
                                    "\nin agreement with the ones of the 5 mins graph?").lower()

    if is_yes_fuzzy(reply_1):
        mess_board.mess_clear()
        mess_board.move_on()
        laura.go_up()
        laura.disco_blink()
        screen.update()
    else:
        mess_board.mess_clear()
        mess_board.no_agreement()
        reply_6 = screen.textinput("new trade", "Would you like to pick another currency?")
        if is_yes_fuzzy(reply_6):
            mess_board.clear()
            continue
        else:
            mess_board.mess_clear()
            mess_board.bye()
            break

    #ask condition 3
    reply_2 = screen.textinput("2", "Have you plotted the ATR10?"
                                    "\n Make sure that your %risk is up to and no more than 2%").lower()
    if is_yes_fuzzy(reply_2):
        mess_board.mess_clear()
        mess_board.move_on()
        laura.go_up()
        laura.disco_blink()
        screen.update()
    else:
        mess_board.mess_clear()
        mess_board.action_needed()
        reply_7 = screen.textinput("fix ATR", "Would you like to fix this and continue?")
        if is_yes_fuzzy(reply_7):
            mess_board.mess_clear()
            skip_to_reply_3 = True
            laura.go_up()
            laura.disco_blink()
            screen.update()
        else:
            break

    #ask condition 4
    reply_3 = screen.textinput("3",
                               "Now this is a very important step. "
                               "\n You need to check whether you are on small bars or long bars."
                               "\n You place a trade on SMALL bars. "
                               "\n You exit on BIG bars. \n Are you on small bars NOW?").lower()

    skip_to_reply_3 = False
    if is_yes_fuzzy(reply_3):
        mess_board.mess_clear()
        mess_board.move_on()
        laura.go_up()
        laura.disco_blink()
        screen.update()
    else:
        mess_board.mess_clear()
        mess_board.dont_place_step_4()
        reply_8 = screen.textinput("alert", "Should we stop looking at this commodity then? take a note for later.")
        if is_yes_fuzzy(reply_8):
            skip_to_reply_5 = True
            mess_board.mess_clear()
            screen.update()
    #ask condition 5 -

    if not skip_to_reply_5:
        reply_4 = screen.textinput("4", "Now let's have a look if there is some support/resistance level"
                                        "\naround the area we want to trade, as this gives us more assurance."
                                        "\n Is there a support/resistance level?").lower()


        if is_yes_fuzzy(reply_4):
            mess_board.mess_clear()
            mess_board.place_trade()
            laura.go_up()
            laura.disco_blink()
            screen.update()
        else:
            mess_board.mess_clear()
            mess_board.dont_place_step_4()


    #ask condition 6. restart or break the loop
    reply_5 = screen.textinput("next trade", "Would you like to look for another trade now?").lower()

    if reply_5 != "yes":
        mess_board.mess_clear()
        mess_board.bye()
        break
    elif is_yes_fuzzy(reply_5):
        mess_board.mess_clear()
        laura.clear()
        laura.penup()
        laura.setposition(STARTING_POSITION)
        laura.pendown()
        screen.update()




screen.mainloop()
screen.exitonclick()