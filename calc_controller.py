# Author: Harvey Ng
# Description: Contains the "controller" of the calculator application. The controller interacts with the model
# and view. It registers the signal of the button press and sends it to the model, which will interpret the button
# press. The controller then tells the view to update itself depending on what the model sends back.

from functools import partial


class CalcController:
    """Controls the interaction between the model and view, updating the view according to the model calculations."""

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_buttons()

    def connect_buttons(self):
        for key in self.view.buttons:
            button = self.view.buttons[key]
            button.clicked.connect(partial(self.button_pressed, key))

    def button_pressed(self, key):
        self.view.set_display(self.model.assign_key(key))