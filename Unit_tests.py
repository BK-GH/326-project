"""
Unit Tests for Final Project
"""

from department_info import DepartmentInfo
from schedule import Status, main

def test():
    """ Demonstrate use of the DepartmentInfo class. """
    
    class_name = "INST 301"
    dep = DepartmentInfo(class_name)
    
    assert dep.get_professor() == "Joyce Garczynski"
    assert dep.get_email() == "jgarczyn@umd.edu"
    assert dep.get_phone_number() == 4107045168
    assert dep.get_office_hours() == "Always reachable via email"
    assert dep.get_department_info() == ("Class Name: " + class_name + "\nProfessor: " + "Joyce Garczynski" 
        + "\nEmail: " + "jgarczyn@umd.edu" + "\nPhone Number: " + str(4107045168) 
        + "\nOffice Hours: "+ "Always reachable via email")
    
    class_schedule = Status(class_name)
    class_schedule.days_left()
    class_schedule.importance()
    df_condense = class_schedule.df[["Subject", "Assignment", "Time Due", "Due Date", "Weight", "days left", "difficulty"]]
    assert main([class_name]) == [df_condense]

    
    
if __name__ == "__main__":
    test()
