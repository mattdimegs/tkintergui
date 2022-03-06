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
        Button(self.pEdit, text="Edit a user", width="30", height="2").pack()

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
