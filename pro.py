"""
Project 326
"""

import tkinter as tk


HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# Item selectable List box
classes = ["335", "326", "314", "311", "301"]
def get_classes():
    num = int(classlist.curselection())
    enrolledlist.insert(tk.END, classes[num])
    
def delete_classes():
    classlist

#The box behind the title label(label below) that creates a frame around the title label, it just looks nice
frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

#Title label, basically welcomes users to the application
label = tk.Label(frame, text = "Welcome to the INST python planner \n Highlight your Class IDs below and press 'add'")   
label.place(relwidth = 1, relheight = 1)  



classlist = tk.Listbox(root, height=5, selectmode = 'single')
for ID in classes:
    classlist.insert(0,ID) # instead of 0 you can do "end", but it flips the list
classlist.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')

#enrolledlist = tk.Frame(root, bg = '#80c1ff', bd = 5)
enrolledlist = tk.Listbox(root, height=5, selectmode='single')

#enrolledlist.place(x = 500, y = 350, relwidth = .24, relheight = .30, anchor = 'w')




addButton = tk.Button(root, text = "add", command = get_classes)
addButton.place(x = 400, y = 250, relwidth = 0.05, relheight = 0.05)

deleteButton = tk.Button(root, text = "delete", command = delete_classes)
deleteButton.place(x = 400, y = 300, relwidth = 0.05, relheight = 0.05)

enrolledlist.place(x = 500, y = 350, relwidth = .24, relheight = .30, anchor = 'w')

root.mainloop()


""" Old list box, I didnt like how this one didnt highlight things
mylistbox = tk.Listbox(root)
mylistbox.place(x = 300, y = 350, relwidth = .24, relheight = .30, anchor = 'e')
mylistbox.insert(0, "301")
mylistbox.insert(1, "311")
mylistbox.insert(2, "314")
mylistbox.insert(3, "326")
mylistbox.insert(4, "335")
"""

""" Didnt like this Listbox
lb1 = tk.Listbox(root)
lb1.insert(1, "326")
lb1.pack
"""