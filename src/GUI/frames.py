import customtkinter as ctk
from bridge import asAsync

# import main


class MyFrame(ctk.CTkFrame):
    def __init__(self, master, label_text, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text=label_text)
        self.label.grid(row=0, column=0)

bridge = asAsync.asAsync.toAsync

class Frame(ctk.CTk):
    def createFrame01(self):
        self.aside = MyFrame(master=self, label_text="", width=600, height=400, fg_color="purple")
        self.aside.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.logoContainer = ctk.CTkFrame(master=self.aside, fg_color="grey")
        self.logoContainer.grid(row=0, column=0, sticky="n")

        self.appname = ctk.CTkLabel(master=self.logoContainer, text="cOBaS\nOBS WebSocket 5.0\nManager",)
        self.appname.grid(row=0, column=0, padx=10, pady=10)

    def createBackground(self):
        self.background = ctk.CTkFrame(master=self, width=500, height=200, fg_color="black")
        self.background.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.background.grid_rowconfigure(0, weight=0)
        self.background.grid_rowconfigure(1, weight=1)
        self.background.grid_columnconfigure(0, weight=1)

    def createObsFrame(self):
        self.connectFrame = ctk.CTkFrame(master=self.background, fg_color="blue")
        self.connectFrame.grid(row=0, column=0, sticky="new")
        self.connectFrame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.host = ctk.CTkLabel(master=self.connectFrame, text="HOST:")
        self.host.grid(row=0, column=0, padx=10, pady=10)
        self.host_entry = ctk.CTkEntry(master=self.connectFrame, placeholder_text="IP-Adress of target PC")
        self.host_entry.grid(row=0, column=1, padx=10, pady=10)

        self.port = ctk.CTkLabel(master=self.connectFrame, text="WebSocket Port:")
        self.port.grid(row=0, column=2, padx=10, pady=10)
        self.port_entry = ctk.CTkEntry(master=self.connectFrame, placeholder_text="WebSocket Port")
        self.port_entry.grid(row=0, column=3, padx=10, pady=10)

        self.password = ctk.CTkLabel(master=self.connectFrame, text="WebSocket Password:")
        self.password.grid(row=0, column=4, padx=10, pady=10)
        self.password_entry = ctk.CTkEntry(master=self.connectFrame, placeholder_text="WebSocket Password", show="*") # NOTE: Added show="*" for password security
        self.password_entry.grid(row=0, column=5, padx=10, pady=10)


        # TODO: EXPORT BUTTONS LATER 
        self.obs_connect_button = ctk.CTkButton(self.connectFrame, text="Connect to OBS", command=lambda: bridge(kwargs="obs_connect"))
        self.obs_connect_button.grid(row=0, column=10, padx=10, pady=10, sticky="w")
    
    def createInnerFrame(self):
        self.inner = ctk.CTkFrame(master=self.background, fg_color="red")
        self.inner.grid(row=1, column=0, sticky="nsew")