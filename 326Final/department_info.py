"""
Final Project
Group 2: Assigment Tracker
B**** ****** | Emmanuel Sitaniapessy | Jenny Dang | Nicholas Wang
INST 326
Professor Cruz
"""

import pandas as pd

class DepartmentInfo:
    """This class will act as department information and will be displayed
    
    Attributes:
        df(Dataframe): dataframe where all the information is stored
        class_name(str): name of the class
        index(int): index to navigate rows
    """
    def __init__(self, class_name):
        #Create a path
        path = r"classinfo.csv"
        #Set the dataframe to the csv with the path
        self.df = pd.read_csv(path)
        #Set class name attribute to the parameter
        self.class_name = class_name
        #Create a counter to loop through each row
        count = 0
        #Loop through to look for index for the specified class
        while count < len(self.df):
            #If the class name matches with any class names in the dataframe
            if self.class_name == self.df["Class Name"][count]:
                #Set the index attribute to that counter
                self.index = count
            #Increment count
            count += 1
    
    def get_professor(self):
        """Gets the professor of that class
        
        Args:
            self: reference to the object
        
        Returns:
            professor(str): professor of that class
        """
        #Search for the professor of that index
        professor = self.df["Professor"][self.index]
        #Return the professor
        return professor
        
    def get_email(self):
        """Gets the professor's email of that class
        
        Args:
            self: reference to the object
        
        Returns:
            email(str): professor's email of that class
        """
        #Search for the email of that index
        email = self.df["Email"][self.index]
        #Return the email
        return email
        
    def get_phone_number(self):
        """Gets the professor's phone number of that class
        
        Args:
            self: reference to the object
        
        Returns:
            phone_number(str): professor's phone number of that class
        """
        #Search for the phone number of that index
        phone_number = self.df["Phone Number"][self.index]
        #Return the phone number
        return phone_number
        
    def get_office_hours(self):
        """Gets the professor's office hours of that class
        
        Args:
            self: reference to the object
        
        Returns:
            office_hours(str): professor's office hours of that class
        """
        #Search for the office hours of that index
        office_hours = self.df["Office Hours"][self.index] 
        #Return the office hours   
        return office_hours
        
    def get_department_info(self):
        """Gets the entire information of that class (from the syllabus)
        
        Args:
            self: reference to the object
        
        Returns:
            department_info(str): entire information of that class
        """
        #Create a string that has all the information for that class
        department_info = ("Class Name: " + self.class_name + "\nProfessor: " + self.get_professor() 
        + "\nEmail: " +  self.get_email() + "\nPhone Number: " + str(self.get_phone_number()) 
        + "\nOffice Hours: "+ self.get_office_hours())

        #Return the information
        return department_info
    
    
def main(class_list):
    """Prints out of the information for the selected classes
    
    Args:
        class_list(list): list of selected classes
    """
    
    #Loop through each class of the selected classes
    alist = []
    for class_name in class_list:
        #Create a instance of DepartmentInfo with the class
        department_object = DepartmentInfo(class_name)
        #Call the get_department_info function and store it in a variable
        department_info = department_object.get_department_info()
        #Print out department info
        #print(department_info + "\n")
        alist.append(department_info)
    
    return alist

if __name__ =="__main__":
    class_list = ["INST 301", "INST 311", "INST 314", "INST 326", "INST 335"]
    main(class_list)
