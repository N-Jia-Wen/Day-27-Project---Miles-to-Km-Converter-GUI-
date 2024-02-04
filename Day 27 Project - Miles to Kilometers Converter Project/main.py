from tkinter import *

# Creates the window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Creates label which specifies unit of input to be Miles
miles_unit = Label(text="Miles", font=("Verdana", 10))
miles_unit.grid(row=0, column=2)

# Creates label which specifies unit of output to be Km
Km_unit = Label(text="Km", font=("Verdana", 10))
Km_unit.grid(row=1, column=2)

# Creates label which tells user that the input and output value (in their respective units) are equal
equal_to_label = Label(text="is equal to", font=("Verdana", 10))
equal_to_label.grid(row=1, column=0)


# Function to be tied to when button is pressed. Converts miles to km and changes the displayed output text.
def calculate_button():
    miles_num = float(miles_input.get())
    km_num = round(miles_num*1.609)
    km_output.config(text=km_num)


# Creates entry text box for user to input the number of miles
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

# Shows default value of 0. Is updated when button is pressed to show the equivalent number of km to the inputted miles
km_output = Label(text="0", font=("Verdana", 10))
km_output.grid(row=1, column=1)

# Creates button which carries out conversion when pressed
button = Button(text="Calculate", command=calculate_button, font=("Verdana", 10))
button.grid(row=2, column=1)


window.mainloop()
