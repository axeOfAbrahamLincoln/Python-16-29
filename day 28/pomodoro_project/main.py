from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TITLE = "T i m e r"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
timer = None
rep = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer to initial state, cancels any scheduled countdown, and clears session count"""
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white")
    label_title.config(text=TITLE, fg=GREEN)
    label_checkmark.config(text="")
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Manages the Pomodoro timer cycles: work, short break, and long break.

    Cycle: Work -> Short Break -> Work -> Short Break -> ... -> Work -> Long Break
    Long break occurs every 8 sessions (after 4 complete work cycles).
    """
    work_seconds = WORK_MIN * 60 - 1
    short_break_seconds = SHORT_BREAK_MIN * 60 - 1
    long_break_seconds = LONG_BREAK_MIN * 60 - 1
    global rep
    rep += 1

    # Determine which session type to start based on session count
    if rep % 8 == 0:
        count_down(long_break_seconds)
        label_title.config(
            text="L O N G   B R E A K", font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=RED
        )
    elif rep % 2 == 0:
        count_down(short_break_seconds)
        label_title.config(
            text="B R E A K", font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=PINK
        )
    else:
        count_down(work_seconds)
        label_title.config(
            text="W O R K", font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=GREEN
        )


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Recursively counts down from the given seconds, updating the display every second.

    When countdown reaches zero, automatically starts the next session.
    Also updates the checkmark count for completed work sessions.
    """
    # Convert total seconds into minutes and remaining seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Format time with leading zeros (e.g., "05:30" instead of "5:30")
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    # Update the canvas timer display
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Schedule the next countdown call in 1 second
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # When countdown completes, start the next session
        start_timer()
        # Update checkmarks: one checkmark for each completed work session
        # How work_session is calculated:
        # - rep counts every session (work + break): 1, 2, 3, 4, 5, 6, 7, 8...
        # - Odd rep numbers (1, 3, 5, 7...) are WORK sessions
        # - Even rep numbers (2, 4, 6, 8...) are BREAK sessions
        # - To count only completed work sessions: divide rep by 2 and floor it
        # - Example: rep=4 means 2 work sessions completed (rep/2 = 2)
        # - Example: rep=7 means 3 work sessions completed (rep/2 = 3.5, floor = 3)
        checkmarks = ""
        work_session = math.floor(rep / 2)  # Calculate number of completed work cycles
        # Create a checkmark for each completed work session
        for _ in range(work_session):
            checkmarks += "✔"
        label_checkmark.config(text=checkmarks)  # Display checkmarks on the UI


# ---------------------------- UI SETUP ------------------------------- #
# WINDOW - Main application window configuration

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# CANVAS - Display area for the tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1, pady=20)

# LABELS - Display title and checkmarks
label_title = Label(text=TITLE, font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=GREEN)
label_title.grid(row=0, column=1)

label_checkmark = Label(bg=YELLOW, fg=GREEN)
label_checkmark.grid(row=3, column=1)

# BUTTONS - Interactive controls for timer
button_start = Button(
    text="Start", width=5, highlightbackground=YELLOW, command=start_timer
)
button_start.grid(row=2, column=0)

button_reset = Button(
    text="Reset", width=5, highlightbackground=YELLOW, command=reset_timer
)
button_reset.grid(row=2, column=2)

window.mainloop()
