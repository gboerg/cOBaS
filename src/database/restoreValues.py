from database.database import websockets
from functions.getGuiElement import getGuiElement

import customtkinter as ctk
import logging as l



def insertKnownWebsocketsInGui():
    dbResult = websockets.select()

    if dbResult:
        for each in dbResult:
            host = each.host
            port = each.port
            passw = each.password
            l.warning(f"each in values: {host}, {port}, {passw}")

            scrollbox = getGuiElement("websocket_scrollbox")
            if not scrollbox or scrollbox is None:
                return
            
            websocket = ctk.CTkButton(scrollbox, text=f"OBS CONNECTION: [{host}, {port}]")
            websocket.pack(anchor="w")
    # l.warning(f"DB RESULT: {dbResult.host}")
