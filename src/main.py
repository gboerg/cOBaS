import customtkinter as ctk
from interaction.toggleDarkMode import toggleDarkMode
from interaction.buttonInteraction import recording_checkbox, connect, add_connect
from PIL import Image
from database.restoreManager import insertKnownWebsocketsInGui, debubVals, insertAvailable
from functions.getGuiElement import getGuiElement
import database.database
from events.onMouseEvent import onDrag
import logging as l





# class PhotoClass(ctk.CTkImage):
#     def __init__(self, light_image = None, dark_image = None, size = ...):
#         super().__init__(light_image, dark_image, size)


#         def settingsWheel(self):
#             settings_wheel = ctk.CTkImage(dark_image=Image.open("assets/images/settings.png"), size=(30, 30))


class App(ctk.CTk):



    def __init__(self):
        super().__init__()
        self.setup()
        self.settingsWheel()
        self.create_grid()
        insertKnownWebsocketsInGui()
        debubVals()
        insertAvailable()
        



    def setup(self):
        self.title("cOBaS | OBS WebSocket 5.0 CMDR")
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

        # Left-aligned widget
        navbar_label = ctk.CTkLabel(self.navbar, text="cOBaS | OBS WebSocket 5.0 Commander", text_color="purple")
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



        # navbar_label.pack(padx= 10, pady=10)

    def aside_frame(self):
        self.aside = ctk.CTkFrame(self)
        # Aside füllt die Spalte 0 von Zeile 1 bis 3
        self.aside.grid(row=1, column=0, rowspan=3, padx=10, pady=10, sticky="ns")
        

        # Setzt ein internes Grid für den Aside-Frame, um den Inhalt zu platzieren
        self.aside.grid_rowconfigure(0, weight=0) # Zeile für Label
        self.aside.grid_rowconfigure(1, weight=0) # Zeile für ScrollableFrame
        self.aside.grid_rowconfigure(2, weight=0) # Zeile für ScrollableFrame
        self.aside.grid_rowconfigure(3, weight=1)
        self.aside.grid_rowconfigure(4, weight=0)

        self.aside.grid_columnconfigure(0, weight=1) # Spalte für den gesamten Inhalt

        # Inhalt des Aside-Frames
        aside_label = ctk.CTkLabel(self.aside, text="Functions:")
        aside_label.grid(row=0, column=0, padx=100, pady=20)

        search_bar = ctk.CTkEntry(self.aside, placeholder_text="SEARCH FOR  .... ?")
        search_bar.grid(row= 1, column = 0)




        self.aside_content_web = ctk.CTkScrollableFrame(master=self.aside)
        self.aside_content_web.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        getGuiElement("websocket_scrollbox", self.aside_content_web)

        # example_web_socket_connect = ctk.CTkButton(self.aside_content_web, text="OBS REC [192.162.172.4 | 4455]")
        # example_web_socket_connect.grid(row=1, column=1)
 


        #NOTE: 
        obs = self.aside_content = ctk.CTkScrollableFrame(master=self.aside)
        children = obs.children
        
        obs_grid = self.aside_content.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        getGuiElement("obs_features", obs)
        l.info(f"children: {children}")


        # Beispiel-Inhalt für das ScrollableFrame
        # toggle_record = ctk.CTkButton(self.aside_content, text="Toggle Recording", command=recording_checkbox)
        # toggle_record.grid(row=1, column=1)



        # NOTE:  
        misc = self.aside_content2= ctk.CTkScrollableFrame(master=self.aside)
        misc_grid = self.aside_content2.grid(row=4, column= 0, padx=10, pady=10, sticky="news")
        getGuiElement("misc_features", misc)
        # test = ctk.CTkButton(self.aside_content2, text="addDelay(delay ms)")
        # test.grid(row=1, column=1)
        
        # for i in range(20):
        #     ctk.CTkCheckBox(self.aside_content, text=f"Item {i+1}").pack(pady=5, padx=5)

    def connect_obs_frame(self):
        self.connect = ctk.CTkFrame(self)
        self.connect.grid(row=1, column=1, padx=10, pady=10, sticky="new")
        
        # Configure the columns for alignment
        self.connect.grid_columnconfigure(0, weight=0)  # For the "WebSocket:" label
        self.connect.grid_columnconfigure(1, weight=1)  # Left spacer for centering
        self.connect.grid_columnconfigure(2, weight=0)  # For host widgets
        self.connect.grid_columnconfigure(3, weight=0)  # For port widgets
        self.connect.grid_columnconfigure(4, weight=0)  # For password widgets
        self.connect.grid_columnconfigure(5, weight=1)  # Right spacer for centering
        self.connect.grid_columnconfigure(6, weight=0)
        self.connect.grid_columnconfigure(7, weight=0)  # For Connect button
        self.connect.grid_columnconfigure(8, weight=0)  # For Previous button
        
        # Configure the rows for the labels and entries
        self.connect.grid_rowconfigure(0, weight=0)
        self.connect.grid_rowconfigure(1, weight=0)

        # Left-aligned "WebSocket:" label
        info_label = ctk.CTkLabel(self.connect, text="WebSocket:")
        info_label.grid(row=1, column=0, sticky="w", padx=(10, 0))


        # Center-aligned widgets
        host_label = ctk.CTkLabel(self.connect, text="Host")
        host_label.grid(row=0, column=2, sticky="ew", padx=(10, 0))

        host_entry = ctk.CTkEntry(self.connect, placeholder_text="ip-address of target pc")
        host_entry.grid(row=1, column=2, sticky="ew", padx=10)
        getGuiElement("host_entry", host_entry)

        port_label = ctk.CTkLabel(self.connect, text="Port")
        port_label.grid(row=0, column=3, sticky="ew")

        port_entry = ctk.CTkEntry(self.connect, placeholder_text="port")
        port_entry.grid(row=1, column=3, sticky="ew", padx=10)
        getGuiElement("port_entry", port_entry)

        password_label = ctk.CTkLabel(self.connect, text="Password")
        password_label.grid(row=0, column=4, sticky="ew")

        password_entry = ctk.CTkEntry(self.connect, placeholder_text="password", show="*")
        password_entry.grid(row=1, column=4, sticky="ew", padx=(10, 10))
        getGuiElement("password_entry", password_entry)

        # Right-aligned buttons

        # save_connect_button = ctk.CTkButton(self.connect, text="Add", hover_color="purple", command= add_connect)
        # getGuiElement("save_connect_button", save_connect_button)
        # save_connect_button.grid(row=1, column=6, sticky="e", padx=(5, 5))
        connect_button = ctk.CTkButton(self.connect, text="Connect", hover_color="purple", command= connect)
        getGuiElement("connect_button", connect_button)
        connect_button.grid(row=1, column=7, sticky="e", padx=(0, 0))

        # load_connect_button = ctk.CTkButton(self.connect, text="load", hover_color="purple")
        # load_connect_button.grid(row=1, column=8, sticky="e")



        

    def content_frame(self):
        #, scrollbar_button_color="purple"
        self.content = ctk.CTkFrame(self)
        self.content.grid(row=2, column=1, padx= 10, pady=10, sticky= "news")

        self.content.grid_columnconfigure(0, weight=0)
        self.content.grid_rowconfigure(0, weight=0)
        
        self.content.grid_columnconfigure(1, weight=1)
        self.content.grid_rowconfigure(1, weight=1)

        content_label = ctk.CTkLabel(self.content, text= "CONFIG OF SELECTED SCRIPTS", )
        content_label.grid(row=0, column= 0)

        mainFrame = self.contentScroll = ctk.CTkScrollableFrame(self.content, scrollbar_button_color="purple")
        self.contentScroll.grid(row=1, column=0, columnspan=2, rowspan= 1, padx=10, pady=10, sticky="news")
        getGuiElement("main_frame", mainFrame)
        









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