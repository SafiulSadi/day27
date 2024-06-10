from tkinter import *

window = Tk()
window.title("My First GUI Program.")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label.config(padx=5, pady=5)
my_label.grid(row=1, column=0)

input = Entry(width=10)
input.grid(row=0, column=1)
x = input.get()

my_label_miles = Label(text="Miles", font=("Arial", 24, "bold"))
my_label_miles.config(padx=5, pady=5)
my_label_miles.grid(row=0, column=2)


my_label_km = Label(text="Km", font=("Arial", 24, "bold"))
my_label_km.config(padx=5, pady=5)
my_label_km.grid(row=1, column=2)

# Button


def button_clicked():
    print("I got clicked")
    x = int(input.get())
    calc = round(x*1.609, 2)
    my_label_ans.config(text=f"{calc}")


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

# Entry

my_label_ans = Label(text=f"", font=("Arial", 24, "bold"))
my_label_ans.config(padx=5, pady=5)
my_label_ans.grid(row=1, column=1)











window.mainloop()
