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
            self.wlc()
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

if __name__ == "__main__":
    root = Tk()
    db(root)

    root.mainloop()
