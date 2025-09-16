import customtkinter as ctk
import logging as l





from database.database import websockets, Features, Builder
from functions.getGuiElement import getGuiElement
from peewee import *
from optional import Optional
# from events.onKeyBoardEvent import onKeyBoardEnterPress
# from functions.sharedFunctions import onKeyBoardEnterPress





def dbBuilderEntry(all_name, feature, content_kwargs: ctk, format_kwargs, command, location):
    # Korrekte Prüfung ob Tabelle leer ist
    pass
    # return
    format_kwargs
    if not Builder.select().exists():
        l.info("nothing in builder")
        new_string = f"{location}+{all_name}"
        
        Builder.get_or_create(
            all_name  = all_name,
            feature = new_string, 
            content_kwargs = content_kwargs,
            # format_kwargs = format_kwargs,
            location = location,
            command = command
        )
    elif Builder.select():
        # Höchste Location finden und inkrementieren
        # max_location_entry = Builder.select().order_by(Builder.location.desc()).first()
        # new_location = max_location_entry.location + 1
        
        # l.info(f"Entry detected placing new one at location: {new_location}")
        new_string = f"{location}+{all_name}"
        Builder.get_or_create(
            all_name  = all_name,
            feature = new_string,
            content_kwargs = content_kwargs,
            # format_kwargs = format_kwargs,
            location = location,
            command = command
        )

def generateButtonFrame(all_name, button_name: str, master, text_name, text_color, fg_color, location: int, db_entry: bool):
    try:
        frame_name = ctk.CTkFrame(master)
        frame_name.pack(pady=(5, 5))
        
        string = str(button_name)  

        button_name = ctk.CTkButton(master=frame_name, text=f"Active {str(text_name)}", fg_color=fg_color, text_color=text_color)
        button_name.configure(command=lambda btn=button_name: command_center(btn))
        label = ctk.CTkLabel(frame_name, text=location)
        label.pack(padx=(5,5), side = "left")
        button_name.pack(side="right", padx=(5, 5))
        locationLabel_entry = ""
        if "WebSocket" not in str(text_name): 
            locationLabel = ctk.CTkLabel(master=frame_name, text="Active Location: ")
            locationLabel_entry = ctk.CTkEntry(master=frame_name, placeholder_text="New Location")
            locationLabel.pack(side="left", padx=(5, 5))
            locationLabel_entry.pack(side="left", padx=(5, 5))
            # locationLabel_entry.bind("<Return>", onKeyBoardEnterPress)
            
            getGuiElement(f"{location}+{all_name}", locationLabel_entry)
            # if db_entry == True:
            #     dbBuilderEntry(all_name=all_name, feature=string, content_kwargs=locationLabel_entry, format_kwargs=[fg_color, text_color], command=[f""], location=location)
            #     return
        if db_entry == True:
            dbBuilderEntry(all_name=all_name, feature=string, content_kwargs=locationLabel_entry, format_kwargs=[fg_color, text_color], command=[f""], location=location)
        
    except Exception as e:
        l.error(f"Error in generateButtonFrame: {e}")

def generateSwitchFrame(all_name, button_name: str, master, text_name, text_color, fg_color, switch_text_1, switch_text_2, obs_values, obs_to_values, location: int, db_entry: bool):
    try:
        obs_switch_frame = ctk.CTkFrame(master)
        obs_switch_frame.pack(pady=(5, 5))
        
        obs_location = ctk.CTkLabel(obs_switch_frame, text=f"Location: ")
        obs_location.pack(side="left")
        
        obs_location_entry = ctk.CTkEntry(obs_switch_frame, placeholder_text="Spot in Builder ")
        obs_location_entry.pack(side="left")
        obs_location_entry.bind("<Return>", onKeyBoardEnterPress)
        
        button_widget = ctk.CTkButton(obs_switch_frame, text=f"Active {str(text_name)}", fg_color=fg_color, text_color=text_color)
        button_widget.configure(command=lambda btn=button_widget: command_center(btn))
        button_widget.pack(side="left", padx=(5, 5))

        obs_switch_from_label = ctk.CTkLabel(obs_switch_frame, text=f"{switch_text_1} ")
        obs_switch_from_label.pack(side="left")
        
        
        obs_switch_from = ctk.CTkComboBox(obs_switch_frame, values=obs_values)
        obs_switch_from.pack(side="left", padx=(5, 5))
        
        obs_switch_to_label = ctk.CTkLabel(obs_switch_frame, text=f"{switch_text_2} ")
        obs_switch_to_label.pack(side="left")
        obs_switch_to = ctk.CTkComboBox(obs_switch_frame, values=obs_to_values)
        obs_switch_to.pack(side="left", padx=(5, 5))
        string = str(button_name)
        
        if db_entry == True:
            l.info("DB ENTRY DONE")
            
    except Exception as e:
        l.error(f"Error in generateSwitchFrame: {e}")
        
        

            
