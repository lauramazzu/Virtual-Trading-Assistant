from  turtle import Turtle

FONT_POPUP = ("Comic Sans MS", 18, "normal")
FONT_POPUP_2 = ("Comic Sans MS", 14, "normal")
FONT_TITLE = ("Comic Sans MS", 18, "bold")

#display messages
class Messageboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("#FF5733")
        self.goto(0, 250)
        self.hideturtle()


    def welcome(self):
        self.write("WELCOME TO THE BREAKFAST BREAKOUT VIRTUAL ROOM!", align="center", font= FONT_TITLE)

    def action_needed(self):
        #remain in the current position
        #text pop up

        self.write(f"PLEASE DO IT", align= "center", font = FONT_POPUP)

    def move_on(self):
        #allowed to go forward
        #text pop up

        self.write(f"Great! You can move to the next step", align="center", font = FONT_POPUP)

    def yes(self):
        self.write(f"Great! Let's crack on", align="center", font=FONT_POPUP)

    def mess_clear(self):
        self.clear()

    def place_trade(self):
        self.write("Awesome!✅ You are good to go and place the trade.🔥\n"
                   "But remember that regardless of this checklist you are the one taking the decision! \n"
                   "Trading involves risk and you may lose all your capital.", align= "center", font = FONT_POPUP_2)

    def dont_place_step_4(self):
        self.write("Alright, it would be better to have this condition satisfied."
                   "\n Remember that trading involve risk.", align= "center", font = FONT_POPUP_2)

    def bye(self):
        self.write("Enjoy the rest of your day, then! \n See you again tomorrow!", align= "center", font = FONT_POPUP)

    def no_agreement(self):
        self.write("⛔if this condition is not met I recommend you"
                   "\nnot to carry on looking at this trade at this time.", align = "center", font = FONT_POPUP_2)