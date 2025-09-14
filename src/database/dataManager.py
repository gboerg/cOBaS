from database.database import websockets, Features, Builder
from functions.getGuiElement import getGuiElement
from events.onMouseEvent import onDrag, onDrop
import random
import matplotlib.colors as mcolors
from matplotlib_colors import colormap_names
from interaction.commandCenter import command_center
# from interaction.buttonInteraction import command_center

import customtkinter as ctk
import logging as l


import colorsys
import colorsys
import random
import matplotlib.colors as mcolors


def insertKnownWebsocketsInGui():
    scrollbox = getGuiElement("websocket_scrollbox")
    if not scrollbox or scrollbox is None:
        return

    # Zerstöre alle Widgets im Scrollable Frame, um Duplikate zu vermeiden
    for widget in scrollbox.winfo_children():
        widget.destroy()
    
    dbResult = websockets.select()
    dbResult2 = Builder.select()

    if dbResult:
        for each in dbResult:
            host = each.host
            port = each.port
            name = each.name
            color = each.color
            text_color = each.text_color
            
            
            if len(name) > 0:
                websocket_name = ctk.CTkButton(scrollbox, text=f"WebSocket: {name} | Host: {host} | Port: {port}", fg_color=color, corner_radius=5, text_color=text_color)
                websocket_name.configure(command=lambda btn=websocket_name: command_center(btn))
                websocket_name.pack(anchor="w", pady=(6, 6))
                # websocket_name.bind('<B1-Motion>', onDrag)
                # websocket_name.bind("<ButtonRelease-1>", onDrop)
                # websocket_name.bind('<Button-1>', command_center)
                # websocket_name.bind('Button-3', command_center)
                # getGuiElement()
            else:
                # Füge das neue Label hinzu
                websocket = ctk.CTkButton(scrollbox, text=f"OBS CONNECTION: [{host}, {port}]", fg_color=red_bg, corner_radius=5, text_color=text_color)
                websocket.configure(command=lambda btn=websocket: command_center(btn))
                websocket.pack(anchor="w", pady=(6, 6))
                # websocket.bind('<Button-1>', command_center)
                # websocket.bind('Button-3', command_center)
                # websocket.bind("<B1-Motion>", onDrag)
                # websocket.bind("<ButtonRelease-1>", onDrop)

