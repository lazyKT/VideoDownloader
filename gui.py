from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msb
from pytube import YouTube
import youtube_dl
import os
import sqlite3


def db_connect():
    with sqlite3.connect("youtube.db") as db:
        cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL, password TEXT NOT NULL);")
    #cursor.execute("CREATE TABLE IF NOT EXISTS songs(username TEXT NOT NULL,songs TEXT NOT NULL);") 
    db.commit()
    db.close()


class db():
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        self.download_path = StringVar()
        self.youtube_link = StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect("youtube.db") as db:
            cursor = db.cursor()
        check_user = ("SELECT * FROM users WHERE username = ? AND password = ?")
        cursor.execute(check_user,[self.username.get(),self.password.get()])
        print(self.username.get()+" "+self.password.get())
        results = cursor.fetchall()
        if results:
            print("Login Successful")
            msb.showinfo("Login Successfully")
            self.login_frame.pack_forget()
            self.head["text"] = ""
            self.home_frame.pack()
            wlc_label = Label(self.home_frame,text="Welcome "+self.username.get()).grid(row='0',column='0')
            print(self.username.get())
        else:
            print("Create new user!!")
            msb.showerror("Incorrect credentials")
            
    
    
    def createUser(self):
        with sqlite3.connect("youtube.db") as db:
            cursor = db.cursor()
        check_user = ("SELECT * FROM users WHERE username = ?")
        cursor.execute(check_user,[self.username.get()])
        if cursor.fetchall():
            msb.showerror("Username already taken!!")
            self.signup()
        else:
            msb.showinfo("User Created Successfully!")
            self.log()
        create_user = "INSERT into users(username,password) VALUES(?,?)"
        cursor.execute(create_user,[self.new_username.get(),self.new_password.get()])
        db.commit()
        print("Created!!")

    #Call login Frame
    def log(self):
        self.username.set("")
        self.password.set("")
        self.signup_frame.pack_forget()
        self.head["text"] = "  LOG IN  "
        self.login_frame.pack()

    #Call sing up frame
    def signup(self):
        self.new_username.set("")
        self.new_password.set("")
        self.login_frame.pack_forget()
        self.head["text"] = "  SIGN UP  "
        self.signup_frame.pack()
    
    def wlc(self):
        self.head["text"] = " Welcome " + self.username.get()

    def widgets(self):
        self.head = Label(self.master,text = "    LOGIN    ",font = ('freesansblod',35), pady=40)
        self.head.pack()

        #Login Frame
        self.login_frame =  Frame(self.master, padx=10, pady=10)
        Label(self.login_frame, text = "Username: ", padx = 5, pady = 5).grid(sticky=W)
        Entry(self.login_frame, textvariable = self.username, bd = 8).grid(row=0, column = 1, sticky = E)
        Label(self.login_frame, text = "Password: ", padx = 5, pady = 5).grid(row=1, column = 0, sticky=W)
        Entry(self.login_frame, textvariable = self.password, bd = 8).grid(row=1, column = 1, sticky = E)
        Button(self.login_frame, text = "  Login  ", command = self.login).grid(row=2) 
        Button(self.login_frame, text = "  Sign Up  ", command = self.signup).grid(row = 2, column = 1)
        self.login_frame.pack()

        #SignUp Frame
        self.signup_frame =  Frame(self.master, padx=10, pady=10)
        Label(self.signup_frame, text = "Username: ", padx = 5, pady = 5).grid(sticky=W)
        Entry(self.signup_frame, textvariable = self.new_username, bd = 8).grid(row=0, column = 1, sticky = E)
        Label(self.signup_frame, text = "Password: ", padx = 5, pady = 5).grid(row=1, column = 0, sticky=W)
        Entry(self.signup_frame, textvariable = self.new_password, bd = 8).grid(row=1, column = 1, sticky = E)
        Button(self.signup_frame, text = "  Back to Login  ", command = self.log).grid(row=2) 
        Button(self.signup_frame, text = "  Sign Up  ", command = self.createUser).grid(row = 2, column = 1)
        #self.signup_frame.pack()

        #home
        self.home_frame = Frame(self.master)
        url_lbl = Label(self.home_frame, text="Enter video url:")
        url_lbl.grid(row='1',column='0',pady='20')       
        root.url_text_box = Entry(self.home_frame,width='60', textvariable=self.youtube_link)
        root.url_text_box.grid(row='2',column='0',padx='20',pady='10')
        dest_lbl = Label(self.home_frame, text="Enter save dest:")
        dest_lbl.grid(row='3',column='0')
        root.dest_text_box = Entry(self.home_frame,width='50', textvariable=self.download_path)
        root.dest_text_box.grid(row='4',column='0',padx='20',pady='10')
        browse_btn = Button(self.home_frame, text="Browse", command=self.browse,padx='5')
        browse_btn.grid(row='4',column='1')
        vdo_btn = Button(self.home_frame, text="Video MP4", command=self.download_video, bg='#00FFEE', fg='#000')
        vdo_btn.grid(row='6', column='0')
        mp3_btn = Button(self.home_frame, text="Audio MP3", command=self.download_audio, bg="#00AADD", fg="#000")
        mp3_btn.grid(row='7', column='0')


    def browse(self):
        dwld_directory = filedialog.askdirectory(initialdir="/")
        self.download_path.set(dwld_directory)


    def download_video(self):
        url = self.youtube_link.get()
        save_dest = self.download_path.get()

        dwdl_opts = {
            'outtmpl' : save_dest + "/%(title)s.%(ext)s",
        }
        with youtube_dl.YoutubeDL(dwdl_opts) as ydl:
            ydl.download([url])
        des_lbl = Label(self.home_frame, text="Download successful")
        des_lbl.grid(row='8',column='0')


    def download_audio(self):
        print("Audio file is about to be downloaded!!")
        url = self.youtube_link.get()
        save_dest = self.download_path.get()

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
            print("title : "+ydl['title'])
            print("file name :  " + dwdl_opts['outtmpl'])
        des_lbl = Label(self.home_frame, text="Download successful")
        des_lbl.grid(row='6',column='0')


if __name__ == '__main__':
    root = Tk()
    #root.geometry("650x120")
    db(root)
    root.title("Youtube Downloader")

    root.mainloop()