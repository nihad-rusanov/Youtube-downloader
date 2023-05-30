from tkinter import *
from pytube import YouTube
import os

def download_video():
    try:
        label.config(text="downloading... ")
        tk.update()
        link = entry.get()
        desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
        YouTube(link).streams.get_highest_resolution().download(output_path=desktop)
        label.config(text="video downloaded in desktop")

    except:
        label.config(text="something went wrong")

tk = Tk()

tk.title("Youtube Video Downloader App")
tk.geometry("500x300")

label = Label(text="Welcome My App", font=("Arial", 25, "italic"), anchor=CENTER)
entry = Entry(width=40)
button = Button(text="Download", width=15, height=1, command=download_video)

label.pack(pady=30)
entry.pack(pady=10)
button.pack(padx=10)

tk.mainloop()
