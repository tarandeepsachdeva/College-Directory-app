from tkinter import *
from tkinter import filedialog,messagebox
import home_page
import registeration

class login_page:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x450+450+150")
        self.root.title("login page")
        
    def next(self):
        self.name = self.entry.get()
        self.passwords = self.entry2.get()
        
        

        
        if not self.name and self.passwords:
            messagebox.showerror("ERROR! Please enter you credentials.... ")
        with open ("user.txt", "r") as file:
            data = file.readlines()
        check = FALSE
        for user in data:
            if self.name in user and  self.passwords in user:
                check = TRUE
                break
        if check:
            messagebox.showinfo("Login Succesfully")
            messagebox.showinfo("Success","Login Successful")
            self.root.destroy()
            obj1=home_page.Home_page()
            obj1.frame2()
            obj1.root.mainloop()
        
        else:
            messagebox.showerror("ERROR! Ivalid username and password")            


        
        
    def showw(self):
        if self.entry2.cget("show")=="*":
            self.entry2.config(show=NONE)
        else:
            self.entry2.config(show="*")
            
    def cng(self):
        if self.c.cget("bg")=="black":
            self.c.config(bg="White")
            self.label.config(bg="Black",fg="White")
            self.name.config(bg="Black",fg="White")
            self.password.config(bg="Black",fg="White")
            self.username.config(bg="Black",fg="White")
            
        elif self.c.cget("bg")=="White":
            self.c.config(bg="black")
            self.label.config(fg="Black",bg="White")
            self.name.config(fg="Black",bg="White")
            self.password.config(fg="Black",bg="White")
            self.username.config(fg="Black",bg="White")
    def frame1(self):
        self.c = Frame(self.root, bg="black")
        self.c.place(x = 10, y = 10, width=380, height=430)
        self.label = Label(self.c, text="Welcome to the PCTE Directory", bg="white", fg="black" )
        self.label.place(x=50, y=50, width=280, height=50)
        self.name = Label(self.c, text="Who's using it?",bg="black", fg='white')
        self.name.place(x =100, y=120, width=200, height=40 )
        self.username = Label(self.c, text="username",bg='black', fg="white" )
        self.username.place(x = 50, y=200, width=100, height=22)
        self.entry = Entry(self.c, border=20, borderwidth=5)
        self.entry.place(x=150, y=200, width=150, height=30)
        self.password = Label(self.c, text="password",bg='black', fg="white" )
        self.password.place(x = 50, y=250, width=100, height=22,)
        self.entry2 = Entry(self.c, border=20, borderwidth=5, show="*")
        self.entry2.place(x=150, y=250, width=150, height=30)
        self.btn = Button(self.c, text='LOGIN',bg='white', fg="black", command=self.next )
        self.btn.place(x=150, y=320, width=100, height=30) 
        self.btn1 = Button(self.c, text='show',bg='white', fg="black", command=self.showw )
        self.btn1.place(x=150, y=360, width=100, height=30)
        self.btn2 = Button(self.c,bg='white', fg="black", command=self.cng )
        self.btn2.place(x=10, y=60, width=30, height=30)


if __name__ == "__main__":
    obj = login_page()
    obj.frame1()

    obj.root.mainloop()        








    