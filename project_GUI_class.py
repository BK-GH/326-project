try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog



class Welcomewindow(tk.Tk):
    """
    A class for opening main window 

    Attributes:
        tk.Tk(): passes in the root of Tkinter
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes Welcomewindow class.
        
        Args:
            args(): passes varible to function
            kwargs(): keyword arguments that passes varible to function
        """
        tk.Tk.__init__(self, *args, **kwargs)
        #   canvas
        self.canvas = tk.Canvas(self, height = 700, width = 800)
        self.canvas.pack()        
        #   list variables
        self.classlistvar = tk.StringVar()
        self.enrolledlistvar = tk.StringVar()        
        #   frame of the title label
        self.titleFrame = tk.Frame(self, bg = '#80c1ff', bd = 5)
        self.titleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        #   title label
        self.titleLabel = tk.Label(self.titleFrame, text = "Welcome to the INST python planner \n Highlight your Class IDs below and press 'add'")   
        self.titleLabel.place(relwidth = 1, relheight = 1)   
        #   frame of the class box
        """
        """        
        #   list of available classes
        self.classlist = tk.Listbox(self, height=5, listvariable = self.classlistvar, selectmode = 'multiple')
        self.classlist.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')    
        #   frame of the enrolled box
        """
        """
        #   user selected classes
        self.enrolledlist = tk.Listbox(self, height=5, listvariable = self.enrolledlistvar, selectmode = 'multiple')
        self.enrolledlist.place(x = 500, y = 350, relwidth = .24, relheight = .30, anchor = 'w')
        #   frame of addbutton
        """
        """
        #   addbutton: send one class from classlist to enrolledlist
        self.addButton = tk.Button(self, text = "add", command = lambda: self.get_classes(True))
        self.addButton.place(x = 370, y = 250, relwidth = 0.08, relheight = 0.05)        
        #   addbutton: sends all classes from classlist to enrolledlist
        self.addallButton = tk.Button(self, text = "add+", command = lambda: self.get_classes)
        self.addallButton.place(x = 370, y = 300, relwidth = 0.08, relheight = 0.05)        
        #   frame of deletebutton
        """
        """
        #   deletebutton: send one class from enrolledlist to classlist
        self.deleteButton = tk.Button(self, text = "delete", command = lambda:  self.delete_classes(True))
        self.deleteButton.place(x = 370, y = 350, relwidth = 0.08, relheight = 0.05)
        #   deletebutton: sends all classes from enrolledlist to classlist
        self.deleteallButton = tk.Button(self, text = "delete-", command = lambda:  self.delete_classes)
        self.deleteallButton.place(x = 370, y = 400, relwidth = 0.08, relheight = 0.05)
        #   departmentinfo button: sends the user to the department info page
        self.DIbutton = tk.Button(self, text = "Department Info", command = lambda:  Departmentinfo.open_department_info(self))
        self.DIbutton.place(x = 320, y = 500, relwidth = 0.2, relheight = 0.05)
        #   getschedule: sends the user to the schedule page
        #self.DIbutton = tk.Button(self, text = "Get Schedule", command = self.open_get_schedule)
        #self.DIbutton.place(x = 320, y = 550, relwidth = 0.2, relheight = 0.05)
        #   inserts default values from classes function into the classlistbox
        self.classes()


    def classes(self):
        """
        A method to set class values to list

        Args:
            classlistvar(list): list of classes
            enrolledlistvar(list): empty list to pass in list of classes
        """
        self.classlistvar.set(value = (301,311,314,326,335)) #    you can also use value = ['A', 'B', 'C']
        self.enrolledlistvar.set(value = ())
    

    def get_classes(self, only_one_item=False):
        """ 
        A method that gets a class from the enrolled list.
        
        Args:
            only_one_item(bool): set to false, can only select one item

        Side effects:
            Alters enrolled list variable
            
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
        right_value_list = [i for i in right_value_list if i.isnumeric()]

        # merge w/o duplicates
        result_list = sorted(list(set(right_value_list + left_selected_list)))
        self.enrolledlistvar.set(value=result_list)


    def delete_classes(self, only_one_item=False):
        """ 
        A method that deletes a class from the enrolled list.
        
        Args:
            only_one_item(bool): set to false, can only select one item

        Side effects:
            Alters enrolled list variable
            
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
        right_value_list = [i for i in right_value_list if i.isnumeric()]
        # values from left side
        left_value_list = [line.strip(' \'') for line in self.classlistvar.get()[1:-1].split(',')]
        # merge w/o duplicates
        result_list = sorted(list(set(right_value_list) - set(right_selected_list)))
        self.enrolledlistvar.set(value=result_list)


    """def open_department_info(self):
        departmentinfo = tk.Toplevel(self, height = 700, width = 800)        
        #   frame of the title label
        DItitleFrame = tk.Frame(departmentinfo, bg = '#80c1ff', bd = 5)
        DItitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        #   title label
        DItitleLabel = tk.Label(DItitleFrame, text = "INST Department Information")   
        DItitleLabel.place(relwidth = 1, relheight = 1) 
        #   Testing
        DItestFrame = tk.Frame(departmentinfo, bg = '#80c1ff')
        DItestFrame.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')
    
    
        my_tree = ttk.Treeview()        
        my_menu = Menu(root)
        root.config(menu = my_menu)
        file_menu = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label = "Spreadsheet", menu = file_menu)
        file_menu.add_command(label = "Open", command = file_open)
        my_label = Label(root, text= " ")
        my_label.place(pady = 20)
        """
        
    """    Test Function
    def file_open():
        filename = filedialog.askopenfilename(
            initialdir = "C:/gui/",
            title = "Opend a file",
            filetype = (("xlsx files", "*.xlsx"), ("All Files ", "*.*"))
            
        )
        
        if filename:
            try:
                filename = r"{}".formate(filename)
                df = pd.read_excel(filename)
            except ValueError:
                my_label.config(text = "File couldnt be opened")
            except FileNotFoundError:
                my_label.config(text = "File couldnt be opened")
    """            
            

    def open_get_schedule(self):
        """ 
        A method to open the schedule from classes in enrolled list.
        
        Side effects:
            opens page with schedule
        """
        
        getschedule = tk.Toplevel(self, height = 700, width = 800)          
        #   frame of the title label
        GStitleFrame = tk.Frame(getschedule, bg = '#80c1ff', bd = 5)
        GStitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        #   title label
        GStitleLabel = tk.Label(GStitleFrame, text = "Here is your INST schedule")   
        GStitleLabel.place(relwidth = 1, relheight = 1)   

