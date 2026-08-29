import tkinter as tk

def info():
    city = citye.get()
    print(city)
window = tk.Tk()

window.title("Weather Dashboard")

window.geometry("400x300")

title=tk.Label(window,text="WEATHER DASHBOARD")
title.pack()

citye=tk.Entry(window)
citye.pack()

button = tk.Button(window, text="GET WEATHER", command=info)
button.pack()

window.mainloop()