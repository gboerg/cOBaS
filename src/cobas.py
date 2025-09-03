import customtkinter
import customtkinter as ctk
import logging as l
import asyncio
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

# cursor = database.cursor
# conn = database.conn
# def on_interaction():
#     global counter
#     counter += 1

#     if counter == 0:
#         return False
#     elif counter == 1:
#         return True
#     elif counter == 2:
#         counter = 0
#         return False

# def get_interaction():
#     l.info(f"Current counter level  {counter}")
#     return counter

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, label_text, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = customtkinter.CTkLabel(self, text=label_text)
        self.label.grid(row=0, column=0)


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS state (
        #         id INTEGER PRIMARY KEY,
        #         record BOOL DEFAULT 0 NOT NULL,
        #         stream BOOL DEFAULT 0 NOT NULL
        #     )
        # """)

        # conn.commit()
        self.geometry("1650x850")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Erster Frame
        self.frame1 = MyFrame(master=self, label_text="", width=600, height=400, fg_color="purple")
        self.frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame1_subframe = ctk.CTkFrame(master=self.frame1, fg_color="grey")
        self.frame1_subframe.grid(row=0, column=0, sticky="n")
        self.appname = ctk.CTkLabel(master=self.frame1_subframe, text="cOBaS\nOBS WebSocket 5.0\nManager",)
        self.appname.grid(row=0, column=0, padx=10, pady=10)
        


        # Zweiter Frame, der als Container dient
        self.frame2 = customtkinter.CTkFrame(master=self, width=500, height=200, fg_color="green")
        self.frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Konfiguriere das Grid im zweiten Frame
        # NOTE: We now use two rows to avoid overlapping frames
        self.frame2.grid_rowconfigure(0, weight=0)
        self.frame2.grid_rowconfigure(1, weight=1)
        self.frame2.grid_columnconfigure(0, weight=1)

        # Ein weiterer Frame, der in frame2 eingefügt wird
        self.sub_frame = customtkinter.CTkFrame(master=self.frame2, fg_color="blue")
        # NOTE: Place this frame in row 0
        self.sub_frame.grid(row=0, column=0, sticky="new")
        
        # Configure the sub_frame to allow content to expand within it
        self.sub_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.host = customtkinter.CTkLabel(master=self.sub_frame, text="HOST:")
        self.host.grid(row=0, column=0, padx=10, pady=10)
        self.host_entry = customtkinter.CTkEntry(master=self.sub_frame, placeholder_text="IP-Adress of target PC")
        self.host_entry.grid(row=0, column=1, padx=10, pady=10)

        self.port = customtkinter.CTkLabel(master=self.sub_frame, text="WebSocket Port:")
        self.port.grid(row=0, column=2, padx=10, pady=10)
        self.port_entry = customtkinter.CTkEntry(master=self.sub_frame, placeholder_text="WebSocket Port")
        self.port_entry.grid(row=0, column=3, padx=10, pady=10)

        self.password = customtkinter.CTkLabel(master=self.sub_frame, text="WebSocket Password:")
        self.password.grid(row=0, column=4, padx=10, pady=10)
        self.password_entry = customtkinter.CTkEntry(master=self.sub_frame, placeholder_text="WebSocket Password", show="*") # NOTE: Added show="*" for password security
        self.password_entry.grid(row=0, column=5, padx=10, pady=10)
        
        # NOTE: This line is removed, the value is retrieved in the callback
        # pe = self.password_entry.get()

        # Place sub_frame2 in row 1
        self.sub_frame2 = customtkinter.CTkFrame(master=self.frame2, fg_color="red")
        self.sub_frame2.grid(row=1, column=0, sticky="nsew")

        self.sub_frame2_button1 = ctk.CTkCheckBox(self.sub_frame2, text="Toggle Recording", command= lambda: self.toAsync(kwargs="toggle_rec"), bg_color="black")
        self.sub_frame2_button1.grid(row=0, column= 1, padx=10, pady=10)


        # NOTE: The method must take 'self' as an argument
        self.button = customtkinter.CTkButton(self.sub_frame, text="Connect to OBS", command=lambda: self.toAsync(kwargs="obs_connect"))
        self.button.grid(row=0, column=10, padx=10, pady=10, sticky="w")



        # NOTE: The method must take 'self' as an argument
        self.button2 = customtkinter.CTkButton(self.frame2, text="RUN", command=lambda: self.toAsync(kwargs="run_all_selected"))
        self.button2.grid(row=3, padx=10, pady=10, sticky="e")


    def toAsync(self, kwargs):
        if kwargs == "run_all_selected":
            l.info("run current selected")

        if kwargs == ("obs_connect"):
            l.info("Obs Connect Button")
            asyncio.run(self.obsConnect())

        if kwargs == "toggle_rec":
            asyncio.run(self.toggle_rec())
            l.info("toggle_rec")

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
app.title("cOBaS")
app.mainloop()
