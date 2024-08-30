import tkinter


def btn_clicked():
    new_label = input.get()
    label["text"] = new_label


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# label.pack()
label.grid(column=0, row=0)

input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=1, row=1)

btn = tkinter.Button(text="Click Me", command=btn_clicked)
# btn.pack()
btn.grid(column=2, row=2)

window.mainloop()
