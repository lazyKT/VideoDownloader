from tkinter import *
import os

class test_gui():
    
    def __init__(self,master):
        self.master = master
        self.widgets()

    
    def refresh(self):
        self.song_lst.delete(0,END)
        test_ls = [1,2,3,4,5,6,7,8]
        for t in test_ls:
            self.song_lst.insert(END,t)
        self.song_lst.pack()


    def widgets(self):

        self.login_frame =  Frame(self.master, padx=10, pady=10)
        Button(self.login_frame, text = "  Refresh  ", command=self.refresh).grid(row=2) 
        Button(self.login_frame, text = "  Add Songs  ").grid(row = 2, column = 1)
        self.login_frame.pack()

        self.song_lst = Listbox(self.master)
        ls = [1,2,3,4]
        for l in ls:
            self.song_lst.insert(END,l)
        self.song_lst.pack()

        self.player_frame = Frame(self.master, padx=10, pady=10)
        Button(self.player_frame, text = "  Play  ").grid(row=2) 
        Button(self.player_frame, text = "  Resume  ").grid(row = 2, column = 1)
        self.player_frame.pack()

if __name__ == "__main__":
    root = Tk()
    test_gui(root)

    root.mainloop()
        