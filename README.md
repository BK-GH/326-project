# 326-project
This repository is for our INST 326 Final Project.

# What is our project:
  Our project is an assignment tracker created for students in order to keep track of upcoming assignments and due dates. The purpose of this project is to allow students to better time manage their coursework since courses are all online. It is harder to keep track of assignments and due dates since there is no face to face interactions with students and professors.

# How to run the program:
  Navigate to the directory on where the python files and csv files are located at. Make sure all the files are in the same directory. Once you are in Visual Studio or the command prompt, navigate to where the directory is located. When you have navigated to the correct directory, type in python3 guioriginal.py to run the program.

# Documentation & Understanding the output:
  Our program relies heavily on our gui file. The gui file is runned as explained above and python brings the user to our homepage (Welcome Window). Once the user has arrived at the Welcome Window, the user can use our two listboxes to add in the classes that he/she is enrolled in. Once the user has added in the classes, he/she can then choose to either see the department info or to see the schedule for the selected classes 
  If the user chooses to click on department info, the user can then choose to select more options. This time the user can select to go back to the Welcome Screen, go to the schedule screen, get the department info, or clear department info. If the user chooses to click on get the department info, the user will see the department info of the selected classes pop up. The user will then have to click on the clear department info, if the user does not he/she won’t be able to get another department info.
  If the user chooses to click on schedule, the user can then choose to select more options. This time the user can select to go back to the Welcome Screen, go to the department info screen, get the schedule, or clear schedule. If the user chooses to click on get the schedule, the user will see the schedule of the selected classes pop up. The user will then have to click on the clear schedule, if the user does not he/she won’t be able to get another schedule.



# Bibliography
References:
Bayden, I. (2017). How To Get Current Date Time with Now() Function In Python? Retrieved from https://www.poftut.com/get-current-date-time-or-now-in-python/#:~:text=How%20To%20Get%20Current%20Date%20Time%20or%20Now,5%20Print%20Specific%20Part%20Of%20Current%20Time.%20

	  For our project, we need to get the current day in order to calculate days left. To do this we needed a function that could just get the current day without messing up our code. We found just that in the article above. This article tells us about the datetime module and the function that gets the current date. The datetime module is specifically used to manipulate dates and time and is what we need. In the module, there is a function called datetime.now() that calculates the current day and time. We can use that to calculate the days left.

Codemy. (2020). Remove Labels - Python Tkinter GUI Tutorial #41. https://www.youtube.com/watch?v=2_qUokpB1fw&t=328s

    The video shows the processes and methods used to remove text from a label in python. In the context of our program, we used the destroy methods to get rid of the text after clicking a button to display either the “get your schedule” or the “see department info” button. We also used similar code to modify the “state” of our buttons so that the user cannot press on the “get your schedule” or “see department info” button again until after clearing the list. 

Codemy. (2020). Building Out The GUI for our Database App - Python Tkinter GUI Tutorial #20. https://www.youtube.com/watch?v=AK1J8xF4fuk&list=FLjR63CqforL7oFxUoUw_-3g&index=1&t=1358s

	  This video shows how to print out custom text on a label in tkinter. We wanted to use similar functionality in our program as we wanted to show the output of a function’s processes on the pages of our GUI. We used the for loop that is at the 21 minute mark to save our output into a variable and print that output in the label that we created.

Krunal. (2020). How To Convert Datetime To String In Python. Retrieved from
https://appdividend.com/2020/01/21/how-to-convert-datetime-to-string-in-python/

	  For our project, we needed to subtract two dates to calculate days left for schedule.py. When we tried to subtract the date for today and the dates under due date, we encountered a problem. The current days was not formatted the way we wanted it to be, so the output of days left ended up having a lot of stuff other than how many days left. To solve this problem we needed to find a way that could change the datetime format for the current day. We found just that in the article above. In that article, it tells us to use the strfttime function of the datetime module. Knowing this, we converted the datetime object of the current day the user was on to Year-Month-Day instead of Year-Month-Day-Hour-Minute-Second. This changed the outputs of the days due column to what we wanted it to be.  
