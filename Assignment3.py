# Main Method

from tkinter import *
 

class Example(Frame):

    

    def __init__(self, parent):

        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.parent.title("Calendar Planner")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        w = Label(self, text="Rouge", fg="red")
        w = Label(self, text="Helvetica", font=("Helvetica", 16))

        # create a menu
        """menu = Menu(self)
        self.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=callback)
        filemenu.add_command(label="Open...", command=callback)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=callback)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=callback)"""


       

        

    def centerWindow(self):
      
        w = 500
        h = 500

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #self.bind("<Button-1>", centerWindow)   





def main():
  
    root = Tk()
    ex = Example(root)

      
    
    root.mainloop()    


if __name__ == '__main__':
    main()  