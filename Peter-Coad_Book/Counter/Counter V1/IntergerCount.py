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
        return super().increment()

    def decrement(self):
        self.value -= 1
        return super().decrement()
        
    def reset(self):
        self.value = self.reseted_value
        return super().reset()

intr = Integer_count(1)



import PySimpleGUI as sg
class hic:
    
    layout = [
    [sg.Text("Your Official Integer Counter")],
    [sg.Button("Increment")],
    [sg.Button("Decrement")],
    [sg.Button("Reset")],
    [sg.Output(size=(5))]
    ]

    window = sg.Window("Counter",layout,margins=(30,10))

    while True:
        event, values = window.read()

        if event == "Increment":
            print(intr.increment())
        elif event == "Decrement":
            print(intr.decrement())
        elif event == "Reset":
            print(intr.reset())
        elif event == "OK" or event == sg.WIN_CLOSED:
            break
