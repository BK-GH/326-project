"""
Unit Tests for Final Project
"""

import department_info
import schedule

def test():
    """ Demonstrate use of the DepartmentInfo class. """
    
    class_name = "INST 301"

    assert department_info.main([class_name]) == [("Class Name: " + class_name + "\nProfessor: " + "Joyce Garczynski" + 
                                                   "\nEmail: " + "jgarczyn@umd.edu" + "\nPhone Number: " + str(4107045168) + 
                                                   "\nOffice Hours: "+ "Always reachable via email")]
    
    assert schedule.main([class_name])

    
    
if __name__ == "__main__":
    test()
