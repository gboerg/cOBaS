import customtkinter
import customtkinter as ctk
import logging as l
import asyncio
from GUI.loader import loadGUI
from GUI import grid, loader, frames
from obs.testConnection import testConnection
from obs.toggleRecording import toggleRecording
from database import database, restoreLast
import sys
import os
import peewee



# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src.obs.testConnection import testConnection as tc
l.basicConfig(level=l.INFO)
# counter = 0
db = database

res = restoreLast
# class MyFrame(customtkinter.CTkFrame):
#     def __init__(self, master, label_text, **kwargs):
#         super().__init__(master, **kwargs)
#         self.label = customtkinter.CTkLabel(self, text=label_text)
#         self.label.grid(row=0, column=0)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        loadGUI(self)
        self.after(100, lambda: asyncio.create_task(self.restoreVals()))

    async def restoreVals():
        l.info("RESOTE ")
        await res.restore.checkPreviousValues()



app = App()
app.title("cOBaS | OBS WebSocket 5.0 Manager")
app.mainloop()

