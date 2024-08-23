from tkinter import *
from datetime import datetime, timedelta

GREY = "#e0e1dd"
METAL_BLUE = "#778da9"
NAVY = "#415a77"
DARK_NAVY = "#1b263b"
FONT_NAME = "Brush Script MT"

event_date = datetime(2024, 9, 30, 18, 0)


def update_timer():
    now = datetime.now()
    time_remaining = event_date - now
    if time_remaining > timedelta(0):
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{time_remaining.days}d {hours:02}:{minutes:02}:{seconds:02}"
    else:
        time_str = "00:00:00"

    canvas.itemconfig(timer_text, text=time_str)
    window.after(1000, update_timer)


window = Tk()
window.title("Sliabh Hiking trip countdown!")
window.iconphoto(True, PhotoImage(file='logo-4.png'))
window.geometry("900x650")
window.config(padx=100, pady=50, bg=GREY)

small_logo = PhotoImage(file="logo-4.png")
image_label = Label(window, image=small_logo)
image_label.grid(column=2, row=0)


title_label = Label(text="Time to our next adventure ", fg=METAL_BLUE, bg=GREY, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=600, height=600, bg=GREY, highlightthickness=0)
mountain_img = PhotoImage(file="mountains.png")
canvas.create_image(300, 200, image=mountain_img)
canvas.grid(column=1, row=1)


timer_text = canvas.create_text(300, 400, text="00:00", fill=DARK_NAVY, font=(FONT_NAME, 35, "bold"))


update_timer()

window.mainloop()
