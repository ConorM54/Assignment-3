import tkinter
import calendar 

class calendarApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialise()


    def initialise(self):
        
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable= self.labelVariable,anchor="w",fg="white",bg = "gray")
        label.grid(column= 0, row = 0, sticky = "WS", padx= 2)
        self.labelVariable.set(u"Choose Month:")

        self.monthVal = tkinter.StringVar()
        
        monthList = []
        for month in range(1,13):
            monthList.append(calendar.month_name[month])
        self.monthsOpt = tkinter.OptionMenu(self, self.monthVal, *monthList)
        self.monthsOpt.grid(column= 1, row = 0, sticky = "EWS", padx= 2)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable= self.labelVariable,anchor="w",fg="white",bg = "gray")
        label.grid(column= 0, row = 1, sticky = "WS", padx= 2)
        self.labelVariable.set(u"Choose Year:")

        self.yearVal = tkinter.StringVar()
        yearList = []
        for year in range(2016,2026):
            yearList.append(year)
            
        self.yearOpt = tkinter.OptionMenu(self, self.yearVal, *yearList)
        self.yearOpt.grid(column= 1, row = 1, sticky = "EWS", padx= 2)

        self.cal = calendar.TextCalendar(calendar.MONDAY)
        c = self.cal.formatmonth(2015, 1)
        displayCalendar = tkinter.Label(self, textvariable= c,fg="white",bg = "gray")
        displayCalendar.grid(column = 3, row = 0, rowspan= 3, sticky = "EW")


        """self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,anchor="w",fg="white",bg = "blue")
        label.grid(column=0, row =1, rowspan=2, sticky = "SEW")
        self.labelVariable.set(u"Hello !")"""


        #Allows user to resize window
        #self.grid_columnconfigure(0,weight=1)
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_columnconfigure(2,weight=1)
        #stops vertical resizing
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.grid()

    def OnButtonClick(self):
       self.labelVariable.set(self.entryVariable.get())

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get())


if __name__ == '__main__':
    app = calendarApp(None)
    app.title ('Calendar App')
    app.wm_geometry("400x200")
    app.mainloop()

        