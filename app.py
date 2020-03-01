import os 
import shutil
import youtube_dl
import pygame
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as msg

class playlist():

    def __init__(self, root):
        self.root = root
        self.youtube_link = StringVar()
        self.views()
    
    
    def refresh(self):
        self.listbox.delete(0,END)

        play_list = os.listdir("Downloads/Audios")
        for p in play_list:
            self.listbox.insert(END,p)
        self.listbox.pack()

    def add(self):
        self.playlist_frame.pack_forget()
        self.listbox.pack_forget()
        self.player_frame.pack_forget()
        self.add_playlist_frame.pack()
    

    def browse_from_local(self):
        new_song_location = fd.askopenfilename(initialdir="/", title="Choose mp3 from local", filetypes=[("MP3 Files", "*.mp3")])
        play_list_location = r"Downloads\Audios"
        shutil.copy2(new_song_location,play_list_location)
        msg.showinfo(title=None,message="Playlist Updated")

    def download_from_youtube(self):
        self.add_playlist_frame.pack_forget()
        self.add_from_youtube_frame.pack()

    def save_from_youtube(self):
        download_dest = r"Downloads\Audios"
        vdo_url = self.youtube_link.get()
        download_output = {
            'format': 'bestaudio/best',
            'outtmpl': download_dest + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '320'
            }]
        }
        with youtube_dl.YoutubeDL(download_output) as ydl:
            ydl.download([vdo_url])
        msg.showinfo(title=None, message="MP3 has been downloaded and added to playlist successfully!!")
        self.add_from_youtube_frame.pack_forget()
        self.add_playlist_frame.pack()

    
    def back(self):
        self.add_playlist_frame.pack_forget()
        self.playlist_frame.pack()
        self.listbox.pack()
        self.player_frame.pack()
        self.refresh()

    def back_youtube(self):
        self.add_from_youtube_frame.pack_forget()
        self.playlist_frame.pack()
        self.listbox.pack()
        self.player_frame.pack()
        self.refresh()

    def locate_song_file(self,name):
        current_dir = os.getcwd()
        song_directory = os.path.join(current_dir+'\\Downloads\\Audios\\'+name)
        song_file = open(song_directory,'r')
        return song_file


    def play(self):
        pygame.mixer.init()
        song = self.listbox.get(self.listbox.curselection())
        pygame.mixer.music.load(self.locate_song_file(song))
        pygame.mixer.music.play()
        #self.play_button.grid_forget()
    
    def stop(self):
        pygame.mixer.music.stop()
        # self.play_button.pack()
        # self.stop_button.pack_forget()

    def pause(self):
        pygame.mixer.music.pause()
        # self.resume_button.pack()
        # self.pause_button.pack_forget()
    
    def resume(self):
        pygame.mixer.music.unpause()
        # self.pause_button.pack()   
        # self.resume_button.pack_forget()     


    def views(self):

        self.playlist_frame = Frame(self.root, padx=10, pady=10)
        #Label(self.playlist_frame, width = 500,text = " Play List ").pack()
        Button(self.playlist_frame, width = 15, text = "Refresh", command=self.refresh).grid(row=0,column=0)
        Button(self.playlist_frame, width = 15, text = " Add to playlist ", command=self.add).grid(row=0,column=1)
        self.playlist_frame.pack()

        self.listbox = Listbox(self.root, width = 400, bd = "1")
        play_list = os.listdir("Downloads/Audios")
        for p in play_list:
            self.listbox.insert(END,p)  
        self.listbox.pack()
        #self.add_btn = Button(self.root, width = 10, text = " Add ", command=self.add).pack()

        self.player_frame = Frame(self.root, padx=10, pady=10)
        Button(self.player_frame, text = "  Play  ", command=self.play).grid(row=2) 
        Button(self.player_frame, text = "  Resume  ", command=self.resume).grid(row = 2, column = 1)
        Button(self.player_frame, text = "  Pause  ", command=self.pause).grid(row = 2, column = 2)
        Button(self.player_frame, text = "  Stop  ", command=self.stop).grid(row = 2, column = 3)
        self.player_frame.pack()


        self.add_playlist_frame = Frame(self.root)
        add_lbl = Label(self.add_playlist_frame, width=300, text =" Add to playlist ").pack()
        browse_btn = Button(self.add_playlist_frame, width=50, text =" Browse from Local ", command=self.browse_from_local).pack()
        youtube_btn = Button(self.add_playlist_frame, width=50, text =" Download from YouTube ", command=self.download_from_youtube)
        youtube_btn.pack()
        back_btn = Button(self.add_playlist_frame, width=50, text=" Back to PlayList", command=self.back).pack()

        self.add_from_youtube_frame = Frame(self.root)
        Label(self.add_from_youtube_frame, text="Enter the video url : ").grid(row=0,sticky=W)
        Entry(self.add_from_youtube_frame, width=70, textvariable=self.youtube_link).grid(row=0,column=1)
        Button(self.add_from_youtube_frame, width=10, text=" Download ", command=self.save_from_youtube).grid(row=1)
        Button(self.add_from_youtube_frame, width=10, text=" Back ", command=self.back_youtube).grid(row=1,column=1)

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x400")
    playlist(root)
    root.title("YouTube2Mp3")
    root.mainloop()