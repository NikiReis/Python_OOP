from datetime import *

class Count:
    def __init__(self,value):
        self.value = value
        self.reseted_value = value

    def increment(self):
        return self.value

    def decrement(self):
        return self.value

    def reset(self):
        return self.reseted_value


class Date_Count(Count):
    def __init__(self,value):
        super().__init__(
            value 
    )
    def increment(self):
        self.value += timedelta(days=1)
        return super().increment()

    def decrement(self):
        self.value -= timedelta(days=1)
        return super().decrement()
        
    def reset(self):
        self.value = datetime.now()
        return super().reset()

date = datetime.now()
date_obj = Date_Count(date)

import PySimpleGUI as sg
class hic:
    
    layout = [
    [sg.Text("Your Official Integer Counter")],
    [sg.Button("Increment")],
    [sg.Button("Decrement")],
    [sg.Button("Reset")],
    [sg.Output(size=(20,5))]
    ]

    window = sg.Window("Counter",layout,margins=(30,10))

    while True:
        event, values = window.read()

        if event == "Increment":
            print(date_obj.increment())
        elif event == "Decrement":
            print(date_obj.decrement())
        elif event == "Reset":
            print(date_obj.reset())
        elif event == "OK" or event == sg.WIN_CLOSED:
            break