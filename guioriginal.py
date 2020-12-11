try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog, messagebox

import re
import department_info

LARGE_FONT= ("Verdana", 18)

alistofclasses = []

class Main(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        #now starts tk_example2.py
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Welcomewindow, Departmentinfo, Getschedule):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Welcomewindow)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()   

def remove_punctuation(word):
    """
    Removes punctuation from the string.

    Args: 
        word(str): a word that may contain some punctuation.

    Returns:
        new_word(str): the same word as word but without punctuation.
    """
    
    '''Removing the non alphanumeric characters and converting the string to the lower string'''
    alphanumeric_string  = "".join(e for e in word if e.isalnum()) 
    
    alphanumeric_string = alphanumeric_string.lower() 
    
    return alphanumeric_string

class Welcomewindow(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent) #start of tk_example2.py code
        
        self.canvas = tk.Canvas(self, height = 700, width = 800)
        self.canvas.pack()
        
        #label = tk.Label(self, text="YERRRRRRR", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)
        self.classlistvar = tk.StringVar()
        self.enrolledlistvar = tk.StringVar() 



        
        #OG code (modified)      
        #   list variables
        #self.classlistvar = tk.StringVar()
        #self.enrolledlistvar = tk.StringVar() 
               
        #   frame of the title label
        self.titleFrame = tk.Frame(self, bg = '#80c1ff', bd = 5)
        self.titleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        
        #   title label
        self.titleLabel = tk.Label(self.titleFrame, text = "Welcome to the INST python planner \n Highlight your Class IDs below and press 'add'")   
        self.titleLabel.place(relwidth = 1, relheight = 1)   
        
        #   list of available classes
        self.classlist = tk.Listbox(self, height=5, listvariable = self.classlistvar, selectmode = 'multiple')
        self.classlist.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')    

        #   user selected classes
        self.enrolledlist = tk.Listbox(self, height=5, listvariable = self.enrolledlistvar, selectmode = 'multiple')
        self.enrolledlist.place(x = 500, y = 350, relwidth = .24, relheight = .30, anchor = 'w')
        
        #   addbutton: send one class from classlist to enrolledlist
        self.addButton = tk.Button(self, text = "add", command = lambda: self.get_classes(True))
        self.addButton.place(x = 370, y = 250, relwidth = 0.08, relheight = 0.05)     
        
        #   deletebutton: send one class from enrolledlist to classlist
        self.deleteButton = tk.Button(self, text = "delete", command = lambda:  self.delete_classes(True))
        self.deleteButton.place(x = 370, y = 350, relwidth = 0.08, relheight = 0.05)
        
        #   inserts default values from classes function into the classlistbox
        self.classes()
        
        button = tk.Button(self, text="Department Info", #sends user to department info page
                            command=lambda: [controller.show_frame(Departmentinfo), self.getdepartmentinfo(self.enrolledlistvar)])
        button.place(x = 320, y = 500, relwidth = 0.2, relheight = 0.05)

        button2 = tk.Button(self, text="Get Schedule", #sends user to get schedule page
                            command=lambda: controller.show_frame(Getschedule))
        button2.place(x = 320, y = 550, relwidth = 0.2, relheight = 0.05)
                


    def classes(self):
        
        self.classlistvar.set(value = (301,311,314,326,335)) #    you can also use value = ['A', 'B', 'C']
        self.enrolledlistvar.set(value = ())
    

    def get_classes(self, only_one_item=False):
        
        if self.classlist.curselection() == ():
            return
        
        # get tuple of selected indices
        if only_one_item:
            selection = [self.classlist.curselection()[0]]
        else:
            selection = self.classlist.curselection()
        
        # left all/selected values
        left_value_list = [line.strip(' \'') for line in self.classlistvar.get()[1:-1].split(',')]
        
        left_selected_list = [left_value_list[index] for index in selection]
        
        # values from right side
        right_value_list = [line.strip(' \'') for line in self.enrolledlistvar.get()[1:-1].split(',')]
        right_value_list = [i for i in right_value_list if i.isdigit()]

        # merge w/o duplicates
        result_list = sorted(list(set(right_value_list + left_selected_list)))
        
        self.enrolledlistvar.set(value=result_list)


    def delete_classes(self, only_one_item=False):
        """ This method deletes a class from the enrolled.

        Side effects:
            Alters enrolled list var.
        """
        
        if self.enrolledlist.curselection() == ():
            return
        
        # get tuple of selected indices
        if only_one_item:
            selection = [self.enrolledlist.curselection()[0]]
            
        else:
            selection = self.enrolledlist.curselection()
        
        # right all/selected values
        right_value_list = [line.strip(' \'') for line in self.enrolledlistvar.get()[1:-1].split(',')]
        
        right_selected_list = [right_value_list[index] for index in selection]
        right_value_list = [i for i in right_value_list if i.isdigit()]
        
        # values from left side
        left_value_list = [line.strip(' \'') for line in self.classlistvar.get()[1:-1].split(',')]
        
        # merge w/o duplicates
        result_list = sorted(list(set(right_value_list) - set(right_selected_list)))
        
        self.enrolledlistvar.set(value=result_list)        
        
    
    
    def getdepartmentinfo(self, eclist):
        
        #for i in eclist.get(): 
            #print(f"INST {int}")
           # print(i)
        #print(f"INST {eclist.get().replace("()")}")
        #print(department_info.main(f"INST {eclist.get()}"))
        #print(remove_punctuation(eclist.get()))
        alist = eclist.get().split()
        #print(alist)
        for element in alist:
            alistofclasses.append(f"INST {remove_punctuation(element)}")
        #print(alistofclasses)



class Departmentinfo(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        #   frame of the title label
        self.DItitleFrame = tk.Frame(self, bg = '#80c1ff', bd = 5)
        self.DItitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

        #   title label
        self.DItitleLabel = tk.Label(self.DItitleFrame, text = "INST Department Information")   
        self.DItitleLabel.place(relwidth = 1, relheight = 1) 
        
        button1 = tk.Button(self, text="Back to Welcome Window",
                            command=lambda: controller.show_frame(Welcomewindow))
        button1.pack()

        button2 = tk.Button(self, text="Get Schedule",
                            command=lambda: controller.show_frame(Getschedule))
        button2.pack()
        
        theclasses = department_info.main(i for i in alistofclasses)
        print(theclasses)
        
        button3 = tk.Button(self, text="See department info",
                            command=lambda: self.call_classes(alistofclasses))
        button3.pack()
        
    def call_classes(self, listofclasses):
     
        theclasses = department_info.main(i for i in listofclasses)
        
        print(theclasses)
        
        print_records = ""
        for classes in theclasses:
            print_records += str(classes) + "\n\n"
        query_label = tk.Label(self, text = print_records)
        query_label.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')
        
    
 

    
class Getschedule(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        #   frame of the title label
        self.GStitleFrame = tk.Frame(self, bg = '#80c1ff', bd = 5)
        self.GStitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        #   title label
        self.GStitleLabel = tk.Label(self.GStitleFrame, text = "Here is your INST schedule")   
        self.GStitleLabel.place(relwidth = 1, relheight = 1)   

        button1 = tk.Button(self, text="Back to Welcome Window",
                            command=lambda: controller.show_frame(Welcomewindow))
        button1.pack()

        button2 = tk.Button(self, text="Department Info",
                            command=lambda: controller.show_frame(Departmentinfo))
        button2.pack()


if __name__=="__main__":
    app = Main()
    app.mainloop()
    