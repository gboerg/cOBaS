from database.database import websockets, Features
from functions.getGuiElement import getGuiElement
from events.onMouseEvent import onDrag

import customtkinter as ctk
import logging as l



def insertKnownWebsocketsInGui():
    scrollbox = getGuiElement("websocket_scrollbox")
    if not scrollbox or scrollbox is None:
        return

    # Zerstöre alle Widgets im Scrollable Frame, um Duplikate zu vermeiden
    for widget in scrollbox.winfo_children():
        widget.destroy()
    
    dbResult = websockets.select()

    if dbResult:
        for each in dbResult:
            host = each.host
            port = each.port
            
            # Füge das neue Label hinzu
            websocket = ctk.CTkLabel(scrollbox, text=f"OBS CONNECTION: [{host}, {port}]", fg_color="purple", corner_radius=5, text_color="white")
            websocket.pack(anchor="w", pady=(6, 6))
            websocket.bind('<B1-Motion>', onDrag)

def debubVals():
    features_to_add = ["obs_toggle_recording", "obs_toggle_streaming", "add_delay" ]
    for feature_name in features_to_add:
        Features.get_or_create(feature=feature_name) # Assuming your field is named 'name' or similar

def insertAvailable():
    obsFeatures = getGuiElement("obs_features")
    miscFeatures = getGuiElement("misc_features")

    if not obsFeatures or obsFeatures is None:
        return
    if not miscFeatures or miscFeatures is None:
        return
    
    featureDB = Features.select()

    for each in featureDB:
        feature = each.feature
        
        if "obs" in feature:
            l.warning(f"FeatureOBS: {feature}")

            new_name = feature.replace("obs_", "")
            feat = ctk.CTkLabel(obsFeatures, text=f"{new_name}", fg_color="blue", corner_radius=5, text_color="white")
            feat.pack(anchor="w", pady=(6, 6))
            feat.bind('<B1-Motion>', onDrag)
            getGuiElement(f"{new_name}", feat)
            
        if not "obs" in feature:
            feat = ctk.CTkLabel(miscFeatures, text=f"{feature}", fg_color="green", corner_radius=5, text_color="white")
            feat.pack(anchor="w", pady=(6, 6))
            feat.bind('<B1-Motion>', onDrag)
            getGuiElement(f"{feature}", feat)