class Departmentinfo(Welcomewindow):
    """
    A class for opening the department info page 
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes Departmentinfo class.
        
        Args:
            args(): passes varible to function
            kwargs(): keyword arguments that passes varible to function
        """
        
        tk.Tk.__init__(self, *args, **kwargs)
        #self.departmentinfo = tk.Toplevel(self, height = 700, width = 800)
        #self.DItitleFrame = tk.Frame(self.departmentinfo, bg = '#80c1ff', bd = 5)
        #self.DItitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        #self.DItitleLabel = tk.Label(self.DItitleFrame, text = "INST Department Information")   
        #self.DItitleLabel.place(relwidth = 1, relheight = 1)
    
    def open_department_info(self):
        """
        A method open the department info page

        Side effects:
            opens department info page
        """
        
        self.departmentinfo = tk.Toplevel(self, height = 700, width = 800)
    
        #   frame of the title label
        self.DItitleFrame = tk.Frame(self.departmentinfo, bg = '#80c1ff', bd = 5)
        self.DItitleFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

        #   title label
        self.DItitleLabel = tk.Label(self.DItitleFrame, text = "INST Department Information")   
        self.DItitleLabel.place(relwidth = 1, relheight = 1) 
    
        #   Testing
        #DItestFrame = tk.Frame(departmentinfo, bg = '#80c1ff')
        #DItestFrame.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')
    
        #my_tree = ttk.Treeview()
    
        #my_menu = tk.Menu(tk.root)
        #root.config(menu = my_menu)
    
        #file_menu = tk.Menu(my_menu, tearoff = False)
        #my_menu.add_cascade(label = "Spreadsheet", menu = file_menu)
        #file_menu.add_command(label = "Open", command = file_open)
    
    """
    #   Test Function
    def file_open():
        my_label = tk.Label(root, text= " ")
        my_label.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')
        filename = filedialog.askopenfilename(
            initialdir = "C:/gui/",
            title = "Open a file",
            filetype = (("xlsx files", "*.xlsx"), ("All Files ", "*.*"))
         )
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_csv("classinfo.csv")
                return df.head()
            except ValueError:
                my_label.config(text = "File couldnt be opened")
            except FileNotFoundError:
                my_label.config(text = "File couldnt be opened")
        
        
"""


if __name__=="__main__":
    app = Welcomewindow()
    app.mainloop()