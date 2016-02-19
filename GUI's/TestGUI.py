from tkinter import Tk, Label, ttk
import csv


class LogInScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Log In Screen")
        usernamelabel = Label(master,text="User name:")
        usernamelabel.place(x=10,y=20)
        passwordlabel = Label(master,text="Password:")
        passwordlabel.place(x=10,y=40)
        '''Create List Of User Names '''
        usernames = []
        with open('../CSV/Username_Passwords.csv', 'r') as f:
            u_p_file = csv.reader(f)
            for row in u_p_file:
                u_name = row[0]
                usernames.append(u_name)

        usernameentry = ttk.Combobox(master)
        usernameentry['values'] = usernames
        usernameentry.place(x=80,y=20)


root = Tk()
root.geometry("300x300")
my_gui = LogInScreen(root)
root.mainloop()
