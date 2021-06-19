"""
Final Project
Group 2: Assigment Tracker
B**** ****** | Emmanuel Sitaniapessy | Jenny Dang | Nicholas Wang
INST 326
Professor Cruz
"""

#import modules
import pandas as pd
from datetime import datetime
        
class Status():
    """
    A class to calculate the status of each assignment
    
    Attributes:
        df(Dataframe): dataframe that will be used throughout the script
    """
    
    def __init__(self, class_name):
        """Initializes the attributes of the status class.
        
        Args:
            self: reference to the object
            class_name(str): name of the class
        
        Side Effects:
            Subsets the dataframe based on the subject,
            Reindexes the index
            Remove the blank columns with NAs
        """
        # Path
        path = r"assignmentdatabase.csv"
                
        # read the CSV file from path
        self.df = pd.read_csv(path)
        self.df = self.df[self.df["Subject"] == class_name].reset_index().dropna(how='all', axis='columns')
    
    def days_left(self):
        """Calculates the days left to complete the assignment.
        
        Arg:
            self: reference to the object
        
        Side Effects:
            Converts the datetime object to a formatted string and then turns it back
            Appends dates to datelist
            Creates a new column to store dates
            Create a new column to store days left
        """
        #Creates a datetime object for the current day
        today = datetime.now()
        #Converts the datetime object to a formatted string
        today = today.strftime("%Y-%m-%d")
        #Convert the string back to a datetime object
        date_format = datetime.strptime(today, "%Y-%m-%d")

        #Creates a list to store the dates for calculation
        datelist = []
        
        #Loop through to modify each date and store the dates
        for item in self.df["Due Date"]:
            #Modify each date
            date = datetime.strptime(item, "%Y-%m-%d")
            #Store the date into the date list
            datelist.append(date)
            
        #Set a column to the list
        self.df["new date"] = datelist
        
        #calculate days left by subtracting each date by today 
        self.df["days left"] = self.df["new date"] - date_format
    
    def importance(self):
        """
        Estimates the time needed for the assignment using the weight
        
        Args:
            self: reference to the object
        
        Side Effects:
            Append to the type weight list
            Create a new column called type weight
            Append to the difficulty list
            Create a new column called difficulty
        """
        
        #Creates a list to store the type weight
        typeweightlist = []
        
        #Create a variable to loop through each type
        count = 0
        #Loop through the Type column of the dataframe
        while count < (len(self.df["Type"])):
            #If the row is discussion
            if self.df["Type"][count] == "Discussion":
                #type weight is equal to 1
                typeweight =  1
            #If the row is homework
            elif self.df["Type"][count] == "Homework":
                #type weight is equal to 2
                typeweight = 2
            #If the row is written
            elif self.df["Type"][count] == "Written":
                #type weight is equal to 3
                typeweight = 3
            #If the row is project
            elif self.df["Type"][count] == "Project":
                #type weight is equal to 4
                typeweight = 4
            #If the row is exam
            elif self.df["Type"][count] == "Exam":
                #type weight is equal to 5
                typeweight = 5
            #Otherwise
            else:
                #type weight is equal to 6
                typeweight = 6
            #Append the type weight into the list
            typeweightlist.append(typeweight)
            #Increment the count
            count+= 1
        
        #Create a new column based on the list, called type weight
        self.df["type_weight"] = typeweightlist
        
        #Create a list for the difficulty
        difficultylist = []
        
        #Create a variable to loop through each type weight
        count2 = 0
        #While count2 is less than the length of type weight
        while count2 < (len(self.df["type_weight"]-1)):
            #Calculate difficulty by multiplying the weight by type weight
            difficulty = self.df["Weight"][count2] * self.df["type_weight"][count2]
            #Round the difficulty and append it to the list
            difficultylist.append(round(difficulty))
            #Increment count
            count2 += 1
        #Create a new column called difficulty, based on the difficulty list
        self.df["difficulty"] = difficultylist

       
def main(class_list):
    """Retrieves and prints the status the assignment.
    
    Args:
        class_list(list): list of classes
    
    Returns:
        df_cond(df): list of columns to show
        
    Side Effects:
        Subset data from the old dataframe
        Appends to the dataframe list
    """
    
    #Creates a list to store the dataframes for each class
    class_dataframe = []
    
    #Loop through the class list
    for class_name in class_list:
        #Create a status object for the class
        status_object = Status(class_name)
        #Call the days left function
        status_object.days_left()
        #Call the importance function
        status_object.importance()
        #create a new dataframe with only the object's subject, assignment, time due, due date, weight, days left, and difficulty
        df_cond = status_object.df[["Subject", "Assignment", "Time Due", "Due Date", "Weight", "days left", "difficulty"]]
        #Append the new dataframe to the list
        class_dataframe.append(df_cond)
    
    #Return that list
    return class_dataframe
    

if __name__ =="__main__":
    class_list = ["INST 301", "INST 311", "INST 314", "INST 326", "INST 335"]
    
    main(class_list)
