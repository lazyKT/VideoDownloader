from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import youtube_dl
import os


def browse():
    dwld_directory = filedialog.askdirectory(initialdir="/")
    download_path.set(dwld_directory)


def download_video():
    url = youtube_link.get()
    save_dest = download_path.get()

    dwdl_opts = {
        'outtmpl' : save_dest + "/%(title)s.%(ext)s",
    }
    with youtube_dl.YoutubeDL(dwdl_opts) as ydl:
        ydl.download([url])
    des_lbl = Label(root, text="Download successful")
    des_lbl.grid(row='6',column='0')


def download_audio():
    print("Audio file is about to be downloaded!!")
    url = youtube_link.get()
    save_dest = download_path.get()

    #des_lbl = Label(root,text="Download Starting...")
    dwdl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': save_dest+"/%(title)s.%(ext)s",
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '320'
        }],
    }
    with youtube_dl.YoutubeDL(dwdl_opts) as ydl:
        ydl.download([url])
    des_lbl = Label(root, text="Download successful")
    des_lbl.grid(row='6',column='0')

#GUI
def createWidegets():
    url_lbl = Label(root, text="Enter video url:")
    url_lbl.grid(row='0',column='0',pady='20')       
    
    root.url_text_box = Entry(root,width='60', textvariable=youtube_link)
    root.url_text_box.grid(row='1',column='0',padx='20',pady='10')
    
    dest_lbl = Label(root, text="Enter save dest:")
    dest_lbl.grid(row='2',column='0')

    root.dest_text_box = Entry(root,width='50', textvariable=download_path)
    root.dest_text_box.grid(row='3',column='0',padx='20',pady='10')

    browse_btn = Button(root, text="Browse", command=browse,padx='5')
    browse_btn.grid(row='3',column='1')

    vdo_btn = Button(root, text="Video MP4", command=download_video, bg='#00FFEE', fg='#000')
    vdo_btn.grid(row='4', column='0')

    mp3_btn = Button(root, text="Audio MP3", command=download_audio, bg="#00AADD", fg="#000")
    mp3_btn.grid(row='5', column='0')

if __name__ == '__main__':
    root = Tk()
    #root.geometry("650x120")
    root.title("Youtube Downloader")

    download_path = StringVar()
    youtube_link = StringVar()

    createWidegets()

    root.mainloop()