def command_center(event: ctk.CTkButton):
    
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()
    for each in mainFrameElements:
        l.info(f"each: {each}")
    
    e_text = event.cget("text")
    e_text_color = event.cget("text_color")
    e_fg_color = event.cget("fg_color")
    
    
    text = e_text
    text_color = e_text_color
    fg_color = e_fg_color
    
    socketSingleDb = websockets.select().where(websockets.all_field.contains(text)).first()
    
    featureSingleDb = Features.select().where(Features.feature.contains(text)).first()
    builderSingleDB = Builder.select().where(Builder.feature.contains(text)).first()
    l.info(f"BUILDER SINGLE: {builderSingleDB}")
    for each in mainFrameElements:
        if isinstance(each, (ctk.CTkLabel)):
            request = each.cget("text")
            l.info("got text")
            if "SELECT WEBSOCKET FIRST!" or "SAME WEBSOCKET ALREADY SELECTED!" in request:
                l.info("before destroy")
                each.destroy()

    if event.master.master == mainFrame and "Active " in text:
            l.warn("DEL FUNC START")
            try:
                extract = event.cget("text")
                f1 = extract.replace("Active", "")
                new_text = f1.lstrip()
                l.info(f"Text [{new_text}]")
                
                delete = Builder.delete().where(Builder.all_name == new_text)
                delete.execute()
                l.info(f"Datensatz gelöscht: {delete}")
                
                event.master.destroy()
            except Exception as e:
                l.info(f"Fehler beim Löschen: {e}")
    else:
        l.info("Keine Lösch-Aktion, da es kein 'Active'-Element ist.")
            
    
    
    # TODO: Bevor alles andere geplact wird muss ein Websocket platziert werden sobald ein Websocket vorhanden ist können andere Elemente folgen
        
    if socketSingleDb and not "Active" in text:
        
        
        for each in mainFrameElements:
            if isinstance(each, (ctk.CTkLabel)):
                request = each.cget("text")
                l.info("got text")
                if "SELECT WEBSOCKET FIRST!" or "SAME WEBSOCKET ALREADY SELECTED!" in request:
                    l.info("before destroy")
                    each.destroy()

        
        
        if Builder.select().where(Builder.all_name == text):
            warning = ctk.CTkLabel(mainFrame, text="ERROR: WEBSOCKET ALREADY ACTIVE!", fg_color="red", corner_radius=8)
            warning.pack(pady=(5,5))
            l.info("CANCEL NO WEBSOCKET")
            l.warn("existing socket creeate")


            
            
            
            
        elif not Builder.select().where(Builder.all_name ==text) :
            count = Builder.select().count()
            if count:
                generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
            else:
                if "WebSocket" in text:
                    count = 0   
                else:
                    count = 1
                    
                generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
        
        
        
    if featureSingleDb and not "Active" in text: 
        
        if Builder.select().where(Builder.all_name.contains("WebSocket")):
            
        
            if "OBS" and not "[" in text:
                count = Builder.select().count()
                if count:
                    generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
                else:   
                    count = 1
                    generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
            elif "(" and not "["in text:
                count = Builder.select().count()
                if count:
                    generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
                else:   
                    count = 1
                    generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
            elif "[" in text:
                
                generateSwitchFrame(text, text, mainFrame, text, text_color, fg_color, "from", "to",["123", "456"], ["789", "012"], True)
            else:
                l.info("Else Function")
                
                
        else:
            warning = ctk.CTkLabel(mainFrame, text="ERROR: SELECT WEBSOCKET FIRST!", fg_color="red", corner_radius=8)
            warning.pack(pady=(5,5))
            l.info("CANCEL NO WEBSOCKET")
        
        

    
        