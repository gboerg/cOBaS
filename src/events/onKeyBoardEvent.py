import logging as l
import customtkinter as ctk
from database.database import Builder, Features, websockets
from functions.getGuiElement import getGuiElement
import tkinter as tk
from typing import Optional




def onKeyBoardEnterPress(event: tk.Event, eventtype: Optional[str] = None):
    
    if eventtype:
        l.info(f"EventType: {eventtype}: {event.widget}")
        
        if "websocket" in eventtype:
            from interaction.defaultGUIButtons import connect
            connect()
    else:
        getItem = event.widget
        l.info(f"KEYBOARD ENTER EVENT: {getItem}")
        from interaction.commandCenter import reloadBuilderContent 
        reloadBuilderContent()

        # l.info(f"event: {event}")
        # l.warn("enter press detected")
    



