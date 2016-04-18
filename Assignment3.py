import tkinter

class calendarApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialise()


    def initialise(self):
        pass


if __name__ == '__main__':
    app = calendarApp(None)
    app.title ('Calendar App')
    app.mainloop()

        