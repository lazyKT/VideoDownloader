import os
import pygame
from tkinter import *
from tkinter import filedialog as fd


def browse():
    song_name = fd.askopenfilename(initialdir='/',filetypes=[('MP3 Files','*.mp3')])
    mp3.set(song_name)


def play():
    pygame.mixer.init()
    song_to_play = mp3.get()
    example = r"C:\Usrs\9380-85615SG\Desktop\StudyMaterials\Programming\Python\Youtube_Downloader\Downloads\Audios\Numb (Official Video) - Linkin Park.mp3"
    dir = os.path.join(os.getcwd(),r"Downloads\Audios")
    f = open(dir+'\\'+os.listdir(dir)[2],'r')
    print(type(f))
    print(type(song_to_play))
    pygame.mixer.music.load(song_to_play)
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()


def widgets():
    song = Entry(root, width=70, textvariable=mp3).grid(row=0)
    browse_btn = Button(root, widt=10, text=" Browse ", command=browse).grid(row=0,column=1)
    play_btn = Button(root, width=10, text=" Play ", command=play).grid(row=1)
    pause_btn = Button(root, width=10, text=" Pause ", command=pause).grid(row=1,column=1)
    resume_btn = Button(root, width=10, text=" Resume ", command=resume).grid(row=1,column=2)


if __name__ == "__main__":
    root = Tk()
    root.geometry('500x300')
    mp3 = StringVar()
    widgets()
    root.mainloop()


