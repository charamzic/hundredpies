import tkinter


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label["text"] = f"{km}"


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)

km_result_label = tkinter.Label(text="0", font=("Arial", 24, "bold"))
km_result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

calculate_btn = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)


window.mainloop()
