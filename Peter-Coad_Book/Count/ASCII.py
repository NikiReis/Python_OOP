import random
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

class Integer_count(Count):
    def __init__(self,value):
        super().__init__(
            value
    )
    def increment(self):
        self.value += 1
        print(chr(self.value))

    def decrement(self):
        self.value -= 1
        print(chr(self.value))
        
    def reset(self):
        self.value = self.reseted_value
        print(chr(self.value))


a = random.randint(0,100)
intr = Integer_count(a)


import PySimpleGUI as sg
class hic:
    
    layout = [
    [sg.Text("Your Official Integer Counter")],
    [sg.Button("Increment")],
    [sg.Button("Decrement")],
    [sg.Button("Reset")],
    [sg.Output(size=(5))]
    ]

    window = sg.Window("Counter",layout,margins=(50,0))
    while True:
        event, values = window.read()
        
        if event == "Increment":
            intr.increment()
        elif event == "Decrement":
            intr.decrement()
        elif event == "Reset":
            intr.reset()
        elif event == "OK" or event == sg.WIN_CLOSED:
            break