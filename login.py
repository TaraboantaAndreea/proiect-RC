from tkinter import *
import os
from topic import Topics

class Login:
    def __init__(self):
        global root
        self.v = []
        self.root = Tk()
        self.root.title('Window')
        self.root.geometry('500x500')
        Label(text="").pack()
        Label(text="").pack()
        Label(text="").pack()
        Label(text="").pack()
        Label(text="").pack()
        Label(text="").pack()

        # buton inregistrare
        Button(text="Inregistrare", height="5", width="20", bg="black", fg="white", command=self.register).pack()

        # buton autentificare
        Button(text="Autentificare", height="5", width="20", bg="black", fg="white", command=self.login).pack()

        self.root.mainloop()

    def register(self):
        global username
        global password
        global username_entry
        global password_entry

        username = StringVar()
        password = StringVar()

        self.register_screen = Toplevel(self.root)
        self.register_screen.title("Inregistrare")
        self.register_screen.geometry("300x300")

        Label(self.register_screen, text="").pack()
        Label(self.register_screen, text="Campurile marcate cu * sunt obligatorii!").pack()
        Label(self.register_screen, text="").pack()

        username_lable = Label(self.register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(self.register_screen, textvariable=username)
        username_entry.pack()

        password_lable = Label(self.register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(self.register_screen, textvariable=password, show='*')
        password_entry.pack()

        Label(self.register_screen, text="").pack()

        # buton inregistrare
        Button(self.register_screen, text="Inregistrare", width=10, height=1, bg="black", fg="white", command=self.register_user).pack()

    def register_user(self):
        # get username and password
        username_info = username.get()
        password_info = password.get()

        file = open(username_info, "w")

        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(self.register_screen, text="Inregistrare realizata cu succes", fg="orange", font=("calibri", 11)).pack()

    def login(self):

        global username_verify
        global password_verify
        global username_login_entry
        global password_login_entry

        self.login_screen = Toplevel(self.root)
        self.login_screen.title("Autentificare")
        self.login_screen.geometry("300x250")
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Campurile marcate cu * sunt obligatorii!").pack()
        Label(self.login_screen, text="").pack()

        username_verify = StringVar()
        password_verify = StringVar()

        Label(self.login_screen, text="Username * ").pack()
        username_login_entry = Entry(self.login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password * ").pack()
        password_login_entry = Entry(self.login_screen, textvariable=password_verify, show='*')
        password_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Button(self.login_screen, text="Autentificare", bg="black", fg="white", width=10, height=1, command=self.login_verify).pack()

    #functie care verifica daca exista un utilizator cu numele si parola aferenta
    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                Label(self.login_screen, text="Autentificare realizata cu succes", fg="orange", font=("calibri", 11)).pack()
                self.login_screen.destroy()
                self.root.destroy()
                t = Topics()
            else:
                Label(self.login_screen, text="Parola incorecta", fg="red", font=("calibri", 11)).pack()
        else:
            Label(self.login_screen, text="Utilizator invalid", fg="red", font=("calibri", 11)).pack()

