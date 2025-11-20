#Project 2 Part 2

# import the required modules
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd


# Window setup

root = Tk()
root.title('CCSU Mobile App')
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg='light blue')


# Make white in logo transparent and show it

img = Image.open('logo.PNG')

# Pillow>=10 changed ANTIALIAS; this keeps it compatible
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)

img = img.convert("RGBA")
data = img.getdata()
newData = []
for item in data:
    # if pixel is white make it transparent; else keep it
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image = logo, bg='light blue')
logoLabel.place(x=10, y=10)


# CSV file

data = pd.read_csv("midterm_exam.csv")

# Label used to display results
lb = Label(root, justify="left", bg="light blue", anchor="w", font=("Arial", 10))
lb.place(x=40, y=210)  # moved lower so text doesn’t overlap buttons


# Clear text before updating

def clear_label():
    lb.config(text="")


# Button 1: Calendar

def calendar():
    clear_label()
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))


# Button 2: Buildings

def building():
    clear_label()
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))


# Button 3: Faculty

def faculty():
    clear_label()
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))


# Button 4: School of Business

def business():
    clear_label()
    courses = [
        "Accounting",
        "Finance",
        "Management & Organization",
        "Marketing",
        "Management Information Systems (MIS)",
        "Business Analytics"
    ]
    lb.config(text="\n".join(courses))


# Button 5: MIS Department

def mis_department():
    clear_label()
    courses = [
        "Intro to MIS",
        "Databases Management",
        "Systems Analysis & Design",
        "Business Analytics / Data Visualization",
        "Network and Information Security",
        "Project Management"
    ]
    lb.config(text="\n".join(courses))


# Buttons

button1 = Button(root, text='Calendar', command=calendar, bg="blue", fg="white", width=12)
button1.place(x=30, y=110)

button2 = Button(root, text='Buildings', command=building, bg="blue", fg="white", width=12)
button2.place(x=150, y=110)

button3 = Button(root, text='Faculty', command=faculty, bg="blue", fg="white", width=12)
button3.place(x=270, y=110)

button4 = Button(root, text='School of Business', command=business, bg="blue", fg="white", width=16)
button4.place(x=100, y=160)

button5 = Button(root, text='MIS Department', command=mis_department, bg="blue", fg="white", width=16)
button5.place(x=260, y=160)


# Run GUI

mainloop()