def debubVals():
    features_to_add = [
        # Audio/Input Controls
        "OBS Get Input List",
        "OBS Get Input Mute",
        "OBS Get Input Settings",
        "OBS Get Input Volume", 
        "OBS Set Input Mute",
        "OBS Set Input Settings",
        "OBS Set Input Volume",
        "OBS Toggle Input Mute",
        
        # General/System
        "OBS Get Version",
        "OBS Get Stats",
        "OBS Get Profile List",
        "OBS Get Current Profile",
        "OBS Set Current Profile",
        "OBS Get Scene Collection List", 
        "OBS Get Current Scene Collection",
        "OBS Set Current Scene Collection",
        "OBS Create Scene Collection",
        "OBS Get Hotkey List",
        "OBS Trigger Hotkey By Name",
        
        # Recording Controls
        "OBS Get Record Status",
        "OBS Start Record",
        "OBS Stop Record",
        "OBS Toggle Recording",  # Bereits vorhanden
        "OBS Pause Record",
        "OBS Resume Record",
        
        # Replay Buffer
        "OBS Get Replay Buffer Status",
        "OBS Start Replay Buffer",
        "OBS Stop Replay Buffer",
        "OBS Save Replay Buffer",
        "OBS Toggle Instant Replay()",  # Bereits vorhanden
        
        # Scene Controls
        "OBS Get Current Program Scene", 
        "OBS Get Current Preview Scene",
        "OBS Get Scene List",
        "OBS Set Current Program Scene",
        "OBS Set Current Preview Scene", 
        "OBS Create Scene",
        "OBS Remove Scene",
        "OBS Set Scene Name",
        "OBS Switch Scene[entry1, entry2]",  # Angepasst von bestehend
        
        # Scene Items
        "OBS Get Scene Item List",
        "OBS Get Scene Item Enabled",
        "OBS Set Scene Item Enabled",
        "OBS Get Scene Item Transform",
        "OBS Set Scene Item Transform",
        "OBS Get Scene Item Index",
        "OBS Set Scene Item Index",
        
        # Sources
        "OBS Get Source Active",
        "OBS Get Source Screenshot",
        "OBS Get Source Settings", 
        "OBS Set Source Settings",
        "OBS Create Input",
        "OBS Remove Input",
        
        # Streaming Controls  
        "OBS Get Stream Status",
        "OBS Start Stream",  # Bereits vorhanden
        "OBS Stop Stream",
        "OBS Toggle Streaming",  # Bereits vorhanden
        "OBS Send Stream Caption",
        
        # Studio Mode
        "OBS Get Studio Mode Enabled",
        "OBS Set Studio Mode Enabled", 
        "OBS Toggle Studio Mode",
        "OBS Trigger Studio Mode Transition",
        
        # Transitions
        "OBS Get Current Scene Transition",
        "OBS Set Current Scene Transition",
        "OBS Get Scene Transition List",
        "OBS Get Transition Duration", 
        "OBS Set Transition Duration",
        "OBS Trigger Scene Transition",
        
        # Virtual Camera
        "OBS Get Virtual Cam Status",
        "OBS Start Virtual Cam",
        "OBS Stop Virtual Cam", 
        "OBS Toggle Virtual Cam",
        
        # Media Controls  
        "OBS Trigger Media Input Action",
        "OBS Get Media Input Status",
        "OBS Set Media Input Cursor",
        "OBS Offset Media Input Cursor",
        
        # Filters
        "OBS Get Source Filter List",
        "OBS Get Source Filter",
        "OBS Set Source Filter Enabled",
        "OBS Set Source Filter Settings",
        "OBS Create Source Filter",
        "OBS Remove Source Filter",
        
        # Custom/Vendor
        "OBS Call Vendor Request",
        "OBS Broadcast Custom Event",
        
        # Utility Functions (bereits vorhanden)
        "add_Delay(amount)",
        "end_of_function",
        "repeat(times)"
    ]
    
    for feature_name in features_to_add:
        get_content = Features.select().where(Features.feature == feature_name)
        if get_content:
            continue
        elif not get_content:
        
            if "OBS" in feature_name:
                blue_bg = "blue"
                blue_text = "white"
                if "toggle" in feature_name:
                    Features.get_or_create(feature=feature_name, allow_follow = False, feature_color = blue_bg, feature_text_color = blue_text)
                else:
                    Features.get_or_create(feature=feature_name, allow_follow = True, feature_color = blue_bg, feature_text_color = blue_text)
            elif "()" or () in feature_name:
                color= "green"
                text_color = "white"
                Features.get_or_create(feature=feature_name, allow_follow = True, feature_color = color, feature_text_color = text_color)
        

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
        color = each.feature_color
        text_color = each.feature_text_color

            
        if "OBS" in feature:
            

            new_name = feature
            feat_obs = ctk.CTkButton(obsFeatures, text=f"{new_name}", fg_color=color, corner_radius=5, text_color=text_color )
            feat_obs.configure(command=lambda btn=feat_obs: command_center(btn))
            feat_obs.pack(anchor="w", pady=(6, 6))
 
            getGuiElement(f"{new_name}", feat_obs)
            
        if not "OBS" in feature:
            if "()" or () in feature:
                feat_amount = ctk.CTkButton(miscFeatures, text=f"{feature}", fg_color=color, corner_radius=5, text_color=text_color, )
                feat_amount.configure(command=lambda btn=feat_amount: command_center(btn))
                feat_amount.pack(anchor="w", pady=(6, 6))

            else:
                feat_else = ctk.CTkButton(miscFeatures, text=f"{feature}", fg_color=color, corner_radius=5, text_color=text_color,)
                feat_else.configure(command=lambda btn=feat_else: command_center(btn))
                feat_else.pack(anchor="w", pady=(6, 6))


def insertMiscAvailable():
    miscFeatures = getGuiElement("misc_features")

    if not miscFeatures or miscFeatures is None:
        return
    
    featureDB = Features.select()

    for each in featureDB:
        feature = each.feature
        
        if not "OBS" in feature:
            color = "green" 
            text_color = "white"
            if "(" in feature:
                feat_amount_2 = ctk.CTkLabel(miscFeatures, text=f"{feature}", fg_color=color, corner_radius=5, text_color=text_color, )
                # feat_amount_2.configure(command=lambda btn=feat_amount_2: command_center(btn))
                feat_amount_2.pack(anchor="w", pady=(6, 6))

            else:
                feat_else_2 = ctk.CTkLabel(miscFeatures, text=f"{feature}", fg_color=color, corner_radius=5, text_color=text_color, )
                # feat_else_2.configure(command=lambda btn=feat_else_2: command_center(btn))
                feat_else_2.pack(anchor="w", pady=(6, 6))