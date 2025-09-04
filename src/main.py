import customtkinter
import customtkinter as ctk
import logging as l
import asyncio
from GUI.loader import loadGUI
from GUI import grid, loader, frames
from obs.testConnection import testConnection
from obs.toggleRecording import toggleRecording
from database import database
import sys
import os
import peewee


# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src.obs.testConnection import testConnection as tc
l.basicConfig(level=l.INFO)
# counter = 0
db = database


# class MyFrame(customtkinter.CTkFrame):
#     def __init__(self, master, label_text, **kwargs):
#         super().__init__(master, **kwargs)
#         self.label = customtkinter.CTkLabel(self, text=label_text)
#         self.label.grid(row=0, column=0)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        loadGUI(self)

        self.connectFrame2_checkBox = ctk.CTkCheckBox(self.inner, text="Toggle Recording", offvalue="off", onvalue="on",  command= lambda: self.toAsync(kwargs="toggle_rec"), bg_color="black")
        self.connectFrame2_checkBox.grid(row=0, column= 1, padx=10, pady=10)





        # NOTE: The method must take 'self' as an argument
        self.runCurrentSelectedButton = customtkinter.CTkButton(self.background, text="RUN", command=lambda: self.toAsync(kwargs="run_all_selected"))
        self.runCurrentSelectedButton.grid(row=3, padx=10, pady=10, sticky="e")


        entry = database.State.get()
        if entry.record == False:
            checkbox_var = customtkinter.StringVar(value="off") 
            self.connectFrame2_checkBox.configure(variable=checkbox_var)
            return
        
        elif entry.record == True:
            checkbox_var = customtkinter.StringVar(value="on") 
            self.connectFrame2_checkBox.configure(variable=checkbox_var)
            return




    async def obsConnect(self):
        # NOTE: Retrieve the value here when the button is clicked
        host = self.host_entry.get()
        port = self.port_entry.get()
        passw = self.password_entry.get()
        l.info(f"Password entry values: {host}, {port}, {passw}")
        self.button.configure(state="disabled", text="Connecting...")
        test_result, message = await testConnection(host, port, passw)

        l.info(f"Test Result during conn: {test_result}")

        if test_result: 
            self.button.configure(state="enabled", text="Verbunden")

        elif test_result == False: 
            self.button.configure(state="enabled", text="No entry")
        else: self.button.configure(state="enabled", text=f"Fehlgeschlagen: {message}")


        return test_result

    async def toggle_rec(self):
        host = self.host_entry.get()
        port = self.port_entry.get()
        passw = self.password_entry.get()
        l.info("before rec db")

        try: 
            entry = database.State.get()

            if entry.record == False:
                l.info("db is negativ")
                database.State.update(record=True).where(database.State.record == False).execute()
                l.info(f"updated entry is now {entry.record}")
                # await toggleRecording(host, port, passw)
                return
            
            elif entry.record == True:

                l.info("db is positiv")
                database.State.update(record=False).where(database.State.record == True).execute()
                l.info(f"updated entry is now {entry.record}")
                # await toggleRecording(host, port, passw)
                return
            
        except Exception as e: 
            l.info(f"Error druing toggle Rec db: {e}")



    async def execute():
        l.info("exec")

app = App()
app.title("cOBaS | OBS WebSocket 5.0 Manager")
app.mainloop()
