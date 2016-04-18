import tkinter

class calendarApp(tkinkter.TK):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialise()


    def initialise(self):
        pass


if __name__ == '__main__':
    app = calendarApp()
    app.title ('Calendar App')

        