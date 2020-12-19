"""
Final Project
Group 2: Assigment Tracker
Brook Goitom | Emmanuel Sitaniapessy | Jenny Dang | Nicholas Wang
INST 326
Professor Cruz
"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinter import ttk, filedialog, messagebox

import re
import department_info
import schedule

LARGE_FONT= ("Verdana", 18)


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
        self.user_classes = [] #holds the INST classes the user selects
        
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
            controller(): pulls user_classes from Main class
            
        Side effects:
            creates buttons and list boxes for welcome window frame
        """
        
        tk.Frame.__init__(self, parent) 
        
        self.canvas = tk.Canvas(self, height = 700, width = 800)
        self.canvas.pack()

        self.classlistvar = tk.StringVar()
        self.enrolledlistvar = tk.StringVar() 
               
        #   frame of the title label
        self.titleFrame = tk.Frame(self, bg = 'red', bd = 5)
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
        
        self.classlistvar.set(value = (301,311,314,326,335))
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
            controller(): pulls user_classes from Main class
            
        Side effects:
            Splits eclist into separate strings and appends to a list with correct name
        """
        
        alist = eclist.get().split() #splits the input from the enrolled listbox and creates a list of the values
        for element in alist:
            #calls remove_punctuation to strip the string of punctuation
            controller.user_classes.append(f"INST {remove_punctuation(element)}")


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
            controller(): pulls user_classes from Main class
            
        Side effects:
            creates buttons and list boxes for Departmentinfo frame
        """
        
        self.print_records = "" #will hold the text that is to be displayed on the page
        
        tk.Frame.__init__(self, parent)
        #   frame of the title label
        self.DItitleFrame = tk.Frame(self, bg = 'red', bd = 5)
        self.DItitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.08, anchor = 'n')

        #   title label
        self.DItitleLabel = tk.Label(self.DItitleFrame, text = "INST Department Information")   
        self.DItitleLabel.place(relwidth = 1, relheight = 1) 
        
        #   department info label
        self.query_label = tk.Label(self, text = "")
        self.query_label.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')
        
        #   this button takes user back to welcome window
        self.button1 = tk.Button(self, text="Back to Welcome Window",
                            command=lambda: [controller.show_frame(Welcomewindow), self.clear_list(controller)])
        self.button1.pack()

        #   takes user to the get schedule page
        self.button2 = tk.Button(self, text="Get Schedule",
                            command=lambda: controller.show_frame(Getschedule))
        self.button2.pack()
        
        #   executes command to display the department info for each class
        self.button3 = tk.Button(self, text="See Department Info",
                            command=lambda: self.call_classes(controller.user_classes))
        self.button3.pack()
        
        #   clears the text output on the page
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
        self.button3['state'] = 'normal' #resets the button status so the user can click on the "See Department Info" button again
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
        #holds info from main class in department_info.py for each class the user selected
        theschedule = department_info.main(i for i in classesfrombutton) 
        
        for items in theschedule:
            #iterating through each element and adding it to a string
            self.print_records += str(items) + "\n\n"
        
        #   displays the information for the department info
        self.query_label = tk.Label(self, text = self.print_records)
        self.query_label.place(x = 400, y = 700, relwidth = .4, relheight = .75, anchor = 's')
        self.button3['state'] = 'disabled' #disables button so the user can only click it once before clicking the "clear list" button
        
    
    def clear_list(self, controller):
        """
        Clears controller.user_classes.
        
        Args:
            controller(): pulls user_classes from Main class
            
        Side effects:
            Sets self.print_records to an empty string
        """
        controller.user_classes.clear() #clears the list of classes generated from clicking on the department info or get schedule button on the welcome window
        self.print_records = "" #resets value to an empty string

        
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
            controller(): pulls user_classes from Main class
            
        Side effects:
            creates buttons and list boxes for Getschedule frame
        """
        
        tk.Frame.__init__(self, parent)
        
        self.print_schedule = "" #holds the text of the class schedule
        
        #   frame of the title label
        self.GStitleFrame = tk.Frame(self, bg = 'red', bd = 5)
        self.GStitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        #   title label
        self.GStitleLabel = tk.Label(self.GStitleFrame, text = "Here is your INST schedule")   
        self.GStitleLabel.place(relwidth = 1, relheight = 1)   

        #   takes user back to welcome window and clears the user selected list
        self.button1 = tk.Button(self, text="Back to Welcome Window",
                            command=lambda: [controller.show_frame(Welcomewindow), self.clear_list(controller)])
        self.button1.pack()

        #   takes user to department info page
        self.button2 = tk.Button(self, text="Department Info",
                            command=lambda: controller.show_frame(Departmentinfo))
        self.button2.pack()
        
        #   executes command to get the schedule for the selected classes
        self.button3 = tk.Button(self, text = "Get Your Schedule",
                            command=lambda: self.get_schedule(controller.user_classes))
        self.button3.pack()
        
        #   clears the list of user selected classes
        self.delete_button = tk.Button(self, text = "Clear List",
                                       command=lambda: self.delete_list(controller.user_classes))
        self.delete_button.pack()
        
        
    def delete_list(self, controller):
        """
        Gets rid of text and label.
    
        Side effects:
            enables See Department Info button to clear to normal
        """
        
        self.textbox.destroy()
        self.button3['state'] = 'normal' #resets status of button so the user can click on the "Get Your Schedule" button again
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
        
        theschedule = schedule.main(i for i in thelist) #holds the information of each class as dataframes in a list
        
        for items in theschedule:
            #iterating through each dataframe
            self.print_schedule += "\n" + "Subject" + " " + "Assignment" + " " + "Time Due" + " " + "Due Date" + " " + "Weight" + " " + "days left" + " " + "difficulty" + "\n\n"
            
            for i,rows in items.iterrows():
                #iterating through each row
                self.print_schedule += (str(rows["Subject"]) + " " + str(rows["Assignment"]) + " " + str(rows["Time Due"]) + " " + str(rows["Due Date"])
                      + " " + str(rows["Weight"]) + " " + self.days_only(str(rows["days left"])) + " difficulty:" + str(rows["difficulty"])) + "\n"
        
        #   will display the schedule of the user selected classes
        self.textbox = tk.Text(self, height = 30, width = 50)
        self.textbox.place(x = 400, y = 700, relwidth = .8, relheight = .75, anchor = 's')
        self.textbox.insert('end', self.print_schedule)
        
        self.button3['state'] = 'disabled' #disables button so the user cannot click on it more than once before clearing the output
        
        
    def clear_list(self, controller):
        """
        Clears controller.user_classes.
        
        Args:
            controller(): pulls user_classes from Main class
            
        Side effects:
            Sets self.print_records to an empty string
        """
        
        controller.user_classes.clear()
        self.print_schedule = ""
        
    def days_only(self, datetime):
        """
        Retrieves the days left only from the line.
        
        Args:
            datetime(str): the days left and the hours for each assignment.
            
        Returns:
            days_left.group(1)(str): the days left for the assignment.
        """
        days_left = re.search(r"([-]?\w+\sdays)", datetime)
        if days_left:
            return (f"{days_left.group(1)} left")


if __name__=="__main__":
    app = Main()
    app.mainloop()