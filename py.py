from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import filedialog

root=tk.Tk()
root.attributes("-toolwindow", True)

img=ImageTk.PhotoImage(Image.open(r"d:\python class\pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg"))
Label(
    master=root,
    image=img
).pack(fill=BOTH,expand=True)

button=tk.Button(root,text="Input video",width=50,font=45,fg="red",bg="blue")
button.place(relx=0.25,rely=0.3)

def open_file():
    root.filename = filedialog.askopenfilename(initialdir="C:/", title="Select a file", filetypes=[("Video files", "*.mp4")])
    #print(root.filename)

button1=tk.Button(root,text="Help",width=50,font=45,fg="red",bg="blue")
button1.place(relx=0.25,rely=0.5)
button2=tk.Button(root,text="Program settings",width=50,font=45,fg="red",bg="blue")
button2.place(relx=0.25,rely=0.7)
button.config(command=open_file)

root.mainloop()






# قسمت اخری کدم
# from tkinter import *
# from PIL import Image,ImageTk
# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.attributes("-toolwindow", True)

# img = ImageTk.PhotoImage(Image.open(r"d:\python class\pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg"))
# Label(
#     master=root,
#     image=img
# ).pack(fill=BOTH, expand=True)

# button = tk.Button(root, text="Input video", width=50, font=45, fg="red", bg="blue")
# button.place(relx=0.25, rely=0.3)

# def open_file():
#     root.filename = filedialog.askopenfilename(initialdir="C:/", title="Select a file", filetypes=[("Video files", "*.mp4")])
#     #print(root.filename)

# button1 = tk.Button(root, text="Help", width=50, font=45, fg="red", bg="blue")
# button1.place(relx=0.25, rely=0.5)
# button2 = tk.Button(root, text="Program settings", width=50, font=45, fg="red", bg="blue")
# button2.place(relx=0.25, rely=0.7)
# button.config(command=open_file)

# def save_video():
#     if root.filename:
#         save_path = filedialog.asksaveasfilename(initialdir="C:/", title="Save video as", filetypes=[("Video files", "*.mp4")])
#         if save_path:
#             # Copy the selected video file to the specified save path
#             os.system(f"copy {root.filename} {save_path}")
#             print("Video saved successfully!")

# button3 = tk.Button(root, text="Save video", width=50, font=45, fg="red", bg="blue")
# button3.place(relx=0.25, rely=0.9)
# button3.config(command=save_video)

# root.mainloop()
