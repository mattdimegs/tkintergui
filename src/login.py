import hashlib
from game import *
import main

db = main.db

mycursor = db.cursor()

user_info = []


class Gui:

    def verified_login(self):
        if self.loginVerified == "y":
            self.lScreen.destroy()
            self.main.destroy()
            gamePage = Game()

    def register_verify(self):
        uVerify = self.username_register.get()
        pVerify = self.password_register.get()
        vpVerify = self.vpassword_register.get()

        if uVerify != '':
            userTest = "select * from profiles where username = '%s';" % uVerify
            information_queue = []

            mycursor.execute(userTest)
            myresults = mycursor.fetchall()

            # Brings the info from the SQL Query and puts it into a List.
            for row in myresults:
                for x in row:
                    information_queue.append(x)

            # Make sure the Username is unique so it doesn't wipe old data, create the user if the password is the same.
            if uVerify not in information_queue:
                if pVerify and vpVerify != '':
                    if pVerify == vpVerify:
                        ppassword = vpVerify.encode()
                        encoded = hashlib.shake_128(ppassword).hexdigest(64)

                        userPassInsert = "insert into profiles" \
                                         "(username, password, points, level) " \
                                         "values" \
                                         "('%s', '%s', 0, 0);" % (uVerify, encoded)

                        mycursor.execute(userPassInsert)
                        db.commit()  # Commits new data to database, or else it won't save.
                        Label(self.main, text="Registration Success, please continue to Login.", fg="green").pack()
                        self.rScreen.destroy()

                    else:
                        Label(self.rScreen, text="The passwords entered do not match.", fg="red").pack()
                else:
                    Label(self.rScreen, text="The password fields must not be empty.", fg="red").pack()
            else:
                Label(self.rScreen, text="The username is already in use, please try again.", fg="orange").pack()
        else:
            Label(self.rScreen, text="The username field must not be empty.", fg="red").pack()

    def login_verify(self):
        uVerify = self.username_login.get()  # uVerify = Username Verification
        pVerify = self.password_login.get()  # pVerify = Password Verification

        # Encrypts the password before searching the database to compare.

        pVerify = pVerify.encode()
        encoded = hashlib.shake_128(pVerify).hexdigest(64)
        self.mypassword_queue = []

        # SQL to compare the codes later in the if statement.
        userPassCheck = "select * from profiles where username = '%s' and password = '%s'" % (uVerify, encoded)

        if uVerify and pVerify != '':
            mycursor.execute(userPassCheck)
            myresults = mycursor.fetchall()
            for row in myresults:
                for x in row:
                    self.mypassword_queue.append(x)
        else:
            print('Error Occurred')

        self.loginVerified = ""

        if (uVerify and encoded) in self.mypassword_queue:
            self.loginVerified = "y"
            self.lButton.destroy()
            Label(self.lScreen, text="Successful Login, your player id is {}.".format(self.mypassword_queue[0]),
                  fg="green").pack()
            for i in self.mypassword_queue:
                if i is not self.mypassword_queue[2]:
                    user_info.append(i)
            Button(self.lScreen, text="Play!", width="30", height="2", command=self.verified_login).pack()
        else:
            self.lError()
            self.plEntry.delete(0, END)

    def lError(self):
        self.leScreen = Toplevel(self.main)
        self.leScreen.title("Login Error")
        self.leScreen.geometry("300x50")
        Label(self.leScreen, text="Unsuccessful Login, Please Try Again.", fg="red").pack()
        Button(self.leScreen, text="Close", width="10", height="1", command=self.leScreen.destroy).pack()

    def register(self):
        self.rScreen = Toplevel(self.main)
        self.rScreen.title("Register")
        self.rScreen.geometry("300x250")
        Label(self.rScreen, text="Please create your Username and Password:").pack()
        Label(self.rScreen, text="").pack()

        self.username_register = StringVar()
        self.password_register = StringVar()
        self.vpassword_register = StringVar()

        Label(self.rScreen, text="Username:").pack()
        # urEntry = Username Register Entry
        self.urEntry = Entry(self.rScreen, textvariable=self.username_register)
        self.urEntry.pack()
        Label(self.rScreen, text="Password:").pack()
        # prEntry = Password Register Entry
        self.prEntry = Entry(self.rScreen, textvariable=self.password_register, show='*')
        self.prEntry.pack()
        Label(self.rScreen, text="Verify Password:").pack()
        # vprEntry = Verify Password Register Entry
        self.vprEntry = Entry(self.rScreen, textvariable=self.vpassword_register, show='*')
        self.vprEntry.pack()
        Button(self.rScreen, text="Login", width="10", height="1", command=self.register_verify).pack()

    def login(self):
        self.lScreen = Toplevel(self.main)
        self.lScreen.title("Login")
        self.lScreen.geometry("300x250")
        Label(self.lScreen, text="Please enter your details below to Login:").pack()
        Label(self.lScreen, text="").pack()

        self.username_login = StringVar()
        self.password_login = StringVar()

        Label(self.lScreen, text="Username:").pack()
        self.ulEntry = Entry(self.lScreen, textvariable=self.username_login)  # ulEntry = Username Login Entry
        self.ulEntry.pack()
        Label(self.lScreen, text="Password:").pack()
        self.plEntry = Entry(self.lScreen, textvariable=self.password_login, show='*')  # plEntry = Password Login Entry
        self.plEntry.pack()
        self.lButton = Button(self.lScreen, text="Login", width="10", height="1", command=self.login_verify)
        self.lButton.pack()

    def mainScreen(self):
        self.main = Tk()
        self.main.geometry("300x250")
        self.main.title("DB Game Main Login/Registration")
        Label(text="Matt's Login/Game", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", width="30", height="2", command=self.login).pack()
        Label(text="").pack()
        Button(text="Register", width="30", height="2", command=self.register).pack()
        Label(text="").pack()

        self.loginVerified = "n"

        self.main.mainloop()

    def __init__(self):
        self.mainScreen()
        self.login()
        self.register()
        self.login_verify()
        self.register_verify()
        self.verified_login()
        self.lError()
