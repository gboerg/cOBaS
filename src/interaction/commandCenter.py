import customtkinter as ctk
import logging as l





from database.database import websockets, Features, Builder
from events.onKeyBoardEvent import onKeyBoardEnterPress
from functions.getGuiElement import getGuiElement
from peewee import *
from typing import Optional

# from functions.sharedFunctions import reloadBuilderContent

# from events.onKeyBoardEvent import onKeyBoardEnterPress
# from functions.sharedFunctions import onKeyBoardEnterPress





def dbBuilderEntry(name, location, value: Optional[any]= None, value2: Optional[any]= None, value3: Optional[any]= None, value4: Optional[any]= None, value5: Optional[any]= None):

    if not Builder.select().exists():
        l.info("nothing in builder")
        new_string = f"{location}+{name}"
        
        Builder.get_or_create(
            feature = new_string, 
            name  = name,
            value = value,
            location = location,
            
        )
    elif Builder.select():

        new_string = f"{location}+{name}"
        Builder.get_or_create(
            feature = new_string,
            name  = name,
            value = value,
            location = location,
        )

def generateButtonFrame(name, button_name: str, master, text_name, text_color, fg_color, location: int, db_entry: bool, value: Optional[any]= None, value2: Optional[any]= None, value3: Optional[any]= None, value4: Optional[any]= None, value5: Optional[any]= None):
    try:
        # TODO: CREATE GRID "DYNAMIC" ELEMENT
        frame_name = ctk.CTkFrame(master)
        frame_name.grid(pady=(10,10), sticky="ew")

                    

        frame_name.grid_columnconfigure(0, weight=0)  # Label
        frame_name.grid_columnconfigure(1, weight=0)  # Spacer
        frame_name.grid_columnconfigure(2, weight=0)  # LocationLabel
        frame_name.grid_columnconfigure(3, weight=0)  # Location Entry
        frame_name.grid_columnconfigure(4, weight=0)  # Button
        frame_name.grid_columnconfigure(5, weight=1)  # SPACER COLUMN - This ensures consistent spacing
        frame_name.grid_columnconfigure(6, weight=0)  # Amount Label
        frame_name.grid_columnconfigure(7, weight=0)  # Amount Entry
        frame_name.grid_columnconfigure(8, weight=0)  # Amount Entry
        frame_name.grid_columnconfigure(9, weight=0)  
        string = str(button_name)  

        button_name = ctk.CTkButton(master=frame_name, text=f"Active {str(text_name)}", fg_color=fg_color, text_color=text_color, hover_color="purple")
        button_name.configure(command=lambda btn=button_name: command_center(btn))
        button_name.grid(row=0, column=9, padx=5, sticky="w")  # Changed to sticky="w" for left alignment
        
        label = ctk.CTkLabel(frame_name, text=location)
        label.grid(row=0, column=0, padx=5, sticky="w")
        
        location_entry = ""
        amount_entry = ""
        currentAmount =""
        
        locationLabel = ctk.CTkLabel(master=frame_name, text="New Location: ")
        location_entry = ctk.CTkEntry(master=frame_name, placeholder_text="New Location")
        
        locationLabel.grid(row=0, column=2, padx=(10, 0))  # Added padding for spacing
        location_entry.grid(row=0, column=3, padx=(5, 10))
        
        location_entry.bind("<Return>", onKeyBoardEnterPress)
        if "(" in string:
            
  
            #TODO: AMOUNT INSERT LABEL
            # # search = f"{location}+{string}" 
            # if not value:
            #     value = 0
                
            # getDBVals

            
            currentAmount = ctk.CTkLabel(master=frame_name, text=value)
            currentAmount.grid(row=0, column=6, sticky="w", padx=(5,5))
            
                
            
            
            amount_label = ctk.CTkLabel(master=frame_name, text="Amount: ")
            amount_label.grid(row=0, column=7, sticky="w", padx=(0, 5))
            
            amount_entry = ctk.CTkEntry(master=frame_name, placeholder_text="unit")
            amount_entry.grid(row=0, column=8, sticky="ew", padx=(0, 5))
            
            amount_entry.bind("<Return>", onKeyBoardEnterPress)
            
        getGuiElement(f"{location}amount_entry{name}", amount_entry)
        getGuiElement(f"{location}+{name}", location_entry)
        
        if db_entry == True:
            dbBuilderEntry(name=name, location=location, value=value)
        
    except Exception as e:
        l.error(f"Error in generateButtonFrame: {e}")

