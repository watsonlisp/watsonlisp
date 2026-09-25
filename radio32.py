import tkinter as tk
import os

def execute_program():
    selected_program = var.get()
    if selected_program == "Program 1":
        os.system("c:/python/beat10.py")
    elif selected_program == "Program 2":
        os.system("c:/python/drunk5.py")
    elif selected_program == "Program 3":
        os.system("c:/python/obsurd3.py")
    elif selected_program == "Program 4":
        os.system("c:/python/happy30.py")
    elif selected_program == "Program 5":
        os.system("c:/python/dream3.py")
    elif selected_program == "Program 6":
        os.system("c:/python/circuit110.py")


# Create the main window
root = tk.Tk()
root.title("Program Selector")

# Create a Tkinter variable
var = tk.StringVar(value="Program 1")

# Create radio buttons
radio1 = tk.Radiobutton(root, text="beat", variable=var, value="Program 1")
radio2 = tk.Radiobutton(root, text="drunk", variable=var, value="Program 2")
radio3 = tk.Radiobutton(root, text="obsud", variable=var, value="Program 3")
radio4 = tk.Radiobutton(root, text="happy", variable=var, value="Program 4")
radio5 = tk.Radiobutton(root, text="dream", variable=var, value="Program 5")
radio6 = tk.Radiobutton(root, text="circuit__________________________", variable=var, value="Program 6")
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
