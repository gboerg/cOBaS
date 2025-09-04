import customtkinter as ctk
from .frames import Frame
import logging as l
class ButtonManager():

    def obsConnect(self):
        connectFrame, host, port, password = Frame.createObsFrame(self)


        l.info(f"connection: {connectFrame}")
        self.connectFrame = connectFrame
        self.obs_connect_button = ctk.CTkButton(self.connectFrame, text="Connect to OBS", command=lambda: bridge(kwargs="obs_connect"))
        self.obs_connect_button.grid(row=0, column=10, padx=10, pady=10, sticky="w")

    def runCurrentSelected(self):
        self.background = Frame.createBackground(self)
        self.runCurrentSelectedButton = ctk.CTkButton(self.background, text="RUN", command=lambda: self.toAsync(kwargs="run_all_selected"))
        self.runCurrentSelectedButton.grid(row=3, padx=10, pady=10, sticky="e")