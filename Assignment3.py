import tkinter
import calendar 

class calendarApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.labelVariable = tkinter.StringVar()
        self.initialise()


    def initialise(self):
        
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable= self.labelVariable,anchor="w",fg="white",bg = "gray")
        label.grid(column= 0, row = 0, sticky = "WS", padx= 2)
        self.labelVariable.set(u"Choose Month:")

        self.monthVal = tkinter.IntVar()
        self.monthVal.set(1)
        mVal = tkinter.StringVar()
        
        monthList = []
        for month in range(1,13):
            monthList.append(calendar.month_name[month])
        self.monthsOpt = tkinter.OptionMenu(self, mVal, *monthList, command= self.setMonth)
        self.monthsOpt.grid(column= 1, row = 0, sticky = "EWS", padx= 2)

       
        label = tkinter.Label(self, textvariable= self.labelVariable,anchor="w",fg="white",bg = "gray")
        label.grid(column= 0, row = 1, sticky = "WS", padx= 2)
        self.labelVariable.set(u"Choose Year:")

        self.yearVal = tkinter.StringVar()
        self.yearVal.set(2015)
        yearList = []
        for year in range(2016,2026):
            yearList.append(year)
            
        self.yearOpt = tkinter.OptionMenu(self, self.yearVal, *yearList, command = self.setYear)
        self.yearOpt.grid(column= 1, row = 1, sticky = "EWS", padx= 2)

        self.createCal()
        

        """self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,anchor="w",fg="white",bg = "blue")
        label.grid(column=0, row =1, rowspan=2, sticky = "SEW")
        self.labelVariable.set(u"Hello !")"""


        #Allows user to resize window
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=2)
        #stops vertical resizing
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.grid()

    def createCal (self):
        
        self.cal = calendar.TextCalendar(calendar.MONDAY)
        self.c = self.cal.formatmonth(int(self.getYear()), self.monthVal.get())
        displayCalendar = tkinter.Label(self, text= self.c , fg="white",bg = "red", padx = 3, pady = 3)
        displayCalendar.grid(column = 3, row = 0, columnspan= 2, rowspan= 3, sticky = "EW")


    def OnButtonClick(self):
       self.labelVariable.set(self.entryVariable.get())

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get())

    def setYear (self, val):
        self.yearVal.set(val)
        self.createCal()

    def getYear(self):
        return self.yearVal.get()

    def setMonth(self, val):
        for m1 in range(1,13):
            if(val == calendar.month_name[m1]):
                self.monthVal.set(m1)
        print (self.monthVal.get())




if __name__ == '__main__':
    app = calendarApp(None)
    app.title ('Calendar App')
    app.wm_geometry("400x200")
    app.mainloop()

        