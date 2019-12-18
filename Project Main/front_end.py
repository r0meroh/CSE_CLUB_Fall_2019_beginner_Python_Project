# initial commit
#Added code to create the window - Tawanda
from tkinter import *
import back_end


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


#function to display list -Maddy 12/17/19
def display_list():
    Items_in_lists.delete(0,END)
    for i in back_end.print_me():
        Items_in_lists.insert(END, i)


def add_item():
    back_end.insert(Brand_entry.get(),Model_entry.get(),Price_entry.get())
    Items_in_lists.delete(0,END)
    Items_in_lists.insert(END,(Brand_entry.get(),Model_entry.get(),Price_entry.get()))

def delete_item():
    back_end.remove_shoe(Model_entry.get())

def search_item():
    Items_in_lists.delete(0,END)
    for i in back_end.search_shoe(Brand_entry.get(),Model_entry.get(),Price_entry.get()):
        Items_in_lists.insert(END, i)


#created window variable
Window = Tk()

#Set window title
Window.title("Shoe Base")

#Set window dimensions
#Window.maxsize(1000, 1000)

#Label -Maddy
#Label (Window, text=" Shoe Base ", fg='black', bg='white') .grid(row=1, column=0)

#Shoe Brand Label -Maddy 12/17/19
Label_1 = Label(Window, text=" Brand ", fg='black')
Label_1.grid(row=1, column=1)

#Text Entry box for Brand - Maddy 12/17/19
Brand_entry = Entry(Window, width=10, bg='white')
Brand_entry.grid( row=1, column=3)

#add button -Maddy 12/17/19
Add_button = Button(Window, text="Add", width=6, command=add_item)
Add_button.grid(row=1 , column=5)

#Shoe Model Label -Maddy 12/17/19
Label_2 = Label(Window, text=" Model ", fg='black')
Label_2.grid(row=5, column=1)

#Text Entry box for Model -Maddy 12/17/19
Model_entry = Entry(Window, width=10, bg='white')
Model_entry.grid( row=5, column=3)

#Delete button -Maddy 12/17/19
Delete_button = Button(Window, text="Delete", width=6, command=delete_item)
Delete_button.grid(row=5 , column=5)

#Shoe Price Label -Maddy 12/17/19
Label_3 = Label(Window, text=" Price ", fg='black')
Label_3.grid(row=10, column=1)

#Text Entry box for Price -Maddy 12/17/19
Price_entry = Entry(Window, width=10, bg='white')
Price_entry.grid( row=10, column=3)

#Search Button - Maddy 12/17/19
Search_button = Button(Window, text="Search", width=6, command=search_item)
Search_button.grid(row=10 , column=5)


#List -Maddy 12/17/19
Items_in_lists = Listbox(Window, height=5, width=40)
Items_in_lists.grid(row=15, column=1, rowspan=5, columnspan=5)

#Display Button - Maddy 12/17/19
Display_button = Button(Window, text="Display", width=6, command=display_list)
Display_button.grid(row=15 , column=6)

#dictionary(if we were searching a word) -Maddy
#compdictionary = {
    #'algoritm': 'text', 'refrence in submit box': 'text text text'
#}


#exit function-maddy
def close_window():
    Window.destroy()
    exit()

#exit button -Maddy
Exit_button = Button(Window, text="Exit", width=6, command=close_window)
Exit_button.grid(row= 21, column=5)



#Start the program
Window.mainloop()

# End code here  11/8/2019 - Tawanda
