from tkinter import *
import login


class Game:

    def administrator(self):
        print("admin")

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
        administrator = Button(self.gameMain, text="Administrator Panel", width="30", height="2")
        if login.user_info[3] >= 0:
            player.pack()
            if login.user_info[3] >= 1:
                developer.pack()
                if login.user_info[3] == 2:
                    administrator.pack()

    def __init__(self):
        self.mainMenu()
        self.administrator()
        self.developer()
        self.player()
