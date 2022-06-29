from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    count_down(2 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    min_display = math.floor(count / 60)
    sec_display = count % 60
    if sec_display < 10:
        sec_display = f"0{sec_display}"

    canvas.itemconfig(timer_text, text=f"{min_display}:{sec_display}")
    if count > 0:
        print(min_display)
        window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)






# Title
timer_label = Label(text="timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 42, "italic"))
timer_label.grid(row=0, column=1)

# Tomato Logo
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=2, column=1)

# Buttons
start_butt = Button(text="Start", width=12, pady=5, command=start_timer)
start_butt.grid(row=3, column=0)

restart_butt = Button(text="Restart", width=12, pady=5)
restart_butt.grid(row=3, column=2)

# Tick marks
tick_marks = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "italic"))
tick_marks.grid(row=4, column=1)


window.mainloop()