
from tkinter import *
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

# ---------UI setup----------------
window = Tk()
window.title("Pomodoro technique")
window.minsize(500, 300)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)   #here x = 100 and y = 112 
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.pack()


window.mainloop()


