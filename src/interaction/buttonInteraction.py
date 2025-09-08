
import logging as l
from functions.getGuiElement import getGuiElement

from database.database import websockets
import time

import customtkinter as ctk




def recording_checkbox():
    l.warning("Record Function ticked")

def connect():
    l.warning("connect function triggered")
    guiElement = getGuiElement("connect_button")
    l.warning(f" guiElement: {guiElement}")
    if guiElement:
        
        hostElement = getGuiElement("host_entry")
        portElement = getGuiElement("port_entry")
        passElement = getGuiElement("password_entry")
        if not hostElement or not portElement or not passElement:
            l.warning("Existiert in Gui NICHT ")
            return
        else: 
            host = hostElement.get()
            port = portElement.get()
            passw = passElement.get()

            if not host or not port or not passw:
                guiElement.configure(text= "ENTER VALUES")
                guiElement.after(5000, lambda: guiElement.configure(text="Connect"))

                return
            else:
                guiElement.configure(text= "Connected")
                l.warning(f"Host: {host}, Port: {port}, Password: {passw}")
                l.warning("Button konfiguriert.")
                scrollbox = getGuiElement("websocket_scrollbox")
                if not scrollbox or scrollbox is None:
                    return
                
                ## NOTE: DATABASE ENTRY:
                # websockets.create(id=0, host= host, port= port, password = passw)

                ## NOTE: LABEL INJECTION:
                # label = ctk.CTkLabel(master=scrollbox, text=f"OBS: {host}")
                # label.pack()



    else: 
        l.error("No Element ")

def add_connect():
    l.warning("connect function triggered")
    guiElement = getGuiElement("save_connect_button")
    l.warning(f" guiElement: {guiElement}")
    if guiElement:
        guiElement.configure(text="Hinzugefügt")
        l.warning("Button konfiguriert.")
    else: 
        l.error("No Element ")