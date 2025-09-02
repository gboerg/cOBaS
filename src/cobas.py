import customtkinter
import customtkinter as ctk
import logging as l
from obs.testConnection import testConnection

# from src.obs.testConnection import testConnection as tc

l.basicConfig(level=l.INFO)

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, label_text, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text=label_text)
        self.label.grid(row=0, column=0)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1650x850")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Erster Frame
        self.frame1 = MyFrame(master=self, label_text="cOBaS | OBS WebSocket 5.0 Manager", width=600, height=400, fg_color="purple")
        self.frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        


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
        self.host_entry = customtkinter.CTkEntry(master=self.sub_frame, placeholder_text="IP-Adress of Computer")
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

        # NOTE: The method must take 'self' as an argument
        self.button = customtkinter.CTkButton(self.sub_frame, text="Connect to OBS", command=self.button_callback)
        self.button.grid(row=0, column=10, padx=10, pady=10, sticky="w")



        # NOTE: The method must take 'self' as an argument
        self.button = customtkinter.CTkButton(self.frame2, text="RUN", command=self.button_callback)
        self.button.grid(row=3, padx=10, pady=10, sticky="e")

    def button_callback(self):
        print("button clicked")
        
        # NOTE: Retrieve the value here when the button is clicked
        host = self.host_entry.get()
        port = self.port_entry.get()
        passw = self.password_entry.get()
        l.info(f"Password entry values: {host}, {port}, {passw}")
        self.button.configure(state="disabled", text="Connecting...")
        test_result, message = testConnection(host, port, passw)

        l.info(f"Test Result during conn: {test_result}")

        if test_result: 
            self.button.configure(state="enabled", text="Verbunden")
        else: self.button.configure(state="enabled", text=f"Fehlgeschlagen: {message}")


app = App()
app.title("cOBaS")
app.mainloop()
