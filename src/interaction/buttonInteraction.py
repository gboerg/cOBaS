
import logging as l
from functions.getGuiElement import getGuiElement
from database.restoreManager import insertKnownWebsocketsInGui
import peewee

from database.database import websockets
import time

import customtkinter as ctk




def recording_checkbox():
    l.warning("Record Function ticked")

def connect():
    l.warning("connect function triggered")
    guiElement = getGuiElement("connect_button")
    if guiElement:
        hostElement = getGuiElement("host_entry")
        portElement = getGuiElement("port_entry")
        passElement = getGuiElement("password_entry")

        if not hostElement or not portElement or not passElement:
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
                try:
                    # Verwende get_or_create, um das Objekt zu finden oder zu erstellen
                    entry, created = websockets.get_or_create(
                        host=host, 
                        port=int(port),  # Wichtig: Port in einen Integer umwandeln
                        defaults={'password': passw}
                    )
                    
                    if created:
                        l.info("Neuer Eintrag in der Datenbank erstellt.")
                        # Füge NUR den neuen Eintrag in die GUI ein
                        insertKnownWebsocketsInGui()
                        guiElement.configure(text= "Connected")
                    else:
                        l.warning("Eintrag existiert bereits. Kein neuer Eintrag in DB oder GUI.")
                        guiElement.configure(text= "Already Exists")
                        guiElement.after(5000, lambda: guiElement.configure(text="Connect"))

                except ValueError:
                    l.error("Fehler: Port-Wert ist keine gültige Zahl.")
                    guiElement.configure(text="Invalid Port")
                    guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
                except peewee.IntegrityError:
                    l.error("Fehler: Datenbank-Integritätsverletzung.")
                    guiElement.configure(text="DB Error")
                    guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
    else: 
        l.error("No Element ")

def add_connect():
    # l.warning("connect function triggered")
    guiElement = getGuiElement("save_connect_button")
    l.warning(f" guiElement: {guiElement}")
    if guiElement:
        guiElement.configure(text="Hinzugefügt")
        # l.warning("Button konfiguriert.")
    else: 
        l.error("No Element ")