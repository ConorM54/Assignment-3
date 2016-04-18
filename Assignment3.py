import tkinter

class calendarApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialise()


    def initialise(self):
        self.grid()

        self.entry = tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky="EW")

        button = tkinter.Button(self, text=u'Test Button')
        button.grid(column=1,row=1)


if __name__ == '__main__':
    app = calendarApp(None)
    app.title ('Calendar App')
    app.mainloop()

        