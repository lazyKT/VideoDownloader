import sqlite3
from tkinter import *
from tkinter import messagebox as msb

with sqlite3.connect("youtube.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT  NOT NULL, password TEXT NOT NULL);")
cursor.execute("SELECT * FROM users")
db.commit()
db.close()



class db():
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        self.widgets()

    def login():
        with sqlite3.connect("youtube.db") as db:
            cursor = db.cursor()
        check_user = ("SELECT * FROM users WHERE username = ? AND password = ?")
        cursor.execute(check_user,[self.username.get(),self.password.get()])
        results = cursor.fetchall()
        if results:
            print("Existing User")
        else:
            print("Create new user!!")
    
    def createUser():
        pass

    def signup():
        pass

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
        Button(self.signup_frame, text = "  Back to Login  ", command = self.login).grid(row=2) 
        Button(self.signup_frame, text = "  Sign Up  ", command = self.createUser).grid(row = 2, column = 1)
        self.signup_frame.pack()


if __name__ == "__main__":
    root = Tk()
    db(root)

    root.mainloop()
