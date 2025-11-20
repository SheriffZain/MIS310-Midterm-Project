#Midterm Project 1

#import the required modules
import tkinter as tk
from tkinter import StringVar
#create the main window
main_window = tk. Tk()
#set up the size
main_window.geometry("340x340")
#give it a name
main_window.title("Serendipity Booksellers")
#background color
main_window.configure(bg="lightblue")
# Function to calculate points based on number of books
def calculate_points():
    try:
        books = int(entry_text.get())
        if books <= 0:
            points = 0
        elif books == 2:
            points = 5
        elif books == 4:
            points = 15
        elif books == 6:
            points = 30
        elif books >= 8:
            points = 60
        else:
            # For odd numbers not specifically listed, assign 0 points
            points = 0
        result_text.set(f"Points awarded: {points}")
    except ValueError:
        result_text.set("Please enter a valid integer")

# StringVars for input and output
entry_text = StringVar()
result_text = StringVar()

# Label widget for instructions
label = tk.Label(main_window, text="Enter the number of books purchased this month:", font=("Arial", 12), bg="lightblue")
label.pack(pady=10)

# Entry widget for user input
entry = tk.Entry(main_window, textvariable=entry_text, font=("Arial", 12), width=10)
entry.pack(pady=5)

# Button to calculate points
calc_button = tk.Button(main_window, text="Compute Points", font=("Arial", 12), command=calculate_points, bg="#FFD700")
calc_button.pack(pady=5)

# Button to display result
display_button = tk.Button(main_window, text="Show Result", font=("Arial", 12), command=lambda: result_label.config(text=result_text.get()), bg="#FFD700")
display_button.pack(pady=5)

# Label to display points
result_label = tk.Label(main_window, text="", font=("Arial", 12), fg="blue", bg="lightblue")
result_label.pack(pady=10)

main_window.mainloop()
