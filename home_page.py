from tkinter import *
from tkinter import messagebox
import registeration  # Import your registration module

class Home_page:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600+300+100")
        self.root.title("Home Page")

        # Load the PCTE logo image
        try:
            self.logo = PhotoImage(file='pctelogo.png')  # Ensure you have a file named 'pctelogo.png'
            self.bg_label = Label(self.root, image=self.logo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            messagebox.showerror("Error", "Could not load background image. Please check the file path.")
            print(e)

        self.frame2()

    def frame2(self):
        # Create a frame to hold the user information
        frame = Frame(self.root, bg="white", bd=5)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=700, height=500)

        # Label to display the college name
        college_label = Label(frame, text="PCTE College of Technology", bg="black", font=("Arial", 24, 'bold'))
        college_label.pack(pady=10)

        # Label to display the title
        title_label = Label(frame, text="Registered Students", bg="black", font=("Arial", 18))
        title_label.pack(pady=5)

        # Listbox to display registered user data
        self.user_listbox = Listbox(frame, bg="black", font=("Arial", 12), width=100)
        self.user_listbox.pack(padx=10, pady=10)

        # Button to add new data
        add_button = Button(frame, text="Add New Data", command=self.open_registration_page, bg="lightblue")
        add_button.pack(pady=10)

        # Load user data from the file
        self.load_user_data()

    def load_user_data(self):
        try:
            with open('user.txt', 'r') as file:
                data = file.readlines()
                for index, user in enumerate(data, start=1):  # Start enumeration at 1
                    user_info = user.strip().split(", ")
                    self.user_listbox.insert(END, 
                        f"{index}. Name: {user_info[0]},Phone-NO: {user_info[1]}, Email: {user_info[2]}, Phone: {user_info[3]}, Gender: {user_info[4]}, Course: {user_info[5]}" )
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def open_registration_page(self):
        # Close the current window
        self.root.destroy()
        # Create a new instance of the registration page
        registration_app = registeration.SignupPage()  # Update if your registration class name is different
        registration_app.content()
        registration_app.root.mainloop()

if __name__ == "__main__":
    app = Home_page()
    app.root.mainloop()