from tkinter import *
import login


class Game:

    def remove(self):
        print("")

    def add(self):
        print("")

    def edit(self):
        self.pEdit = Toplevel(self.gameMain)  # pEdit = Player Edit
        self.pEdit.title("Administration: Edit Player")
        self.pEdit.geometry("300x250")
        self.aScreen.destroy()
        Label(self.pEdit, text="Edit Player", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
        Label(self.pEdit, text="").pack()

        self.pIDEntry = StringVar()

        Label(self.pEdit, text="User's ID:").pack()
        # pID = Player ID that is trying to be edited.
        self.pID = Entry(self.pEdit, textvariable=self.pIDEntry)
        self.pID.pack()
        Button(self.pEdit, text="Search", width="10", height="1", command=self.edit_id_search).pack()

    def edit_id_search(self):
        pIDVerify = self.pIDEntry.get()
        if pIDVerify != '':
            userTest = "select id, username, points, level from profiles where id = '%s';" % pIDVerify
            self.information_queue = []

            login.mycursor.execute(userTest)
            myresults = login.mycursor.fetchall()

            for row in myresults:
                for x in row:
                    self.information_queue.append(x)

            if self.information_queue[1] != '':
                if self.information_queue[3] < login.user_info[3]:
                    print("good")
                else:
                    self.sError()
                    self.pID.delete(0, END)
            else:
                self.sError()
                self.pID.delete(0, END)
        else:
            self.sError()
            self.pID.delete(0, END)

    def administrator(self):
        self.aScreen = Toplevel(self.gameMain)
        self.aScreen.title("Administrator Panel")
        self.aScreen.geometry("300x250")
        Label(self.aScreen, text="Welcome to the Administration Panel", bg="grey", width="300", height="2",
              font=("Calibri", 13)).pack()
        Label(self.aScreen, text="").pack()
        Button(self.aScreen, text="Edit a user", width="30", height="2", command=self.edit).pack()
        Label(self.aScreen, text="").pack()
        Button(self.aScreen, text="Add a user", width="30", height="2", command=self.add).pack()
        Label(self.aScreen, text="").pack()
        Button(self.aScreen, text="Remove a user", width="30", height="2", command=self.remove).pack()

    def developer(self):
        print("developer")

    def player(self):
        print("player")

    def sError(self):
        self.seScreen = Toplevel(self.gameMain)
        self.seScreen.title("Player Search Error")
        self.seScreen.geometry("300x50")
        Label(self.seScreen, text="Unsuccessful Player Search, Please Try Again.", fg="red").pack()
        information_queue = []
        Button(self.seScreen, text="Close", width="10", height="1", command=self.seScreen.destroy).pack()

    def mainMenu(self):
        self.gameMain = Tk()
        self.gameMain.geometry("300x250")
        self.gameMain.title("DB Game Main Menu")
        Label(self.gameMain, text="Matt's Game Main Menu", bg="grey", width="300", height="2",
              font=("Calibri", 13)).pack()
        player = Button(self.gameMain, text="Play", width="30", height="2")
        developer = Button(self.gameMain, text="Developer Panel", width="30", height="2")
        administrator = Button(self.gameMain, text="Administrator Panel", width="30", height="2",
                               command=self.administrator)
        # login.user_info is [ID, Username, Points, Level]
        if login.user_info[3] >= 0:
            player.pack()
            if login.user_info[3] >= 1:
                developer.pack()
                if login.user_info[3] == 2:
                    administrator.pack()

        self.gameMain.mainloop()

    def __init__(self):
        self.mainMenu()
        self.administrator()
        self.developer()
        self.player()
        self.edit()
        self.add()
        self.remove()
