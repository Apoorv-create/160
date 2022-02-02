from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("C:\\Users\\apoor\\Downloads\\160\\C-160\\open.png"))
exit_img = ImageTk.PhotoImage(Image.open("C:\\Users\\apoor\\Downloads\\160\\C-160\\exit.jpg"))
save_img = ImageTk.PhotoImage(Image.open("C:\\Users\\apoor\\Downloads\\160\\C-160\\save.png"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx = 0.28, rely = 0.3, anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.3, anchor=CENTER)

mytext = Text(root, height = 35, width = 80)
mytext.place(relx = 0.8, rely = 0.55, anchor=CENTER)

open_button = Button(root, image = open_img, text = "OpenFile", command = openFile)
open_button.place(relx = 0.05, rely = 0.03, anchor=CENTER)

root.mainloop()