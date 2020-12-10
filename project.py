"""
Project: Assignment Tracker
Brook Goitom | Emmanuel Sitaniapessy | Jenny Dang | Nicholas Wang
INST 326
Professor Cruz
"""

#import modules
import pandas as pd
from datetime import datetime


class Assignment:
    """
    A class for reading through assignments
    """
    
    def __init__(self):
        """
        Initializes the Assignment attributes.
        """
        # Path
        path = r"assignmentdatabase.csv"
                
        # read the CSV file from path
        self.df = pd.read_csv(path)
        
        self.assignment = []
        
    '''
    def get_course_name(self):
        """
        Gets the name of the course.
        """
        course_name = self.assignment["Subject"]
        return course_name
        
    
    def get_assignment_name(self):
        """
        Gets the name of the assignment.
        """
        assignment_name = self.assignment["Assignment"]
        return assignment_name
    
    
    def get_time_due(self):
        """ 
        Gets time that the assignment is due
        """
        due_date = self.assignment["Due Date"]
        return due_date
    
    
    def get_due_date(self):
        """ 
        Gets time that the assignment is due
        """
        time_due = self.assignment["Time Due"]
        return time_due
    
    def get_weight(self):
        """ 
        Gets the weight of assignment
        """
        weight = self.assignment["Weight"]
        return weight
    
    def get_assignment_type(self):
        """ 
        Gets assignment type
        """
        assignment_type = self.assignment["Type"]
        return assignment_type
        '''
        
        
class Status():
    
    def __init__(self):
        """
        Initializes the attributes of the status class.
        """
        # Path
        path = r"assignmentdatabase.csv"
                
        # read the CSV file from path
        self.df = pd.read_csv(path)
    
    def days_left(self):
        """
        Calculates the days left to complete the assignment.
        """
        
        today = pd.to_datetime("now")
        self.df["Due Date"] = pd.to_datatime(self.df["Due Date"])
    
        
        #date_format = today.strftime("%m/%d/%y %H:%M:%S")
        
        print(today)
        
        #print(f"today is {date_format}")
        
        print(self.df["Due Date"])
        
        #calculate days left 
        self.df["days left"] = today - self.df["Due Date"]
    

    
    def importance(self):
        """
        Estimates the time needed for the assignment using the weight
        
        Returns:
            estimate(int): estimate of how much time needed
        """
       
        #df_cond = self.df[["Weight", "Type"]]
        
        count = 0
        while count < len(self.df["Type"]):
            if self.df["Type"] == "Discussion":
                self.type_weight =  1
            elif self.df["Type"] == "Homework":
                self.type_weight = 2
            elif self.df["Type"] == "Written":
                self.type_weight = 3
            elif self.df["Type"] == "Project":
                self.type_weight = 4
            elif self.df["Type"] == "Exam":
                self.df["type_weight"] = 5
            else:
                self.df["type_weight"] = 6
        
        self.df["difficulty"] = self.df["Weight"] * self.df["type_weight"]
        
        difficulty = self.df["difficulty"] #df.loc[days_left() >= 0, ["difficulty"]]
        
        print(f"Level of difficulty: {difficulty}")


def main():
    """
    Retrieves and prints the status the assignment.
    """
    
    print("Upcoming Assignments:")
    
    status_object = Status()
        
    if status_object.days_left() >= 0:
        print (status_object.df["Due Date" < datetime.now()])
            
    #create instance of status and print to print out days remaining and estimate
    

if __name__ =="__main__":
    class_list = ["INST 301", "INST 311", "INST 314", "INST 326", "INST 335"]
    main()