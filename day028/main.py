import threading
import tkinter as tk

from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_SOUND = "sound.mp3"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def play_sound():
    threading.Thread(target=playsound, args=(TIMER_SOUND,), daemon=True).start()


def countdown(count):
    count_min = count // 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count % 60:02d}")
    if count == 15:
        play_sound()
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_marks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(
    110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_btn = tk.Button(
    text="Start",
    borderwidth=0,
    highlightbackground=YELLOW,
    bg=YELLOW,
    highlightthickness=0,
    pady=5,
    command=start_timer,
)
start_btn.grid(column=0, row=2)

reset_btn = tk.Button(
    text="Reset",
    borderwidth=0,
    highlightbackground=YELLOW,
    bg=YELLOW,
    highlightthickness=0,
    pady=5,
    command=reset_timer,
)
reset_btn.grid(column=2, row=2)

check_marks_label = tk.Label(fg=GREEN, bg=YELLOW)
check_marks_label.grid(column=1, row=3)

window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
