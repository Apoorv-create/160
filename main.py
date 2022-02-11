from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open(r"C:\C-160\open.png"))
exit_img = ImageTk.PhotoImage(Image.open(r"C:\C-160\exit.jpg"))
save_img = ImageTk.PhotoImage(Image.open(r"C:\C-160\save.png"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx = 0.28, rely = 0.3, anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.3, anchor=CENTER)

mytext = Text(root, height = 35, width = 80)
mytext.place(relx = 0.8, rely = 0.55, anchor=CENTER)

name = ""

def OpenFile():
    global name
    mytext.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title ="Open Text File", filetypes=(("Text File", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split(".")[0]
    input_file_name.insert(END, formated_name)
    root.title(formated_name)
    text_file = open(name, "r")
    para = text_file.read()
    my_text.insert(END, para)
    text_file.close()
    

def save():
    input_name = input_file_name.get()
    file = open(input_name + ".txt", "w")
    data = mytext.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    mytext.delete(1.0, END)
    messagebox.showinfo("Update", "Success")

def closewindow():
    root.destroy()
    
open_button = Button(root, image = open_img, text = "openFile", command = OpenFile)
open_button.place(relx = 0.05, rely = 0.03, anchor=CENTER)

save_button = Button(root, image = save_img, text = "saveFile", command = save)
save_button.place(relx = 0.11, rely = 0.03, anchor=CENTER)

exit_button = Button(root, image = exist_button, text = "closeFile", command = closeWindow)
exit_button.place(relx = 0.17, rely = 0.03, anchor=CENTER)




root.mainloop()