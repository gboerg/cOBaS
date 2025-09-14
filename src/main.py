import customtkinter as ctk
from interaction.toggleDarkMode import toggleDarkMode
from interaction.defaultGUIButtons import connect, reset
from PIL import Image
from database.dataManager import insertKnownWebsocketsInGui, debubVals, insertAvailable
from functions.getGuiElement import getGuiElement
from config.IniManager import generateConfig
from events.onMouseEvent import onDrag, MouseMotion
import logging as l
import os
# from interaction.commandCenter import mainFrameDBCombare

from functions.sharedFunctions import reloadBuilderContent

l.basicConfig(level=l.INFO)
class App(ctk.CTk):


    def __init__(self):
        super().__init__()
        self.setup()
        self.settingsWheel()
        self.create_grid()
        insertKnownWebsocketsInGui()
        debubVals()
        insertAvailable()
        generateConfig()
        # self.after(5000, self.start_db_check)

    # def start_db_check(self):
    #     # Your timed function to compare GUI and database
    #     mainFrameDBCombare()

    #     # Schedule the next check
    #     self.after(5000, self.start_db_check) 
        
    def setup(self):  
        getGuiElement("root", self)
        self.title("cOBaS | OBS WebSocket 5.0 BLDR")
        # self.geometry("1450x725") 
        self.geometry("1650x825") 
        # self.resizable(False, False)


    def settingsWheel(self):
        self.settings_wheel_image = ctk.CTkImage(
            dark_image=Image.open("src/assets/images/settings.png"),
            size=(30, 30)
        )

    def create_grid(self):
        # Zeilengewichtung festlegen
        self.grid_rowconfigure(0, weight=0)  # NavBar
        self.grid_rowconfigure(1, weight=0)  # connect_obs_frame
        self.grid_rowconfigure(2, weight=1)  # content_frame - diese Zeile nimmt den verbleibenden Platz ein#1
        self.grid_rowconfigure(3, weight=0)  # footer_frame

        # Spaltengewichtung festlegen
        self.grid_columnconfigure(0, weight=0)  # Aside
        self.grid_columnconfigure(1, weight=1)  # Hauptinhalt

        self.navbar_frame()
        self.aside_frame()
        self.connect_obs_frame()
        self.content_frame()
        self.footer_frame()





    # In your App class (within main.py)
    def navbar_frame(self):
        self.navbar = ctk.CTkFrame(self)
        self.navbar.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="news")

        self.navbar.grid_rowconfigure(0, weight=0)

        # Make column 1 a "spacer" column to push content to the right
        self.navbar.grid_columnconfigure(0, weight=0)  # For the label on the far left
        self.navbar.grid_columnconfigure(1, weight=1)  # This column will expand
        self.navbar.grid_columnconfigure(2, weight=0)  # For the switch
        self.navbar.grid_columnconfigure(3, weight=0)  # For the button

        user = os.getlogin()

        # Left-aligned widget
        navbar_label = ctk.CTkLabel(self.navbar, text=f"Welcome: {user} :> Glad to see you again - What do you want to build today?", height=30)
        navbar_label.grid(row=0, column=0, sticky="w")

        # Right-aligned widgets (the switch and the button)
        navbar_switch_var = ctk.StringVar(value="on")
        navbar_switch = ctk.CTkSwitch(
            self.navbar, 
            text="DarkMode", 
            command=toggleDarkMode, 
            variable=navbar_switch_var, 
            onvalue="on", 
            offvalue="off"
        )
        navbar_switch.grid(row=0, column=2, padx=20, sticky="e")

        navbar_button = ctk.CTkButton(
            self.navbar,
            text="",
            hover_color="purple",
            image=self.settings_wheel_image,

        )
        navbar_button.grid(row=0, column=3, sticky="e")
        navbar_button.configure()



        # navbar_label.pack(padx= 10, pady=10)

    def aside_frame(self):
        self.aside = ctk.CTkFrame(self)
        getGuiElement("aside_frame", self.aside)
        # Aside füllt die Spalte 0 von Zeile 1 bis 3
        self.aside.grid(row=1, column=0, rowspan=3, padx=10, pady=10, sticky="ns")
        

        # Setzt ein internes Grid für den Aside-Frame, um den Inhalt zu platzieren
        self.aside.grid_rowconfigure(0, weight=0) # Zeile für Label
        self.aside.grid_rowconfigure(1, weight=0) # Zeile für ScrollableFrame
        self.aside.grid_rowconfigure(2, weight=0) # Zeile für ScrollableFrame
        self.aside.grid_rowconfigure(3, weight=1)
        self.aside.grid_rowconfigure(4, weight=0)
        self.aside.grid_rowconfigure(5, weight=0)
        self.aside.grid_columnconfigure(0, weight=1) # Spalte für den gesamten Inhalt

        # Inhalt des Aside-Frames
        aside_label = ctk.CTkLabel(self.aside, text="Elements and Functions:")
        aside_label.grid(row=0, column=0, padx=100, pady=20)

        search_bar = ctk.CTkEntry(self.aside, placeholder_text="SEARCH any FOR  .... ?")
        search_bar.grid(row= 1, column = 0)




        self.aside_content_web = ctk.CTkScrollableFrame(master=self.aside)
        self.aside_content_web.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        getGuiElement("websocket_scrollbox", self.aside_content_web)

  

        #NOTE: 
        obs = self.aside_content = ctk.CTkScrollableFrame(master=self.aside)
        
        obs_grid = self.aside_content.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        getGuiElement("obs_features", obs)
 

        # NOTE:  
        misc = self.aside_content2= ctk.CTkScrollableFrame(master=self.aside)
        misc_grid = self.aside_content2.grid(row=4, column= 0, padx=10, pady=10, sticky="news")
        getGuiElement("misc_features", misc)
        
        

    def connect_obs_frame(self):
        self.connect = ctk.CTkFrame(self)
        getGuiElement("connect_frame", self.connect)
        self.connect.grid(row=1, column=1, padx=10, pady=10, sticky="new")
        
        # Konfiguriere die Spalten, um die gewünschte Anordnung zu erreichen
        self.connect.grid_columnconfigure(0, weight=0) # WebSocket Label (links)
        self.connect.grid_columnconfigure(1, weight=1) # Spacer (drückt die Felder nach rechts)
        self.connect.grid_columnconfigure(2, weight=0) # Name
        self.connect.grid_columnconfigure(3, weight=0) # Host
        self.connect.grid_columnconfigure(4, weight=0) # Port
        self.connect.grid_columnconfigure(5, weight=0) # Password
        self.connect.grid_columnconfigure(6, weight=1) # Spacer (drückt den Button nach rechts)
        self.connect.grid_columnconfigure(7, weight=0) # Connect Button (rechts)

        # Konfiguriere die Reihen
        self.connect.grid_rowconfigure(0, weight=0)
        self.connect.grid_rowconfigure(1, weight=0)

        # 'WebSocket:' Label (ganz links, in Spalte 0)
        info_label = ctk.CTkLabel(self.connect, text="WebSocket:")
        info_label.grid(row=1, column=0, sticky="w", padx=(10, 0))

        # Name-Widgets (zentriert, in Spalte 2)
        name_label = ctk.CTkLabel(self.connect, text="Name",)
        name_label.grid(row=0, column=2, sticky="ew")


        name_entry = ctk.CTkEntry(self.connect, placeholder_text="obs record ...(optional)")
        name_entry.grid(row=1, column=2, sticky="ew", padx=(10, 10))
        getGuiElement("name_entry", name_entry)
        
        # Host-Widgets (zentriert, in Spalte 3)
        host_label = ctk.CTkLabel(self.connect, text="Host")
        host_label.grid(row=0, column=3, sticky="ew", padx=(10, 0))

        host_entry = ctk.CTkEntry(self.connect, placeholder_text="ip-address of target pc")
        host_entry.grid(row=1, column=3, sticky="ew", padx=10)
        getGuiElement("host_entry", host_entry)

        # Port-Widgets (zentriert, in Spalte 4)
        port_label = ctk.CTkLabel(self.connect, text="Port")
        port_label.grid(row=0, column=4, sticky="ew")

        port_entry = ctk.CTkEntry(self.connect, placeholder_text="port")
        port_entry.grid(row=1, column=4, sticky="ew", padx=10)
        getGuiElement("port_entry", port_entry)

        # Password-Widgets (zentriert, in Spalte 5)
        password_label = ctk.CTkLabel(self.connect, text="Password")
        password_label.grid(row=0, column=5, sticky="ew")

        

        password_entry = ctk.CTkEntry(self.connect, placeholder_text="password", show="*")
        password_entry.grid(row=1, column=5, sticky="ew", padx=(10, 10))
        getGuiElement("password_entry", password_entry)
        
        # Connect Button (ganz rechts, in Spalte 7)
        connect_button = ctk.CTkButton(self.connect, text="Connect", hover_color="purple", command= connect)
        getGuiElement("connect_button", connect_button)
        connect_button.grid(row=1, column=7, sticky="e", padx=(0, 0))
        


        

    def content_frame(self):
        #, scrollbar_button_color="purple"
        contentFrame = self.content = ctk.CTkFrame(self)
        contentFrameGrid =self.content.grid(row=2, column=1, padx= 10, pady=10, sticky= "news")

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=0)
        self.content.grid_columnconfigure(2, weight=0)
        self.content.grid_columnconfigure(3, weight=1)
        self.content.grid_columnconfigure(4, weight=0)
        
        self.content.grid_rowconfigure(0, weight=0)
        self.content.grid_rowconfigure(1, weight=1)
        self.content.grid_rowconfigure(3, weight=0)
        

        # content_label = ctk.CTkLabel(self.content, text= "Graphical Drag N' Drop Script Builder: [ORIENTATION GUIDE] Up -> Down or Left -> Right")
        content_label = ctk.CTkLabel(self.content, text= "Script Builder:")
        content_label.grid(row=0, column= 1)
        
        clear_Button = ctk.CTkButton(self.content, text="Clear Script", command=reset)
        clear_Button.grid(row=2, column=1, padx=(5, 5))
        
        # reload_builder_button = ctk.CTkButton(self.content, text="Reload / RESTORE", command=reloadBuilderContent)
        reload_builder_button = ctk.CTkButton(self.content, text="Reload / RESTORE", command=reloadBuilderContent)
        reload_builder_button.grid(row=0, column=4)

        mainFrame = self.contentScroll = ctk.CTkScrollableFrame(self.content)
        mainFrameGrid = self.contentScroll.grid(row=1, column=0, columnspan=6, rowspan= 1, padx=10, pady=10, sticky="news")

        # MouseMotion(conntentFrame)
        contentFrame.bind("<Enter>", MouseMotion)
        contentFrame.bind("<Leave>", MouseMotion)
    

        getGuiElement("main_frame", mainFrame)
        getGuiElement("content_frame", contentFrame)
        getGuiElement("reload_button", reload_builder_button)

        




    def footer_frame(self):
        self.footer = ctk.CTkFrame(self)
        self.footer.grid(row=3, column=1, padx= 10, pady=10, sticky= "news")

        self.footer.grid_rowconfigure(1, weight=0)
        self.footer.grid_columnconfigure(0, weight=0)
        self.footer.grid_columnconfigure(1, weight=1)
        self.footer.grid_columnconfigure(2, weight=0)
        self.footer.grid_columnconfigure(3, weight=0)



        footer_label = ctk.CTkLabel(self.footer, text="Made by Jan Gerstenberg @gboergIndustries with LOVE", )
        footer_label.grid(row= 1, column =1, sticky="w")
        # footer_label.pack(padx =20, pady= 20)

        run_button = ctk.CTkButton(self.footer, text="RUN", hover_color="purple")
        run_button.grid(row=1, column=2, sticky="e", padx="5")

        export_button = ctk.CTkButton(self.footer, text="EXPORT", hover_color="purple")
        export_button.grid(row=1, column=3, sticky="e")






app = App()
app.mainloop()