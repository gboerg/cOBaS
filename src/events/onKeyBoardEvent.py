# import logging as l
# import customtkinter as ctk
# from database.database import Builder, Features, websockets
# from functions.getGuiElement import getGuiElement




# def dbBuilderEntry(all_name, feature, content_kwargs: ctk, format_kwargs, command, location):
#     # Korrekte Prüfung ob Tabelle leer ist
#     pass
#     # return
#     format_kwargs
#     if not Builder.select().exists():
#         l.info("nothing in builder")
#         new_string = f"{location}+{all_name}"
        
#         Builder.get_or_create(
#             all_name  = all_name,
#             feature = new_string, 
#             content_kwargs = content_kwargs,
#             # format_kwargs = format_kwargs,
#             location = location,
#             command = command
#         )
#     elif Builder.select():
#         # Höchste Location finden und inkrementieren
#         # max_location_entry = Builder.select().order_by(Builder.location.desc()).first()
#         # new_location = max_location_entry.location + 1
        
#         # l.info(f"Entry detected placing new one at location: {new_location}")
#         new_string = f"{location}+{all_name}"
#         Builder.get_or_create(
#             all_name  = all_name,
#             feature = new_string,
#             content_kwargs = content_kwargs,
#             # format_kwargs = format_kwargs,
#             location = location,
#             command = command
#         )
    

    
# def destroyMainFrame():
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()
#     for each in mainFrameElements:
#         each.destroy()
        
        

        
# def checkMainFrame():
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()
    
#     currentLocationList = []
#     mainFrameItemLocationList = []
#     newFrameDict = {}
    
    
#     content = Builder.select()
#     # l.info(f"Content: {content}")
    
#     for entry in content:
#         combined_name = entry.feature
#         feature = entry.all_name
#         location = entry.location
        
        
#         currentLocationList.append({
#             "key": combined_name,
#             "feature": feature,
#             "location": location
#         })
        

    
#     for each in mainFrameElements:
#         try:
#             # l.info(f"each: {each}")
#             if each and isinstance(each, (ctk.CTkFrame)):
                
#                 for currentLocationItem in currentLocationList:
#                     name = currentLocationItem["key"]
#                     location = currentLocationItem["location"]

#                     r_widget = getGuiElement(f"{name}")
#                     if not r_widget:
#                         continue
#                     entry_value = r_widget.get()

#                     mainFrameItemLocationList.append({
#                         "key": name,
#                         "now_location": location,
#                         "desired_location": entry_value 
#                     })

#         except Exception as e:
#             l.error(f"Error in checkMainFrame: {e}")
            
#     # l.info(f"Database Location Checker: {currentLocationList}")
#     # l.info(f"Location entry checker: {mainFrameItemLocationList}")
            
    
    
    
#     for dbBuilder in currentLocationList:
#         dbName = dbBuilder["key"]
#         dbLocation = dbBuilder["location"]
#         raw_name = dbBuilder["feature"]
        
#         for inMainFrame in mainFrameItemLocationList:
#             db_name_in_main_frame= inMainFrame["key"]
#             db_item_in_main_frame_location = inMainFrame["now_location"]
#             desired_location = inMainFrame["desired_location"]
            
        

#             if dbName == db_name_in_main_frame:
#                 # l.info("DB Name Matches Name in Script")
                
#                 if dbLocation == desired_location:
#                     # l.info("Skipping Element no Change")
#                     continue
                
#                 elif dbLocation is not desired_location:
#                     # l.info(f"Changing Db Entry for {dbName} [old location: {dbLocation} / {db_item_in_main_frame_location}] | new Location: {desired_location}")
                    
                    
#                     getItemOnNewLocation = Builder.select().where(Builder.location == desired_location)
#                     for each in getItemOnNewLocation:
#                         switch_to = each.location
#                         featureRawNameOnNewLocation = each.all_name
#                         elementOnNewLocationCombinedName = each.feature
#                         # l.info(f"Switch location {switch_to} and name: {featureRawNameOnNewLocation} | Combined Name: {elementOnNewLocationCombinedName}")
                        
                        
                        
#                         # l.info(f"[Element {dbName}  Raw: {raw_name} Location: {db_item_in_main_frame_location}] tauscht mit [{featureRawNameOnNewLocation} | {elementOnNewLocationCombinedName} Location: {switch_to}] ---> [{featureRawNameOnNewLocation} | {elementOnNewLocationCombinedName}new Location: {dbLocation}]   <|> {dbName}  {raw_name} new Location: {desired_location}")

#                         newFrameDict[dbName] = {
#                             "changing_db_name": dbName,
#                             "changing_raw_name": raw_name,
#                             "changing_currentLocation": db_item_in_main_frame_location,
#                             "changing_new_location": desired_location,

