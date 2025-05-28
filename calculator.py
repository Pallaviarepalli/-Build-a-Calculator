import tkinter as tk

# Function to handle button press
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to handle operations
def button_operation(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + operator)

# Function to evaluate the expression
def button_equal():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry field for the calculator
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=5, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=('Arial', 18), command=button_equal)
    else:
        button = tk.Button(root, text=text, width=5, height=3, font=('Arial', 18),
                           command=lambda t=text: button_click(t) if t not in '+-/*=' else button_operation(t))
    button.grid(row=row, column=col)

# Add a clear button
clear_button = tk.Button(root, text="C", width=5, height=3, font=('Arial', 18), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()
