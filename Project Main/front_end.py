# initial commit
#Added code to create the window - Tawanda
from tkinter import *

#key down function connected to text boxs and submit button -Maddy
# Don't forget to enter the dates that code was submitted in the comments @maddy
# Great work so far in writting the implementation of the window and the label fields.
# Look up how the 'grid' works in order for the window to have a nicer aesthetic
# Hugo 11_13_2019

def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = compdictionary[entered_text]
    except:
        definition = "Sorry,Not Found"
    output.insert(END, definition)



#created window variable
Window = Tk()

#Set window title
Window.title("Please work")

#Set window dimensions
Window.maxsize(1000, 1000)

#Label -Maddy
Label (Window, text="Enter Info", fg='black', bg='white') .grid(row=1, column=0, sticky=E)

#text entry box -Maddy
textentry = Entry(Window, width=20, bg='white')
textentry.grid( row=2, column=0, sticky=W)

#submit button -Maddy
Button(Window, text="Submit", width=6, command=click) .grid(row= 3, column=0, sticky=W)

#another label-Maddy
Label (Window, text="\nInfo", fg='black', bg='white') .grid(row=4, column=0, sticky=W)

#text box -Maddy
output = Text(Window, width=75, height=6, wrap=WORD, bg='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

#dictionary(if we were searching a word) -Maddy
compdictionary = {
    'algoritm': 'text', 'refrence in submit box': 'text text text'
}

#exit label -Maddy
Label (Window, text="Click to Exit", fg='black', bg='white') .grid(row=6, column=0, sticky=E)

#exit function-maddy
def close_window():
    Window.destroy()
    exit()
# close window function is great, make sure to implement it though. Hugo  11_13_2019
# -edit window function is already implementedin command. Great Job!!-Hugo 11_13_2019
#exit button -Maddy
Button(Window, text="Exit", width=6, command=close_window) .grid(row= 7, column=0, sticky=W)



#Start the program
Window.mainloop()

# End code here  11/8/2019 - Tawanda
#hello