#                             "changeWithElement": {
#                                 "info": "Auf der Location befindet Sich: ",
#                                 "switched_db_name": elementOnNewLocationCombinedName,
#                                 "switched_raw_name": featureRawNameOnNewLocation,
                                
#                                 "switched_current_location": switch_to,
#                                 "switched_changing_new_location": desired_location,
#                                 "switched_new_location": db_item_in_main_frame_location
#                             }
#                         }
#     # l.info(f"{newFrameDict} ist das neue Dict")
    
#     # NOTE: FINAL COMPARE LOOP AND DATABASE ENTRY CHANGE
#     for compare in content:
#         combined_name = compare.feature
#         feature = compare.all_name
#         location = compare.location
        
#         for key in newFrameDict:
            
#             # l.info(f"EACH KEY {key} and EACH COMBINED NAME: {combined_name}")
            
#             if key == combined_name:
#                 result = newFrameDict.get(key)
                
#                 changingDbItemName = result["changing_db_name"]
#                 changingFeatureName = result["changing_raw_name"]
#                 changingCurrentLocation = result["changing_currentLocation"]
#                 changingNewLocation = result["changing_new_location"]

#                 l.info("SINGLE ______________________________")
#                 l.info("changingDbItemName: %s", changingDbItemName)
#                 l.info("changingFeatureName: %s", changingFeatureName)
#                 l.info("changingCurrentLocation: %s", changingCurrentLocation)
#                 l.info("changingNewLocation: %s", changingNewLocation)
                
#                 switchWith = result["changeWithElement"]
#                 l.info("#########################################")
                
#                 # l.info(f"ALL SWITCH WITH ELEMENTS: {switchWith}")
                
#                 switchingDbItemName = switchWith["switched_db_name"]
#                 switchingFeatureName = switchWith["switched_raw_name"]
#                 switchingCurrentLocation = switchWith["switched_current_location"]
#                 switchingNewLocation = switchWith["switched_new_location"]
                
#                 # l.info("ALL ELEMENTS: ")
#                 l.info(f"switchingDbItemName: {switchingDbItemName}\n"
#                     f"switchingFeatureName: {switchingFeatureName}\n"
#                     f"switchingCurrentLocation: {switchingCurrentLocation}\n"
#                     f"switchingNewLocation: {switchingNewLocation}")
#                 l.info("SINGLE END ______________________________")



#                 l.info(f"ELEMENT: {changingDbItemName} von {changingCurrentLocation} will mit {switchingDbItemName} auf {switchingCurrentLocation} die Plätze Tauschen")
#                 l.info(f"ELEMENT {changingDbItemName} wird dann auf {switchingCurrentLocation} sein und {switchingDbItemName} wird dann auf {changingCurrentLocation} sein")


#                 dataBaseChange = [
#                     Builder.update({Builder.location: switchingCurrentLocation, Builder.feature: f"{switchingCurrentLocation}+{changingFeatureName}"}).where(Builder.feature == changingDbItemName),
#                     Builder.update({Builder.location: changingCurrentLocation, Builder.feature: f"{changingCurrentLocation}+{switchingFeatureName}"}).where(Builder.feature == switchingDbItemName)
#                 ]

#                 # qry = Builder.update({Builder.location: switchingCurrentLocation, Builder.feature: f"{switchingCurrentLocation}+{changingFeatureName}"}).where(Builder.feature == changingDbItemName)
#                 # l.info(f"SQL QUERY: {qry}")
#                 # qry = Builder.update({Builder.location: switchingNewLocation}).where(Builder.feature == switchingDbItemName)
#                 # qry2 = Builder.update({Builder.location: changingNewLocation}).where(Builder.feature == changingDbItemName)
#                 for function in dataBaseChange:
#                     l.info(f"FUNCTION SQL: {function}")
#                     function.execute()
#                 # qry2.execute()
        
    

    
    
    
    
    
# def rebuildBuilderContent():
#     websocket_list = []
#     builder_list = []
#     feature_list = []
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()
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
        
        
        
#     sorted_builder_list = sorted(builder_list, key=lambda item: item['location'])


    
#     # Für jeden Builder einen Button erstellen
#     for builder in sorted_builder_list:
#         builder_name = builder["key"]
#         location = int(builder["location"])
        

        
#         # Finde alle passenden WebSockets (CONTAINS)
#         for socket in websocket_list:
#             if builder_name in socket["key"] or socket["key"] in builder_name:  # ← CONTAINS!
#                 # l.info(f"Match: '{builder_name}' <-> '{socket['key']}'")
                
#                 alln = Builder.select().where(Builder.all_name == builder_name)
#                 name = Builder.select().where(Builder.feature.contains(builder_name))
                
