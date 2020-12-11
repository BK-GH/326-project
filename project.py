"""
Project: Assignment Tracker
Brook Goitom | Emmanuel Sitaniapessy | Jenny Dang | Nicholas Wang
INST 326
Professor Cruz
"""

#import modules
import pandas as pd
from datetime import datetime

'''
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
        #self.df = pd.DataFrame(columns=["Due Date"])
        #today = pd.to_datetime("now")
        today = datetime.now()
        
        today = today.strftime("%Y-%m-%d")
        #self.df["Due Date"] = pd.to_datatime(self.df["Due Date"])
        
        date_format = datetime.strptime(today, "%Y-%m-%d")
    
        #print(today)
        #print(type(date_format))
        
        #print(f"today is {date_format}")
        
        print(self.df["Due Date"])
        
        datelist = []
        
        for item in self.df["Due Date"]:
            date = datetime.strptime(item, "%Y-%m-%d")
            datelist.append(date)
            #self.df["new date"] = self.df["Due Date"]

        self.df["new date"] = datelist
        #date = datetime.parse(self.df["Due Date"]);
        
        #calculate days left 
        self.df["days left"] = self.df["new date"] - date_format
        
        
    
        print(self.df["days left"])
        
    
    def importance(self):
        """
        Estimates the time needed for the assignment using the weight
        
        Returns:
            estimate(int): estimate of how much time needed
        """
       
        #df_cond = self.df[["Weight", "Type"]]
        
        typeweightlist = []
        
        count = 0
        while count < (len(self.df["Type"])):
            if self.df["Type"][count] == "Discussion":
                typeweight =  1
            elif self.df["Type"][count] == "Homework":
                typeweight = 2
            elif self.df["Type"][count] == "Written":
                typeweight = 3
            elif self.df["Type"][count] == "Project":
                typeweight = 4
            elif self.df["Type"][count] == "Exam":
                typeweight = 5
            else:
                typeweight = 6
            typeweightlist.append(typeweight)
            count+= 1
        
        self.df["type_weight"] = typeweightlist
        
        difficultylist = []
        
        count2 = 0
        while count2 < (len(self.df["type_weight"]-1)):
            difficulty = self.df["Weight"][count2] * self.df["type_weight"][count2]
            difficultylist.append(round(difficulty))
            count2+= 1
        self.df["difficulty"] = difficultylist
        
        difficulty = self.df["difficulty"] #df.loc[days_left() >= 0, ["difficulty"]]
        
        #for difficulty in self.df["difficulty"]:
            #print(f"Level of difficulty: {difficulty}")


def main():
    """
    Retrieves and prints the status the assignment.
    """
    
    print("Upcoming Assignments:")
    
    status_object = Status()
        
    status_object.days_left()
    
    status_object.importance()
    #    print (status_object.df["Due Date" < datetime.now()])
            
    #create instance of status and print to print out days remaining and estimate
    
    df_cond = status_object.df[["Subject", "Assignment", "Time Due", "Due Date", "Weight", "days left", "difficulty"]]
    print(df_cond)
    return df_cond
    

if __name__ =="__main__":
    class_list = ["INST 301", "INST 311", "INST 314", "INST 326", "INST 335"]
    main()