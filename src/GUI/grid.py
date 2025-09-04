import customtkinter as ctk


class Grid(ctk.CTk):
    def createGrid(self):
        self.geometry("1650x850")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)