#                 for each in name:
#                     # l.info(f"counter check: {each.all_name}")
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
#                 # l.info(f"Match: '{builder_name}' <-> '{feature['key']}'")
#                 removestring = "0123456789+-"
#                 for each in removestring:
#                     builder_name = builder_name.replace(each, "")
#                 # l.info(f"new name {builder_name}")
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
                
# def reloadBuilderContent():
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()

    


#     checkMainFrame()
#     destroyMainFrame()
#     rebuildBuilderContent()
    
                
                
                


# def generateButtonFrame(all_name, button_name: str, master, text_name, text_color, fg_color, location: int, db_entry: bool):
#     try:
#         frame_name = ctk.CTkFrame(master)
#         frame_name.pack(pady=(5, 5))
        
#         string = str(button_name)  

#         button_name = ctk.CTkButton(master=frame_name, text=f"Active {str(text_name)}", fg_color=fg_color, text_color=text_color)
#         button_name.configure(command=lambda btn=button_name: command_center(btn))
#         label = ctk.CTkLabel(frame_name, text=location)
#         label.pack(padx=(5,5), side = "left")
#         button_name.pack(side="right", padx=(5, 5))
#         locationLabel_entry = ""
#         # if "WebSocket" not in str(text_name): 
#         locationLabel = ctk.CTkLabel(master=frame_name, text="Active Location: ")
#         locationLabel_entry = ctk.CTkEntry(master=frame_name, placeholder_text="New Location")
#         locationLabel.pack(side="left", padx=(5, 5))
#         locationLabel_entry.pack(side="left", padx=(5, 5))
        
#         if "(" in string:
            
#             amount_label = ctk.CTkLabel(master=frame_name, text="Amount: ")
#             amount_label.pack(side="left", padx=(5,5))
#             amount_entry = ctk.CTkEntry(master=frame_name, placeholder_text="unit")
#             amount_entry.pack(side="right", padx=(5,5))
#         else:
#             amount_label = ctk.CTkLabel(master=frame_name, text="SPACER")
#             amount_label.pack(side="left", padx=(5,5))
#             amount_entry = ctk.CTkEntry(master=frame_name, placeholder_text="SPACER", )
#             amount_entry.pack(side="right", padx=(5,5))
#         # if "(" in button_name:
#         amount_entry.bind("<Return>", onKeyBoardEnterPress)
#         locationLabel_entry.bind("<Return>", onKeyBoardEnterPress)
#         # getGuiElement(f"{location}+{all_name}", )
#         getGuiElement(f"{location}+{all_name}", locationLabel_entry)
#         getGuiElement(f"{location}+{all_name}", amount_entry)
#         # if db_entry == True:
#         #     dbBuilderEntry(all_name=all_name, feature=string, content_kwargs=locationLabel_entry, format_kwargs=[fg_color, text_color], command=[f""], location=location)
#         #     return
#         if db_entry == True:
#             dbBuilderEntry(all_name=all_name, feature=string, content_kwargs=locationLabel_entry, format_kwargs=[fg_color, text_color], command=[f""], location=location)
        
#     except Exception as e:
#         l.error(f"Error in generateButtonFrame: {e}")

# def generateSwitchFrame(all_name, button_name: str, master, text_name, text_color, fg_color, switch_text_1, switch_text_2, obs_values, obs_to_values, location: int, db_entry: bool):
#     try:
#         obs_switch_frame = ctk.CTkFrame(master)
#         obs_switch_frame.pack(pady=(5, 5))
        
#         obs_location = ctk.CTkLabel(obs_switch_frame, text=f"Location: ")
#         obs_location.pack(side="left")
        
#         obs_location_entry = ctk.CTkEntry(obs_switch_frame, placeholder_text="Spot in Builder ")
#         obs_location_entry.pack(side="left")
#         obs_location_entry.bind("<Return>", onKeyBoardEnterPress)
        
#         button_widget = ctk.CTkButton(obs_switch_frame, text=f"Active {str(text_name)}", fg_color=fg_color, text_color=text_color)
#         button_widget.configure(command=lambda btn=button_widget: command_center(btn))
#         button_widget.pack(side="left", padx=(5, 5))

#         obs_switch_from_label = ctk.CTkLabel(obs_switch_frame, text=f"{switch_text_1} ")
#         obs_switch_from_label.pack(side="left")
        
        
#         obs_switch_from = ctk.CTkComboBox(obs_switch_frame, values=obs_values)
#         obs_switch_from.pack(side="left", padx=(5, 5))
        
