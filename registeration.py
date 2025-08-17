from tkinter import *
from tkinter import messagebox
import login_form

class SignupPage:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x450+450+150")
        self.root.title("Sign-up Page")
        self.root.config(bg="white")

        

    def content(self):
        
        self.title = Label(self.root, text="Sign-up Form", bg="white", fg="black", font=("Arial", 20))
        self.title.place(x=130, y=20, width=120)

        self.name_entry = Entry(self.root, bg="white", fg="BLack")
        self.name_entry.insert(0,"Name")
        self.name_entry.place(x=100, y=80, width=200)

        
        self.email_entry = Entry(self.root,bg="white", fg="BLack")
        self.email_entry.insert(0,"Email")
        self.email_entry.place(x=100, y=130, width=200)

        
        self.phone_entry = Entry(self.root,bg="white", fg="BLack")
        self.phone_entry.insert(0,"Phone-No")
        self.phone_entry.place(x=100, y=180, width=200)

        
        self.password_entry = Entry(self.root, show='*',bg="white", fg="BLack")
        self.password_entry.place(x=100, y=230, width=200)

        self.gender = Label(self.root, text="Gender", bg="white", fg="black", font=("arial",15))
        self.gender.place(x=50, y=280)
        self.genderr = StringVar()
        self.male =Radiobutton(self.root, text="Male", variable=self.genderr, value="Male", bg="white", fg="black")
        self.male.place(x=150, y=280)
        self.female = Radiobutton(self.root, text="Female", variable=self.genderr, value="Female", bg="white", fg="black")
        self.female.place(x=220, y=280)

        self.courses = ["BCA", "BTech", "BTech CSE","BTech CE", "MCA", "B Pharma", "D Pharma", "BBA", "MBA","BTTM", "BHMCT", "Other"]
        self.course_var = StringVar()
        self.course_var.set("Select Course")  # Set default value for the OptionMenu

        self.course_label = Label(self.root, text="Course", bg="white", fg="black", font=("Arial", 15))
        self.course_label.place(x=50, y=330)

        self.course_menu = OptionMenu(self.root, self.course_var, *self.courses)
        self.course_menu.config(bg="white", fg="black")
        self.course_menu.place(x=150, y=330, width=150)

        self.signup_button = Button(self.root, text="Sign Up", bg="cornflower blue", command=self.signup)
        self.signup_button.place(x=150, y=370, width=100, height=30)
    def signup(self):
        self.name =self.name_entry.get()
        self.password = self.password_entry.get()
        self.email = self.email_entry.get()
        self.phno = self.phone_entry.get()
        self.gender = self.genderr.get()
        self.course = self.course_var.get() 
        if not self.name or not self.email or not self.phno or not self.password:
            messagebox.showerror("Error", "please enter the credentials!")
            return
        
        else:
            messagebox.showinfo("Success", f"Sign-up Successful!\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phno}\nGender: {self.gender}\nCourse: {self.course}")
            with open('user.txt', 'a') as file1:
                file1.write(f"{self.name}, {self.password}, {self.email}, {self.phno}, {self.gender}, {self.course}")
                file1.write("\n")
            self.root.destroy()
            obj=login_form.login_page()
            obj.frame1()
            obj.root.mainloop()


if __name__ == "__main__":
    app = SignupPage()
    app.content()
    app.root.mainloop()