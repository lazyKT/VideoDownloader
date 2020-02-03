from tkinter import *
from pytube import YouTube
import youtube_dl as mp3
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

def convertMP3():
    pass

#GUI
def createWidegets():
    url_lbl = Label(root, text="Enter video url:")
    url_lbl.grid(row='0',column='0',pady='20')       
    
    root.url_text_box = Entry(root)
    root.url_text_box.grid(row='1',column='0',padx='200',pady='10')
    
    dest_lbl = Label(root, text="Enter save dest:")
    dest_lbl.grid(row='2',column='0')

    root.dest_text_box = Entry(root)
    root.dest_text_box.grid(row='3',column='0',padx='200',pady='10')

    vdo_btn = Button(root, text="Download", command=download, bg='#00FFEE', fg='#000')
    vdo_btn.grid(row='4', column='0')

    mp3_btn = Button(root, text="Convert MP3", command=convertMP3, bg="#00AADD", fg="#000")
    mp3_btn.grid(row='5', column='0')



#root.geometry("650x120")
root.title("Youtube Downloader")

createWidegets()

root.mainloop()