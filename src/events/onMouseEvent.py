import customtkinter as ctk
from tkinter import Event
from functions.getGuiElement import getGuiElement
import logging as l
from database.database import Builder,websockets
import tkinter as tk




class confirmActionWindow(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        window = self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)
        


def onMouseRightClick(event: ctk.CTkBaseClass):
    l.info("CLICK")
    event
    widget = event.widget
    text = widget.cget("text")
    # confirmActionWindow().attributes("-topmost", True)
    # confirmActionWindow().transient()
    dbOverwrite = [
        Builder.delete().where(Builder.name.contains(text)),
        websockets.delete().where(websockets.all_field.contains(text))
    ]
    
    for overwrite in dbOverwrite:
        overwrite.execute()
    
    event.widget.master.destroy()