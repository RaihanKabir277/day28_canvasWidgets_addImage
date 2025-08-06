
from tkinter import *
import math
# print("day 28 starts here..")

# --------------Consants-----------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# -------------Countdown mechanism --------------
def start_timer():
    # --------call the function for count down -----
    count_down(5 * 60)

def count_down(count):
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------UI setup----------------
window = Tk()
window.title("Pomodoro technique")
window.minsize(500, 300)
window.config(padx=200, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 50, "bold", ))
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)   #here x = 100 and y = 112 
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



start_btn = Button(text="Start",command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=2)
start_btn.config(padx=5,pady=5)

reset_btn = Button(text="Reset",highlightthickness=0)
reset_btn.grid(column=2 , row=2)
reset_btn.config(padx=5, pady=5)

check_mark = Label(text="✓",font=(FONT_NAME,25,"bold"), fg=RED, bg=YELLOW, highlightthickness=0, pady=20)
check_mark.grid(column=1, row=2)





window.mainloop()



