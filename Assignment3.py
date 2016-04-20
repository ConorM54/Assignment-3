import tkinter
import calendar 

class calendarApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.labelVariable = tkinter.StringVar()
        self.initialise()


    def initialise(self):
        
        self.monthlabel = tkinter.StringVar()
        self.labelVariable= tkinter.StringVar()
        self.monthlabel.set(u"Choose Month:")

        label = tkinter.Label(self, textvariable= self.monthlabel,anchor="w",fg="white",bg = "gray")
        label.grid(column= 0, row = 0, sticky = "WS", padx= 2)
       
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

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable= self.labelVariable,anchor="w",fg="white",bg = "gray")
        label.grid(column= 0, row = 3, sticky = "WS", padx= 2)
        self.labelVariable.set(u"Choose Date:")
        self.createdateOpt()


        self.createCal()
        self.createEventLog()
        


        #Allows user to resize window
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=2)
        #stops vertical resizing
        self.configure(background = "gray")
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.grid()

    def createCal (self):
        
        self.cal = calendar.TextCalendar(calendar.MONDAY)
        self.c = self.cal.formatmonth(int(self.getYear()), self.monthVal.get())
        displayCalendar = tkinter.Label(self, text= self.c , fg="white",bg = "gray", padx = 3, pady = 3)
        displayCalendar.grid(column = 3, row = 0, columnspan= 2, rowspan= 3, sticky = "EW")

    def createdateOpt (self):

        self.dateVal = tkinter.IntVar()
        self.dateVal.set(1)
        mVal = tkinter.StringVar()
        self.date = tkinter.IntVar()
        dateList = []
        for date in range (1,(calendar.monthrange(int(self.yearVal.get()), int(self.monthVal.get()) )[1]) +1):
            dateList.append(date)
        
        self.dateOpt = tkinter.OptionMenu(self, self.date, *dateList, command= self.setDate)
        self.dateOpt.config(width = 20)
        self.dateOpt.grid(column= 1, row = 3, sticky = "EWS", padx= 2)

    def createEventLog(self):
        self.eventVal = tkinter.StringVar()
        l1= tkinter.Label(self, text= "Events:", fg="white", background = "gray", padx = 3, pady = 3)
        l1.grid(column =0, row = 4, rowspan= 3, sticky = "WS")
        E1 = tkinter.Entry(self, textvariable= self.eventVal)
        E1.grid(column = 1, row = 4, columnspan= 3,rowspan = 3, sticky = "EWS")




    def setYear(self, val):
        self.yearVal.set(val)
        self.createCal()

    def getYear(self):
        return self.yearVal.get()

    def setMonth(self, val):
        for m1 in range(1,13):
            if(val == calendar.month_name[m1]):
                self.monthVal.set(m1)
        self.createCal()
        self.createdateOpt()

    def setDate (self, val):
        self.dateVal.set(val)






if __name__ == '__main__':
    app = calendarApp(None)
    app.title ('Calendar App')
    app.wm_geometry("300x200")
    app.mainloop()

        