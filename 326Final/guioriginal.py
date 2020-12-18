try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog, messagebox

import re
import department_info
import schedule

LARGE_FONT= ("Verdana", 18)

#alistofclasses = []

class Main(tk.Tk):
    """
    A class for opening Main window 

    Attributes:
        tk.Tk(): passes in the root of Tkinter
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes Welcomewindow class.
        
        Args:
            args(): passes varible to function
            kwargs(): keyword arguments that passes varible to function
            
        Side effects:
            creates frame
        """
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.alistofclasses = []
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
        """
        Method to show frame.
        
        Args:
            cont(): each frame
        """
        
        frame = self.frames[cont]
        frame.tkraise()   


def remove_punctuation(word):
    """
    Removes punctuation from the string.

    Args: 
        word(str): a word that may contain some punctuation.

    Side effects:
        Modifies characters to lowercase
    
    Returns:
        alphanumeric_string(str): the same word as word but without punctuation.
    """
    
    alphanumeric_string  = "".join(e for e in word if e.isalnum()) 
    
    alphanumeric_string = alphanumeric_string.lower() 
    
    return alphanumeric_string


class Welcomewindow(tk.Frame):
    """
    A class for opening Welcomewindow page.

    Attributes:
        tk.Frame(): inherits tkinter frame attributes
    """
    
    def __init__(self, parent, controller):
        """
        Initializes Welcomewindow class.
        
        Args:
            parent(): 
            controller(): pulls alistofclasses from Main class
            
        Side effects:
            creates buttons and list boxes for welcome window frame
        """
        
        tk.Frame.__init__(self, parent) #start of tk_example2.py code
        
        self.canvas = tk.Canvas(self, height = 700, width = 800)
        self.canvas.pack()

        self.classlistvar = tk.StringVar()
        self.enrolledlistvar = tk.StringVar() 
               
        #   frame of the title label
        self.titleFrame = tk.Frame(self, bg = '#80c1ff', bd = 5)
        self.titleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        
        #   title label
        self.titleLabel = tk.Label(self.titleFrame, text = "Welcome to the INST python planner \n Highlight your Class IDs below and press 'add'")   
        self.titleLabel.place(relwidth = 1, relheight = 1)   
        
        #   list of available items
        self.classlist = tk.Listbox(self, height=5, listvariable = self.classlistvar, selectmode = 'multiple')
        self.classlist.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')    

        #   user selected items
        self.enrolledlist = tk.Listbox(self, height=5, listvariable = self.enrolledlistvar, selectmode = 'multiple')
        self.enrolledlist.place(x = 500, y = 350, relwidth = .24, relheight = .30, anchor = 'w')
        
        #   addbutton: send one class from classlist to enrolledlist
        self.addButton = tk.Button(self, text = "add", command = lambda: self.get_classes(True))
        self.addButton.place(x = 370, y = 250, relwidth = 0.08, relheight = 0.05)     
        
        #   deletebutton: send one class from enrolledlist to classlist
        self.deleteButton = tk.Button(self, text = "delete", command = lambda:  self.delete_classes(True))
        self.deleteButton.place(x = 370, y = 350, relwidth = 0.08, relheight = 0.05)
        
        #   inserts default values from items function into the classlistbox
        self.items()
        
        button = tk.Button(self, text="Department Info", #sends user to department info page
                            command=lambda: [controller.show_frame(Departmentinfo), self.getdepartmentinfo(self.enrolledlistvar, controller)])
        button.place(x = 320, y = 500, relwidth = 0.2, relheight = 0.05)

        self.button2 = tk.Button(self, text="Get Schedule", #sends user to get schedule page
                            command=lambda: [controller.show_frame(Getschedule), self.getdepartmentinfo(self.enrolledlistvar, controller)])
        self.button2.place(x = 320, y = 550, relwidth = 0.2, relheight = 0.05)
                


    def items(self):
        """
        A method to set class values to list
        
        Side effects:
            sets values to attributes
        """
        
        self.classlistvar.set(value = (301,311,314,326,335)) #    you can also use value = ['A', 'B', 'C']
        self.enrolledlistvar.set(value = ())
    

    def get_classes(self, only_one_item=False):
        """ 
        Gets a class from the enrolled list.
        
        Args:
            only_one_item(bool): set to false, can only select one item

        Side effects:
            Alters enrolledlistvar
            
        Returns:
            None: if there is no selection
        """
        
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
        """ 
        Deletes a class from the enrolled list.
        
        Args:
            only_one_item(bool): set to false, can only select one item

        Side effects:
            Alters enrolledlistvar
            
        Returns:
            None: if there is no selection
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
        
    
    
    def getdepartmentinfo(self, eclist, controller):
        """
        Creates separate strings of selected values into a list
        
        Args:
            eclist(string): contains the selected values along with extra punctuation
            controller(): pulls alistofclasses from Main class
            
        Side effects:
            Splits eclist into separate strings and appends to a list with correct name
        """
        
        alist = eclist.get().split()
        for element in alist:
            controller.alistofclasses.append(f"INST {remove_punctuation(element)}")


class Departmentinfo(tk.Frame):
    """
    A class for opening Departmentinfo page.

    Attributes:
        tk.Frame(): inherits tkinter frame attributes
    """
    
    def __init__(self, parent, controller):
        """
        Initializes Departmentinfo class.
        
        Args:
            parent(): 
            controller(): pulls alistofclasses from Main class
            
        Side effects:
            creates buttons and list boxes for Departmentinfo frame
        """
        
        self.print_records = ""
        tk.Frame.__init__(self, parent)
        #   frame of the title label
        self.DItitleFrame = tk.Frame(self, bg = '#80c1ff', bd = 5)
        self.DItitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.08, anchor = 'n')

        #   title label
        self.DItitleLabel = tk.Label(self.DItitleFrame, text = "INST Department Information")   
        self.DItitleLabel.place(relwidth = 1, relheight = 1) 
        
        self.query_label = tk.Label(self, text = "")
        self.query_label.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')
        
        self.button1 = tk.Button(self, text="Back to Welcome Window",
                            command=lambda: [controller.show_frame(Welcomewindow), self.clear_list(controller)])
        self.button1.pack()

        self.button2 = tk.Button(self, text="Get Schedule",
                            command=lambda: controller.show_frame(Getschedule))
        self.button2.pack()
        
        self.button3 = tk.Button(self, text="See Department Info",
                            command=lambda: self.call_classes(controller.alistofclasses))
        self.button3.pack()
        
        self.delete_button = tk.Button(self, text = "Clear List",
                                       command=lambda: self.delete_list())
        self.delete_button.pack()
        
        
    def delete_list(self):
        """
        Gets rid of text and label.
    
        Side effects:
            enables See Department Info button to clear to normal
        """
        self.query_label.destroy()
        self.button3['state'] = 'normal'
        self.print_records = ""
    
    
    def call_classes(self, classesfrombutton):
        """
        Pulls classes from selected values.
    
        Args:
            classesfrombutton(list): list of classes chosen
            
        Side effects():
            Disables the See Department Info button after it is clicked
            Prints text from label
        """
        
        theschedule = department_info.main(i for i in classesfrombutton)
        
        #print(theschedule)
        
        for items in theschedule:
            self.print_records += str(items) + "\n\n"
        
        self.query_label = tk.Label(self, text = self.print_records)
        self.query_label.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')
        self.button3['state'] = 'disabled'
        
    
    def clear_list(self, controller):
        """
        Clears controller.alistofclasses.
        
        Args:
            controller(): pulls alistofclasses from Main class
            
        Side effects:
            Sets self.print_records to an empty string
        """
        controller.alistofclasses.clear()
        self.print_records = ""
        #self.query_label = tk.Label(self, text = "")
        #self.query_label.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')
        
        
class Getschedule(tk.Frame):
    """
    A class for opening Getschedule page.

    Attributes:
        tk.Frame(): inherits tkinter frame attributes
    """
    
    def __init__(self, parent, controller):
        """
        Initializes Getschedule class.
        
        Args:
            parent(): 
            controller(): pulls alistofclasses from Main class
            
        Side effects:
            creates buttons and list boxes for Getschedule frame
        """
        
        tk.Frame.__init__(self, parent)
        
        self.print_schedule = ""
        
        #   frame of the title label
        self.GStitleFrame = tk.Frame(self, bg = '#80c1ff', bd = 5)
        self.GStitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        #   title label
        self.GStitleLabel = tk.Label(self.GStitleFrame, text = "Here is your INST schedule")   
        self.GStitleLabel.place(relwidth = 1, relheight = 1)   
        
        #self.textbox = tk.Text(self, height = 30, width = 30)
        #self.textbox.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')

        self.button1 = tk.Button(self, text="Back to Welcome Window",
                            command=lambda: [controller.show_frame(Welcomewindow), self.clear_list(controller)])
        self.button1.pack()

        self.button2 = tk.Button(self, text="Department Info",
                            command=lambda: controller.show_frame(Departmentinfo))
        self.button2.pack()
        
        self.button3 = tk.Button(self, text = "Get Your Schedule",
                            command=lambda: self.get_schedule(controller.alistofclasses))
        self.button3.pack()
        
        self.delete_button = tk.Button(self, text = "Clear List",
                                       command=lambda: self.delete_list(controller.alistofclasses))
        self.delete_button.pack()
        
        
    def delete_list(self, controller):
        """
        Gets rid of text and label.
    
        Side effects:
            enables See Department Info button to clear to normal
        """
        
        self.show_schedule.destroy()
        self.button3['state'] = 'normal'
        self.print_schedule = ""
        
    def get_schedule(self, thelist):
        """
        Pulls classes from selected values.
    
        Args:
            thelist(list): list of classes chosen
            
        Side effects():
            Disables the See Department Info button after it is clicked
            Prints text from label
        """
        
        theschedule = schedule.main(i for i in thelist)
        
        #print(theschedule)
        
        for items in theschedule:
            self.print_schedule += str(items) + "\n\n"
        
        
        """     Treeview
        self.schedtree = ttk.Treeview(self)
        self.schedtree['columns'] = ("Subject","Assignment","Time Due","Due Date","Weight","Type")
        
        self.schedtree.column("#0", width = 0)
        self.schedtree.column("Subject", anchor = 'w', width = 120)
        self.schedtree.column("Assignment", anchor = 'w', width = 120)
        self.schedtree.column("Time Due", anchor = 'w', width = 120)
        self.schedtree.column("Due Date", anchor = 'w', width = 120)
        self.schedtree.column("Weight", anchor = 'w', width = 120)
        self.schedtree.column("Type", anchor = 'w', width = 120)
        
        self.schedtree.heading("#0", text = "")
        self.schedtree.heading("Subject", text = "Subject", anchor = 'w')
        self.schedtree.heading("Assignment", text = "Assignment", anchor = 'w')
        self.schedtree.heading("Time Due", text = "Time Due", anchor = 'w')
        self.schedtree.heading("Due Date", text = "Due Date", anchor = 'w')
        self.schedtree.heading("#Weight", text = "Weight", anchor = 'w')
        self.schedtree.heading("Type", text = "Type", anchor = 'w')
        
        self.schedtree.insert(parent = '', index = 'end', iid = 0, text = "", values = self.print_schedule)
        """
        
        """ Works incorrectly
        testbox = tk.Listbox(self)
        for x,y in enumerate(self.print_schedule):
            testbox.insert(x+1,y)
        testbox.place(x = 400, y = 700, relwidth = .6, relheight = .75, anchor = 's')
        """
        
        self.textbox = tk.Text(self, height = 30, width = 30)
        self.textbox.place(x = 400, y = 700, relwidth = .8, relheight = .75, anchor = 's')
        self.textbox.insert('end', self.print_schedule)


        """ Works incorrectly
        self.sched = tk.StringVar(self, value= self.print_schedule)
        self.schedbox = tk.Listbox(self, listvariable = self.sched)
        self.schedbox.place(x = 400, y = 700, relwidth = .6, relheight = .75, anchor = 's')
        """
            
        #self.schedbox.insert(self.schedbox, self.print_schedule)
        
            
        #self.scrollbar = tk.Scrollbar(self, orient = 'vertical')
        #self.show_schedule = tk.Text(self, text = self.print_schedule, yscrollcommand = self.scrollbar.set)
        #self.scrollbar.config(self, command = self.show_schedule.yview)
        #self.scrollbar.pack(self, side = 'RIGHT', fill = 'Y')
        #self.show_schedule.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')
        
        self.button3['state'] = 'disabled'
        
        
    def clear_list(self, controller):
        """
        Clears controller.alistofclasses.
        
        Args:
            controller(): pulls alistofclasses from Main class
            
        Side effects:
            Sets self.print_records to an empty string
        """
        
        controller.alistofclasses.clear()
        self.print_schedule = ""


if __name__=="__main__":
    app = Main()
    app.mainloop()