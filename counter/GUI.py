import tkinter as tk
import random
window=tk.Tk()
'''     
root = tk.Tk()
root.title("Counter")
greeting=tk.Label(root, text="Hello",fg="white",bg="black",width=20,height=5)
greeting.pack()

lebel=tk.Label(root,text="halo")
lebel.config(text="halo juga")
lebel.config(font=("Helvetica", 20))
lebel.pack()

def on_button():
    lebel.config(text="Hello World")

button=tk.Button(root,text="click me",command=on_button)
button.pack()
'''
window.config(bg="black")

window.title("Counter")

def increase():
    global counter
    counter += 1
    counter_label.config(text=f"counter: {counter}")

def decrease():
    global counter
    counter -= 1
    counter_label.config(text=f"counter: {counter}")
'''
def blue():
    colorname=["red","green","blue"]
    window.config(bg=random.choice(colorname))

blue_button=tk.Button(window,text="change bg color",command=blue)
blue_button.pack(side="left",pady=20,padx=20)
'''
counter=0

if counter >= 50:
    window.config(bg="green")
elif counter <= -50:
    window.config(bg="red")
else:
    window.config(bg="white")

counter = 0
counter_label = tk.Label(window, text=f"counter: {counter}")
counter_label.pack(pady=20)

increase_button = tk.Button(window, text="Increase", command=increase)
increase_button.pack(side="left", pady=20,padx=20)

decrease_button = tk.Button(window, text="Decrease", command=decrease)
decrease_button.pack(side="left", pady=20, padx=20)



window.mainloop()