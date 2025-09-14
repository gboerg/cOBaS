
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


from database.database import websockets, Features, Builder

import colorsys


# def destroyMainFrame():
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()
#     for each in mainFrameElements:
#         each.destroy()


# def previousVals(entry):
#     selectprevios_location = Builder.select().where(Builder.location == entry)
#     prev_location=""
#     prev_all_name=""
#     for each in selectprevios_location:
#         prev_location= each.location
#         prev_all_name = each.all_name
        
# return p
# def crossfunction():
#     reloadBuilderContent()
    
# def checkMainFrame():
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()
#     for each in mainFrameElements:
        
#         try:
#             l.info(f"each: {each}")
#             if each:
#                 l.info(f"Elements detected Resorting: {each}")
#                 if isinstance(each, (ctk.CTkFrame)):
#                     content = Builder.select()
#                     l.info(f"Content: {content}")
                    
#                     for each in content:
#                         feature = each.feature
#                         all_name = each.all_name
#                         location = each.location
#                         l.info(f"entry: {feature}")
                        
#                         if "WebSocket" not in feature:
#                             r_widget = getGuiElement(f"{feature}")
#                             entry = r_widget.get()
                            
#                             l.info(f"Widget entry value: {entry}")
                            
#                             if entry == "0":
#                                 l.info("Entry is 0, returning")
#                                 return
                            
#                             if entry:

#                                 selectprevios_location = Builder.select().where(Builder.location == entry)
#                                 prev_location=""
#                                 prev_all_name=""
#                                 for each in selectprevios_location:
#                                     prev_location= each.location
#                                     prev_all_name = each.all_name
                                    
                                    
#                                     delete = Builder.delete().where(Builder.all_name == all_name)
#                                     delete.execute()
#                                     delete2 = Builder.delete().where(Builder.all_name == prev_all_name)
#                                     delete2.execute()
                                    
#                                     dbBuilderEntry(all_name=all_name, feature=feature, content_kwargs="", format_kwargs="", command="", location=entry)
#                                     dbBuilderEntry(all_name=prev_all_name, feature=feature, content_kwargs="", format_kwargs="", command="", location=location)
                                
                                    
#                                 l.info(f"Entry: {all_name} changes place with {prev_all_name} | {all_name} is now on {prev_location} and {prev_all_name} is{entry}")
#                                 l.info("after")
#                                 return
  
#                 # 
#                 return

#         except Exception as e:
#             l.info(f"error {e}")
      
# def reloadBuilderContent():
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()

#     websocket_list = []
#     builder_list = []
#     feature_list = []
    


#     checkMainFrame()
#     destroyMainFrame()
    
    
#     # Alle Daten als Listen sammeln
#     for socket in websockets.select():
#         websocket_list.append({
#             "key": socket.all_field,
#             "color": socket.color,
#             "text_color": socket.text_color
#         })
    
#     for script in Builder.select():
#         builder_list.append({
#             "key": script.feature,
#             "location": script.location,
#             "content_kwargs": script.content_kwargs
#         })
    
#     for feature in Features.select():
#         feature_list.append({
#             "key": feature.feature,
#             "color": feature.feature_color,
#             "text_color": feature.feature_text_color
#         })
        
        
        

    
#     # Für jeden Builder einen Button erstellen
#     for builder in builder_list:
#         builder_name = builder["key"]
#         location = int(builder["location"])
        

        
#         # Finde alle passenden WebSockets (CONTAINS)
#         for socket in websocket_list:
#             if builder_name in socket["key"] or socket["key"] in builder_name:  # ← CONTAINS!
#                 l.info(f"Match: '{builder_name}' <-> '{socket['key']}'")
                
#                 alln = Builder.select().where(Builder.all_name == builder_name)
#                 name = Builder.select().where(Builder.feature.contains(builder_name))
                
#                 for each in name:
#                     l.info(f"counter check: {each.all_name}")
#                     builder_name = each.all_name
                    
                
#                 generateButtonFrame(
#                     all_name=f"{alln}",
#                     button_name=builder_name,
#                     master=mainFrame,
#                     text_color=socket["text_color"],
#                     text_name=builder_name,
#                     fg_color=socket["color"],
#                     location=location,
#                     db_entry=False
#                 )
        
#         # Finde alle passenden Features (CONTAINS)
#         for feature in feature_list:
#             if builder_name in feature["key"] or feature["key"] in builder_name:  # ← CONTAINS!
#                 l.info(f"Match: '{builder_name}' <-> '{feature['key']}'")
#                 removestring = "0123456789+-"
#                 for each in removestring:
#                     builder_name = builder_name.replace(each, "")
#                 l.info(f"new name {builder_name}")
#                 generateButtonFrame(
                    
                    
#                     all_name=f"{builder_name}",
#                     button_name=builder_name,
#                     master=mainFrame,
#                     text_color=feature["text_color"],
#                     text_name=builder_name,
#                     fg_color=feature["color"],
#                     location=location,
#                     db_entry=False
#                 )
    
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
        
        
        if not name or None:
            name="Empty"
        # Leere Strings behandeln
        # name = name_str if name_str else None
        
        if not host or not port or not passw:
            guiElement.configure(text="ENTER VALUES")
            guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
            return
        else:
            try:
                port_int = int(port)
                red_bg= "white"
                red_text = "black"
                
                all_field_string = f'WebSocket: {name} | Host: {host} | Port: {port}'
                
                result = websockets.select().where(websockets.all_field == all_field_string)
                
                if not result:
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
                

            except ValueError:
                l.error("Fehler: Port-Wert ist keine gültige Zahl.")
                guiElement.configure(text="Invalid Port")
                guiElement.after(5000, lambda: guiElement.configure(text="Connect"))
            except peewee.IntegrityError:
                l.error("Fehler: Datenbank-Integritätsverletzung.")
                guiElement.configure(text="DB Error")
                guiElement.after(5000, lambda: guiElement.configure(text="Connect"))






def add_connect():
    # l.warning("connect function triggered")
    guiElement = getGuiElement("save_connect_button")
    l.warning(f" guiElement: {guiElement}")
    if guiElement:
        guiElement.configure(text="Hinzugefügt")
        # l.warning("Button konfiguriert.")
    else: 
        l.error("No Element ")