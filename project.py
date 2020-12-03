"""
Project: Assignment Tracker
Brook Goitom | Emmanuel Sitaniapessy | Jenny Dang | Nicholas Wang
INST 326
Professor Cruz
"""

#import modules
import pandas as pd

# Takes the file's folder 
path = r"assignmentdatabase.csv"
   
# read the CSV file 
df = pd.read_csv(path) 
   
# print the first five rows 
print(df)

def course_name(line):
    """
    Finds out the name of the course of the assignment.
    
    Args:
        line(str): line from the file.
        
    Return:
        name(str): Returns name of the course for the assignment.
    """

def assignment_name(line):
    """
    Gets the name of the assignment.
    
    Args:
        line(str): line from the file
        
    Return:
        assignment_name(str): Name of the assignment.
    """

class Assignment:
    
    def __init__(self, path):
        """
        Initializes the Assignment attributes.
        
        Args:
            path(str): Path to the csv file.
            
        Return:
            None
        """
    
    def due_date():
        pass
    
    def weight(self):
        """ Initializes the weight of assignment
        
        Args:
            self: reference to the object
            
        """
        pass


class Status:
    
    def __init__(self):
        """
        Initializes the attributes of the status class.
        """
    
    def days_left():
        """
        Calculates the days left to complete the assignment.
        """
        pass
    
    def organize_list():
        pass
    
    def estimate():
        """Estimates the time needed for the assignment using the weight
        
        Returns:
            estimate(int): estimate of how much time needed
        
        """
        pass


def main():
    """
    Retrieves and prints the status the assignment.
    """
    pass


if __name__ =="__main__":
    pass
