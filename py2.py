from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import ffmpeg
from moviepy.editor import VideoFileClip

root = tk.Tk()
root.attributes("-toolwindow", True)

img = ImageTk.PhotoImage(Image.open(r"d:\python class\pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg"))
Label(master=root, image=img).pack(fill=BOTH, expand=True)

button = tk.Button(root, text="انتخاب ویدئو", width=50, font=45, fg="red", bg="blue")
button.place(relx=0.25, rely=0.3)


def open_file():
    root.filename = filedialog.askopenfilename(initialdir="C:/", title="انتخاب ویدئو", filetypes=[("Video files", "*.mp4")])

    video_name = root.filename.split("/")[-1]

    video_dir = root.filename.split("/")[:-1]

    output_path = "/".join(video_dir) + "/" + video_name.split(".")[0] + ".mp3"


    video_clip = VideoFileClip(root.filename)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)


    tk.Label(root, text="فایل صوتی با موفقیت در {} ذخیره شد".format(output_path)).pack()


button.config(command=open_file)


button1 = tk.Button(root, text="راهنما", width=50, font=45, fg="red", bg="blue")
button1.place(relx=0.25, rely=0.5)
button2 = tk.Button(root, text="تنظیمات برنامه", width=50, font=45, fg="red", bg="blue")
button2.place(relx=0.25, rely=0.7)


root.mainloop()



