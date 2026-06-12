import tkinter as tk
import os

def execute_program():
    selected_program = var.get()
    if selected_program == "Program 1":
        os.system("c:/python/eject12.py")
    elif selected_program == "Program 2":
        os.system("c:/python/hangman2.py")
    elif selected_program == "Program 3":
        os.system("c:/python/company4.py")
    elif selected_program == "Program 4":
        os.system("c:/python/lies7.py")
    elif selected_program == "Program 5":
        os.system("c:/python/choice6.py")
    elif selected_program == "Program 6":
        os.system("c:/python/flight59.py")


# Create the main window
root = tk.Tk()
root.title("Program Selector")

# Create a Tkinter variable
var = tk.StringVar(value="Program 1")

# Create radio buttons
radio1 = tk.Radiobutton(root, text="eject", variable=var, value="Program 1")
radio2 = tk.Radiobutton(root, text="hangman", variable=var, value="Program 2")
radio3 = tk.Radiobutton(root, text="company", variable=var, value="Program 3")
radio4 = tk.Radiobutton(root, text="lies", variable=var, value="Program 4")
radio5 = tk.Radiobutton(root, text="choice", variable=var, value="Program 5")
radio6 = tk.Radiobutton(root, text="flight__________________________", variable=var, value="Program 6")
# Pack the radio buttons

radio1.pack(anchor=tk.W)
radio2.pack(anchor=tk.W)
radio3.pack(anchor=tk.W)
radio4.pack(anchor=tk.W)
radio5.pack(anchor=tk.W)
radio6.pack(anchor=tk.W)

# Create a button to execute the selected program
execute_button = tk.Button(root, text="Execute", command=execute_program)
execute_button.pack()

# Run the main loop
root.mainloop()