def generateSwitchFrame(name, button_name: str, master, text_name, text_color, fg_color, switch_text_1, switch_text_2, obs_values, obs_to_values, location: int, db_entry: bool):
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
                
                delete = Builder.delete().where(Builder.name == new_text)
                delete.execute()
                l.info(f"Datensatz gelöscht: {delete}")
                
                event.master.destroy()
            except Exception as e:
                l.info(f"Fehler beim Löschen: {e}")
    else:
        l.info("Keine Lösch-Aktion, da es kein 'Active'-Element ist.")
            
    
    
    # TODO: Bevor alles andere geplact wird muss ein Websocket platziert werden sobald ein Websocket vorhanden ist können andere Elemente folgen
        
    if socketSingleDb and not "Active" in text:
        
        l.info(f" The text: {text}")
        for each in mainFrameElements:
            if isinstance(each, (ctk.CTkLabel)):
                request = each.cget("text")
                l.info("got text")
                if "SELECT WEBSOCKET FIRST!" or "SAME WEBSOCKET ALREADY SELECTED!" in request:
                    l.info("before destroy")
                    each.destroy()

        
        
        if Builder.select().where(Builder.feature == text):
            warning = ctk.CTkLabel(mainFrame, text="ERROR: WEBSOCKET ALREADY ACTIVE!", fg_color="red", corner_radius=8)
            warning.pack(pady=(5,5))
            l.info("CANCEL NO WEBSOCKET")
            l.warn("existing socket creeate")


            
            
            
            
        elif not Builder.select().where(Builder.feature ==text) :
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
        
        if Builder.select().where(Builder.feature.contains("WebSocket")):
            
        
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
            # warning.pack(pady=(5,5))
            l.info("CANCEL NO WEBSOCKET")
        
        
def rebuildBuilderContent():
    websocket_list = []
    builder_list = []
    feature_list = []
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()
    # Alle Daten als Listen sammeln
    for socket in websockets.select():
        websocket_list.append({
            "key": socket.all_field,
            "color": socket.color,
            "text_color": socket.text_color
        })
    
    for script in Builder.select():
        value=0
        value2=0
        value3=0
        value4=0
        value5=0
        builder_list.append({
            "key": script.feature,
            "location": script.location,
            "value": script.value,
            "value2": script.value2,
            "value3": script.value3,
            "value4": script.value4,
            "value5": script.value5
            
        })
    
    for feature in Features.select():
        feature_list.append({
            "key": feature.feature,
            "color": feature.feature_color,
            "text_color": feature.feature_text_color
        })
        
        
        
    sorted_builder_list = sorted(builder_list, key=lambda item: item['location'])


    
    # Für jeden Builder einen Button erstellen
    for builder in sorted_builder_list:
        builder_name = builder["key"]
        location = int(builder["location"])
        value = builder["value"]
        value2 = builder["value2"]
        value3= builder["value3"]
        value4=builder["value4"]
        value5=builder["value5"]

        
        # Finde alle passenden WebSockets (CONTAINS)
        for socket in websocket_list:
            if builder_name in socket["key"] or socket["key"] in builder_name:  # ← CONTAINS!
                # l.info(f"Match: '{builder_name}' <-> '{socket['key']}'")
                
                alln = Builder.select().where(Builder.name == builder_name)
                name = Builder.select().where(Builder.feature.contains(builder_name))
                
                for each in name:
                    # l.info(f"counter check: {each.name}")
                    builder_name = each.name
                    
                
                generateButtonFrame(
                    name=f"{alln}",
                    button_name=builder_name,
                    master=mainFrame,
                    text_color=socket["text_color"],
                    text_name=builder_name,
                    fg_color=socket["color"],
                    location=location,
                    db_entry=False,
                    value= value,
                    value2= value2,
                    value3= value3,
                    value4= value4,
                    value5= value5,
                )
        
        # Finde alle passenden Features (CONTAINS)
        for feature in feature_list:
            if builder_name in feature["key"] or feature["key"] in builder_name:  # ← CONTAINS!
                # l.info(f"Match: '{builder_name}' <-> '{feature['key']}'")
                removestring = "0123456789+-"
                for each in removestring:
                    builder_name = builder_name.replace(each, "")
                # l.info(f"new name {builder_name}")
                generateButtonFrame(

                    name=f"{builder_name}",
                    button_name=builder_name,
                    master=mainFrame,
                    text_color=feature["text_color"],
                    text_name=builder_name,
                    fg_color=feature["color"],
                    location=location,
                    db_entry=False,
                    value= value,
                    value2= value2,
                    value3= value3,
                    value4= value4,
                    value5= value5,
                )
                
