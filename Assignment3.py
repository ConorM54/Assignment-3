import tkinter

class calendarApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialise()


    def initialise(self):
        self.grid()
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable = self.entryVariable)
        self.entry.grid(column=0,row=0,sticky="EW")
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here")

        button = tkinter.Button(self, text=u'Test Button', command = self.OnButtonClick)
        button.grid(column=1,row=1)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,anchor="w",fg="white",bg = "blue")
        label.grid(column=0, row =1, rowspan=2, sticky = "EW")
        self.labelVariable.set(u"Hello !")


        #Allows user to resize window
        self.grid_columnconfigure(0,weight=1)
        #stops vertical resizing
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())

    def OnButtonClick(self):
       self.labelVariable.set(self.entryVariable.get())

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get())


if __name__ == '__main__':
    app = calendarApp(None)
    app.title ('Calendar App')
    app.mainloop()

        