from .frames import Frame

import customtkinter as ctk
import logging as l

class checkBoxManager():

    

    def createCheckBoxToggleRecord(self):
        l.info("test")
        self.inner = Frame.createInnerFrame(self)
        checkBox = self.connectFrame2_checkBox = ctk.CTkCheckBox(self.inner, text="Toggle Recording", offvalue="off", onvalue="on",  command= lambda: self.toAsync(kwargs="toggle_rec"), bg_color="black")
        checkBox_grid = self.connectFrame2_checkBox.grid(row=0, column= 1, padx=10, pady=10)