#         obs_switch_to_label = ctk.CTkLabel(obs_switch_frame, text=f"{switch_text_2} ")
#         obs_switch_to_label.pack(side="left")
#         obs_switch_to = ctk.CTkComboBox(obs_switch_frame, values=obs_to_values)
#         obs_switch_to.pack(side="left", padx=(5, 5))
#         string = str(button_name)
        
#         if db_entry == True:
#             l.info("DB ENTRY DONE")
            
#     except Exception as e:
#         l.error(f"Error in generateSwitchFrame: {e}")
        
        

            
# def command_center(event: ctk.CTkButton):
    
#     mainFrame = getGuiElement("main_frame")
#     mainFrameElements = mainFrame.winfo_children()
#     for each in mainFrameElements:
#         l.info(f"each: {each}")
    
#     e_text = event.cget("text")
#     e_text_color = event.cget("text_color")
#     e_fg_color = event.cget("fg_color")
    
    
#     text = e_text
#     text_color = e_text_color
#     fg_color = e_fg_color
    
#     socketSingleDb = websockets.select().where(websockets.all_field.contains(text)).first()
    
#     featureSingleDb = Features.select().where(Features.feature.contains(text)).first()
#     builderSingleDB = Builder.select().where(Builder.feature.contains(text)).first()
#     l.info(f"BUILDER SINGLE: {builderSingleDB}")
#     for each in mainFrameElements:
#         if isinstance(each, (ctk.CTkLabel)):
#             request = each.cget("text")
#             l.info("got text")
#             if "SELECT WEBSOCKET FIRST!" or "SAME WEBSOCKET ALREADY SELECTED!" in request:
#                 l.info("before destroy")
#                 each.destroy()

#     if event.master.master == mainFrame and "Active " in text:
#             l.warn("DEL FUNC START")
#             try:
#                 extract = event.cget("text")
#                 f1 = extract.replace("Active", "")
#                 new_text = f1.lstrip()
#                 l.info(f"Text [{new_text}]")
                
#                 delete = Builder.delete().where(Builder.all_name == new_text)
#                 delete.execute()
#                 l.info(f"Datensatz gelöscht: {delete}")
                
#                 event.master.destroy()
#             except Exception as e:
#                 l.info(f"Fehler beim Löschen: {e}")
#     else:
#         l.info("Keine Lösch-Aktion, da es kein 'Active'-Element ist.")
            
    
    
#     # TODO: Bevor alles andere geplact wird muss ein Websocket platziert werden sobald ein Websocket vorhanden ist können andere Elemente folgen
        
#     if socketSingleDb and not "Active" in text:
        
        
#         for each in mainFrameElements:
#             if isinstance(each, (ctk.CTkLabel)):
#                 request = each.cget("text")
#                 l.info("got text")
#                 if "SELECT WEBSOCKET FIRST!" or "SAME WEBSOCKET ALREADY SELECTED!" in request:
#                     l.info("before destroy")
#                     each.destroy()

        
        
#         if Builder.select().where(Builder.all_name == text):
#             warning = ctk.CTkLabel(mainFrame, text="ERROR: WEBSOCKET ALREADY ACTIVE!", fg_color="red", corner_radius=8)
#             warning.pack(pady=(5,5))
#             l.info("CANCEL NO WEBSOCKET")
#             l.warn("existing socket creeate")


            
            
            
            
#         elif not Builder.select().where(Builder.all_name ==text) :
#             count = Builder.select().count()
#             if count:
#                 generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
#             else:
#                 if "WebSocket" in text:
#                     count = 0   
#                 else:
#                     count = 1
                    
#                 generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
        
        
        
#     if featureSingleDb and not "Active" in text: 
        
#         if Builder.select().where(Builder.all_name.contains("WebSocket")):
            
        
#             if "OBS" and not "[" in text:
#                 count = Builder.select().count()
#                 if count:
#                     generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
#                 else:   
#                     count = 1
#                     generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
#             elif "(" and not "["in text:
#                 count = Builder.select().count()
#                 if count:
#                     generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
#                 else:   
#                     count = 1
#                     generateButtonFrame(text, text, mainFrame, text, text_color, fg_color, count, True)
#             elif "[" in text:
                
#                 generateSwitchFrame(text, text, mainFrame, text, text_color, fg_color, "from", "to",["123", "456"], ["789", "012"], True)
#             else:
#                 l.info("Else Function")
                
                
#         else:
#             warning = ctk.CTkLabel(mainFrame, text="ERROR: SELECT WEBSOCKET FIRST!", fg_color="red", corner_radius=8)
#             warning.pack(pady=(5,5))
#             l.info("CANCEL NO WEBSOCKET")
        
        


# def onKeyBoardEnterPress(event):
#     reloadBuilderContent()
#     l.info(f"event: {event}")
#     l.warn("enter press detected")