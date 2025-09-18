
import logging as l
from functions.getGuiElement import getGuiElement
from database.dataManager import insertKnownWebsocketsInGui
import peewee
import re
import time
import random
import matplotlib.colors as mcolors
from matplotlib_colors import colormap_names
import customtkinter as ctk
from obs.testConnection import testObsWebSocketConnection


from database.database import websockets, Features, Builder

import colorsys
import datetime
    
def reset():
    guiElement = getGuiElement("main_frame")
    elements = guiElement.winfo_children()
    for each in elements:
        each.destroy()
    if elements:
        Builder.drop_table()
        Builder.create_table()
        l.info("mainframe cleared")
    else:
        l.info("Nothing to clear")
        Builder.drop_table()
        Builder.create_table()

def clearWindow():
    from interaction.commandCenter import destroyMainFrame
    destroyMainFrame()


def recording_checkbox():
    l.warning("Record Function ticked")
    
    
    

def connect():
    l.warning("connect function triggered")
    guiElement = getGuiElement("connect_button")
    if not guiElement:
        l.error("No Element")
        return

    nameElement = getGuiElement("name_entry")
    hostElement = getGuiElement("host_entry")
    portElement = getGuiElement("port_entry")
    passElement = getGuiElement("password_entry")

    if not hostElement or not portElement or not passElement:
        return
    else: 
        # name_str = nameElement.get() if nameElement else ""
        name = nameElement.get()
        host = hostElement.get()
        port = portElement.get()
        passw = passElement.get()
        
        connectionDict = {}
        connectionDict["websocket"] = {
            "host": host,
            "port": port,
            "passw": passw
        }
        
        if not name or None:
            result = websockets.select().count()
            l.warn(f"RESULT OF WEBSICJT: {result}")
            if not result:
                result = 1 
            elif result:
                result +=1
            name=f"Con: {result}"
        
        # Leere Strings behandeln
        # name = name_str if name_str else None
        
        
        if not all((host, port, passw)):
            guiElement.configure(text="WebSocket Connection is required")
            guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
            return

        # if not host or not port or not passw:
        if not host:
            guiElement.configure(text="ENTER Host")
            guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
            return
        elif not port:
            guiElement.configure(text="ENTER Port")
            guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
            return
        elif not passw:
            guiElement.configure(text="ENTER Password")
            guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
            return
        else:
            try:
                port_int = int(port)
                red_bg= "white"
                red_text = "black"
                
                
                version = testObsWebSocketConnection(host=host, port=port, password=passw) 
                
                l.info(f"OBS VERSION CONN REQ: {version}")
                
                # Check for the specific failure string
                if version == "No Response from OBS":
                    # Change the button text
                    guiElement.configure(text=version) 
                    return
                
                if "OBS" in version:
                    all_field_string = f'WebSocket: {name} | Host: {host} | Port: {port}'
                    #TODO: Same websocket Dectection
                    result = websockets.select().where(websockets.all_field == all_field_string)
                    result2 = websockets.select().where((websockets.port == port) & (websockets.password == passw) & (websockets.host == host))
                    l.info(f"WEBSOCKET DB CHECK2 {result2}")
                    # if not all([result, result2]):
                    if not result and not result2:
                        # Verwende get_or_create, um das Objekt zu finden oder zu erstellen
                        entry, created = websockets.get_or_create(
                            host=host, 
                            port=port_int, 
                            name= name,
                            all_field= all_field_string,
                            defaults={'name':name,'password':passw},
                            color = red_bg,
                            text_color= red_text
                            
                        )
                        if created:
                            l.info("Neuer Eintrag in der Datenbank erstellt.")
                            insertKnownWebsocketsInGui()
                            guiElement.configure(text="Connected")
                        elif not created:
                            pass
                    else:
                        l.info("same websocket is not allowed")
                        l.warning("Eintrag existiert bereits. Kein neuer Eintrag in DB oder GUI.")
                        guiElement.configure(text="Already Exists")
                        guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
                elif not "OBS" in version: 
                    guiElement.configure(text="NO RESPONSE FROM OBS")
                    guiElement.after(5000, lambda: guiElement.configure(text="Connect"))

            except ValueError:
                l.error("Fehler: Port-Wert ist keine gültige Zahl.")
                guiElement.configure(text="Invalid Port")
                guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
            except peewee.IntegrityError:
                l.error("Fehler: Datenbank-Integritätsverletzung.")
                guiElement.configure(text="DB Error")
                guiElement.after(5000, lambda: guiElement.configure(text="Connect"))






# def add_connect():
#     # l.warning("connect function triggered")
#     guiElement = getGuiElement("save_connect_button")
#     l.warning(f" guiElement: {guiElement}")
#     if guiElement:
#         guiElement.configure(text="Hinzugefügt")
#         # l.warning("Button konfiguriert.")
#     else: 
#         l.error("No Element ")