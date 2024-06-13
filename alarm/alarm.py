import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pytz

#set time zone
tz = pytz.timezone('Asia/kuala_lumpur')\


def update_time():
    current_time = datetime.now(tz).strftime(time_format.get())
    label.config(text=current_time)
    label.after(1000, update_time)
    chack_alarm(current_time)
def alarm():
    alarm_time_str = alarm_time.get()
    alarm_datetime = datetime.strptime(alarm_time_str, "%H:%M:%S")
    alarm_hour=alarm_datetime.hour
    alarm_minute=alarm_datetime.minute
    alarm_seccond=alarm_datetime.second
    alarm_active.set(True)
    alarm_label.config(text="Alarm Set for: " + alarm_time_str)
def chack_alarm(current_time):
    if alarm_active.get() and alarm_active.get()==current_time:
        messagebox.showinfo("Alarm", "Time to Wake Up")

        alarm_active.set(False)
        alarm_label.config(text="")



root=tk.Tk()
root.geometry("300x300")
root.title("Alarm Clock")
root.config(bg="lightblue")

frame=tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor="center")

label=tk.Label(frame, font=("Arial", 100), bg="lightblue")
label.pack()

alarm_time = tk.StringVar()
alarm_time.set("00:00:00")
alarm_entry = tk.Entry(frame, textvariable=alarm_time, font=("Arial", 20))
alarm_entry.pack(pady=10)

time_format=tk.StringVar()
time_format.set("%H:%M:%S")

alarm_label = tk.Label(frame, font=("Arial", 50), bg="lightblue")
alarm_label.pack(pady=10)
alarm_active = tk.BooleanVar()
alarm_active.set(True)

set_alarm_button = tk.Button(frame, text="Set Alarm", font=("Arial", 20), command=alarm)
set_alarm_button.pack(pady=10)




update_time()

root.mainloop()