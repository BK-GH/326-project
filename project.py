"""
Project: Assignment Tracker
Brook Goitom | Emmanuel Sitaniapessy | Jenny Dang | Nicholas Wang
INST 326
Professor Cruz
"""

import tkinter as tk

#Height and width of GUI window
HEIGHT = 700
WIDTH = 800

#Function to retrieve the class ID or IDs of the user
def get_classes(entry):
    print("The classes are:", entry)

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

### Frames

#frame of the first row
frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

label = tk.Label(frame, text = "Welcome to the INST python planner \n Enter your Class IDs below")        #Title Label
label.place(relwidth = 1, relheight = 1)                                    #

#frame on the second row
second_frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
second_frame.place(relx = 0.5, rely = 0.21, relwidth = 0.75, relheight = 0.1, anchor = 'n')

#frame on the third row
third_frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
third_frame.place(relx = 0.5, rely = 0.32, relwidth = 0.75, relheight = 0.1, anchor = 'n')


### Entry windows

#Entry on the first row
#entry = tk.Entry(frame, font = 40)
#entry.place(relwidth = 0.65 ,relheight = 1)

#Entry on the second row
second_entry = tk.Entry(second_frame, font = 40)
second_entry.place(relwidth = 0.65 ,relheight = 1)

#Entry on the third row
third_entry = tk.Entry(third_frame, font = 40)
third_entry.place(relwidth = 0.65 ,relheight = 1)


### Buttons

#button on the first row
#button = tk.Button(frame, text = "Enter", font = 40, command = lambda: get_classes(entry.get()) )
#button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

#button on the second row
button = tk.Button(second_frame, text = "Enter", font = 40, command = lambda: get_classes(second_entry.get()) )
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

#button on the third row
button = tk.Button(third_frame, text = "Enter", font = 40, command = lambda: get_classes(third_entry.get()) )
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)





""" This is will load a background image from the root folder 
background_image = tk.PhotoImage(file = 'umdphoto2.png')
background_label = tk.Label(root, image = background_image)
background_label.place(reldwidth = 1, relheight = 1)
"""

"""This is the old lower frame
lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')


label = tk.Label(lower_frame)
label.place(relwidth = 1, relheight = 1)
#label.pack(side = 'left', fill = 'both')
"""

root.mainloop()



"""
class Assignment:
    
    def due_date():
        pass
    
    def name():
        pass
    
    def course_name():
        pass
    
    def weight():
        pass


class Status:
    
    def days_left():
        pass
    
    def reminder():
        pass
    
    def countdown():
        pass
    
    def organize_list():
        pass
    
    def estimate():
        pass


def main():
    pass


if __name__ =="__main__":
    pass
"""