def checkMainFrame():
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()
    
    currentLocationList = []
    mainFrameItemLocationList = []
    newFrameDict = {}
    # l.warn("CHECKMAINFRAME STARTET")
    
    content = Builder.select()
    # l.info(f"Content: {content}")
    
    for entry in content:
        combined_name = entry.feature
        feature = entry.name
        location = entry.location
        value = entry.value
        
        
        currentLocationList.append({
            "key": combined_name,
            "feature": feature,
            "location": location,
            "value": value
        })
        

    
    for each in mainFrameElements:
        try:
            # l.info(f"each: {each}")
            if isinstance(each, (ctk.CTkFrame)):
                
                for currentLocationItem in currentLocationList:
                    name = currentLocationItem["key"]
                    feature = currentLocationItem["feature"]
                    location = currentLocationItem["location"]
                    locationWidget = getGuiElement(f"{name}")
                    amountWidget = getGuiElement(f"{location}amount_entry{feature}")
                    
                    amount_value = 0
                    if not locationWidget:
                        continue
                    if amountWidget:
                        amount_value = amountWidget.get()
                        qry = Builder.update({Builder.value:amount_value}).where(Builder.feature == name)
                        qry.execute()
                        l.info(f"[AMOUNT FUNCTION]: CHANGE DECTED: {name} on {location} has now a amount of {amount_value}")
                        

                    location_value = locationWidget.get()

                    
                    mainFrameItemLocationList.append({
                        "key": name,
                        "now_location": location,
                        "desired_location": location_value,
                        "value": amount_value
                    })

        except Exception as e:
            l.warn(f"ERROR DURING MAINFRAME LIST CREATION: {e}")
            

    
    
    
    for dbBuilder in currentLocationList:
        dbName = dbBuilder["key"]
        dbLocation = dbBuilder["location"]
        raw_name = dbBuilder["feature"]
        value = dbBuilder["value"]
        
        for inMainFrame in mainFrameItemLocationList:
            db_name_in_main_frame= inMainFrame["key"]
            db_item_in_main_frame_location = inMainFrame["now_location"]
            desired_location = inMainFrame["desired_location"]
            
        

            if dbName == db_name_in_main_frame:
                # l.info("DB Name Matches Name in Script")
                
                if dbLocation == desired_location:
                    # l.info("Skipping Element no Change")
                    continue
                
                elif dbLocation is not desired_location:
                    # l.info(f"Changing Db Entry for {dbName} [old location: {dbLocation} / {db_item_in_main_frame_location}] | new Location: {desired_location}")
                    
                    
                    getItemOnNewLocation = Builder.select().where(Builder.location == desired_location)
                    for each in getItemOnNewLocation:
                        switch_to = each.location
                        featureRawNameOnNewLocation = each.name
                        elementOnNewLocationCombinedName = each.feature
                        # l.info(f"Switch location {switch_to} and name: {featureRawNameOnNewLocation} | Combined Name: {elementOnNewLocationCombinedName}")
                        
                        
                        
                        # l.info(f"[Element {dbName}  Raw: {raw_name} Location: {db_item_in_main_frame_location}] tauscht mit [{featureRawNameOnNewLocation} | {elementOnNewLocationCombinedName} Location: {switch_to}] ---> [{featureRawNameOnNewLocation} | {elementOnNewLocationCombinedName}new Location: {dbLocation}]   <|> {dbName}  {raw_name} new Location: {desired_location}")

                        newFrameDict[dbName] = {
                            "changing_db_name": dbName,
                            "changing_raw_name": raw_name,
                            "changing_currentLocation": db_item_in_main_frame_location,
                            "changing_new_location": desired_location,

                            "changeWithElement": {
                                "info": "Auf der Location befindet Sich: ",
                                "switched_db_name": elementOnNewLocationCombinedName,
                                "switched_raw_name": featureRawNameOnNewLocation,
                                
                                "switched_current_location": switch_to,
                                "switched_changing_new_location": desired_location,
                                "switched_new_location": db_item_in_main_frame_location
                            }
                        }
    # l.info(f"{newFrameDict} ist das neue Dict")
    
    # NOTE: FINAL COMPARE LOOP AND DATABASE ENTRY CHANGE
    for compare in content:
        combined_name = compare.feature
        feature = compare.name
        location = compare.location
        value = compare.value
        
        for key in newFrameDict:
            
            
            # l.info(f"EACH KEY {key} and EACH COMBINED NAME: {combined_name}")
            
            if key == combined_name:
                result = newFrameDict.get(key)
                
                changingDbItemName = result["changing_db_name"]
                changingFeatureName = result["changing_raw_name"]
                changingCurrentLocation = result["changing_currentLocation"]
                changingNewLocation = result["changing_new_location"]

                l.info("SINGLE ______________________________")
                l.info("changingDbItemName: %s", changingDbItemName)
                l.info("changingFeatureName: %s", changingFeatureName)
                l.info("changingCurrentLocation: %s", changingCurrentLocation)
                l.info("changingNewLocation: %s", changingNewLocation)
                
                switchWith = result["changeWithElement"]
                l.info("#########################################")
                
                # l.info(f"ALL SWITCH WITH ELEMENTS: {switchWith}")
                
                switchingDbItemName = switchWith["switched_db_name"]
                switchingFeatureName = switchWith["switched_raw_name"]
                switchingCurrentLocation = switchWith["switched_current_location"]
                switchingNewLocation = switchWith["switched_new_location"]
                
                # l.info("ALL ELEMENTS: ")
                l.info(f"switchingDbItemName: {switchingDbItemName}\n"
                    f"switchingFeatureName: {switchingFeatureName}\n"
                    f"switchingCurrentLocation: {switchingCurrentLocation}\n"
                    f"switchingNewLocation: {switchingNewLocation}")
                l.info("SINGLE END ______________________________")



                l.info(f"ELEMENT: {changingDbItemName} von {changingCurrentLocation} will mit {switchingDbItemName} auf {switchingCurrentLocation} die Plätze Tauschen")
                l.info(f"ELEMENT {changingDbItemName} wird dann auf {switchingCurrentLocation} sein und {switchingDbItemName} wird dann auf {changingCurrentLocation} sein")


                dataBaseOverwrite = [
                    Builder.update({Builder.location: switchingCurrentLocation, Builder.feature: f"{switchingCurrentLocation}+{changingFeatureName}", Builder.value: value}).where(Builder.feature == changingDbItemName),
                    Builder.update({Builder.location: changingCurrentLocation, Builder.feature: f"{changingCurrentLocation}+{switchingFeatureName}", Builder.value: value}).where(Builder.feature == switchingDbItemName)
                ]

                for function in dataBaseOverwrite:
                    l.info(f"FUNCTION SQL: {function}")
                    function.execute()
                # qry2.execute()
        
    

    
def destroyMainFrame():
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()
    for each in mainFrameElements:
        each.destroy()
        
    

    

    
def reloadBuilderContent():
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()

    


    checkMainFrame()
    destroyMainFrame()
    rebuildBuilderContent()
                