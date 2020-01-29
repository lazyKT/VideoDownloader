from tkinter import *
from pytube import YouTube
import os

root = Tk()

def download():
    vdo_url = url_text_box.get()
    save_dest = dest_text_box.get()
    checkLocation(save_dest)
    YouTube(vdo_url).streams.first().download(save_dest)


def checkLocation(save_dest):
    if os.path.isdir(save_dest):
        print("Valid Location. Download gonna starts soon!!")
    else:
        print("Invalid Location.Creating new directory!!")
        os.makedirs(save_dest)

url_lbl = Label(root, text="Enter video url:")
url_text_box = Entry(root)
dest_lbl = Label(root, text="Enter save dest:")
dest_text_box = Entry(root)
btn = Button(root, text="Download", command=download, bg='#00FFEE', fg='#000')

url_lbl.grid(row='0',column='0',pady='20')
url_text_box.grid(row='1',column='0',padx='200',pady='10')
dest_lbl.grid(row='2',column='0')
dest_text_box.grid(row='3',column='0',padx='200',pady='10')
btn.grid(row='4', column='0')


root.mainloop()