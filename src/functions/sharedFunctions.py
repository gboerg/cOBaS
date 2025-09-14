from database.database import Builder, Features, websockets
from functions.getGuiElement import getGuiElement
from interaction.commandCenter import generateButtonFrame
import logging as l
import customtkinter as ctk

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
    
def crossfunction():
    reloadBuilderContent()
    
def destroyMainFrame():
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()
    for each in mainFrameElements:
        each.destroy()
        
def checkMainFrame():
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()
    for each in mainFrameElements:
        
        try:
            l.info(f"each: {each}")
            if each:
                l.info(f"Elements detected Resorting: {each}")
                if isinstance(each, (ctk.CTkFrame)):
                    content = Builder.select()
                    l.info(f"Content: {content}")
                    
                    for each in content:
                        feature = each.feature
                        all_name = each.all_name
                        location = each.location
                        l.info(f"entry: {feature}")
                        
                        if "WebSocket" not in feature:
                            r_widget = getGuiElement(f"{feature}")
                            entry = r_widget.get()
                            
                            l.info(f"Widget entry value: {entry}")
                            
                            if entry == "0":
                                l.info("Entry is 0, returning")
                                return
                            
                            if entry:

                                selectprevios_location = Builder.select().where(Builder.location == entry)
                                prev_location=""
                                prev_all_name=""
                                for each in selectprevios_location:
                                    prev_location= each.location
                                    prev_all_name = each.all_name
                                    
                                    
                                    delete = Builder.delete().where(Builder.all_name == all_name)
                                    delete.execute()
                                    delete2 = Builder.delete().where(Builder.all_name == prev_all_name)
                                    delete2.execute()
                                    
                                    dbBuilderEntry(all_name=all_name, feature=feature, content_kwargs="", format_kwargs="", command="", location=entry)
                                    dbBuilderEntry(all_name=prev_all_name, feature=feature, content_kwargs="", format_kwargs="", command="", location=location)
                                
                                    
                                l.info(f"Entry: {all_name} changes place with {prev_all_name} | {all_name} is now on {prev_location} and {prev_all_name} is{entry}")
                                l.info("after")
                                return
  
                # 
                return

        except Exception as e:
            l.info(f"error {e}")
      
def reloadBuilderContent():
    mainFrame = getGuiElement("main_frame")
    mainFrameElements = mainFrame.winfo_children()

    websocket_list = []
    builder_list = []
    feature_list = []
    


    checkMainFrame()
    destroyMainFrame()
    
    
    # Alle Daten als Listen sammeln
    for socket in websockets.select():
        websocket_list.append({
            "key": socket.all_field,
            "color": socket.color,
            "text_color": socket.text_color
        })
    
    for script in Builder.select():
        builder_list.append({
            "key": script.feature,
            "location": script.location,
            "content_kwargs": script.content_kwargs
        })
    
    for feature in Features.select():
        feature_list.append({
            "key": feature.feature,
            "color": feature.feature_color,
            "text_color": feature.feature_text_color
        })
        
        
        

    
    # Für jeden Builder einen Button erstellen
    for builder in builder_list:
        builder_name = builder["key"]
        location = int(builder["location"])
        

        
        # Finde alle passenden WebSockets (CONTAINS)
        for socket in websocket_list:
            if builder_name in socket["key"] or socket["key"] in builder_name:  # ← CONTAINS!
                l.info(f"Match: '{builder_name}' <-> '{socket['key']}'")
                
                alln = Builder.select().where(Builder.all_name == builder_name)
                name = Builder.select().where(Builder.feature.contains(builder_name))
                
                for each in name:
                    l.info(f"counter check: {each.all_name}")
                    builder_name = each.all_name
                    
                
                generateButtonFrame(
                    all_name=f"{alln}",
                    button_name=builder_name,
                    master=mainFrame,
                    text_color=socket["text_color"],
                    text_name=builder_name,
                    fg_color=socket["color"],
                    location=location,
                    db_entry=False
                )
        
        # Finde alle passenden Features (CONTAINS)
        for feature in feature_list:
            if builder_name in feature["key"] or feature["key"] in builder_name:  # ← CONTAINS!
                l.info(f"Match: '{builder_name}' <-> '{feature['key']}'")
                removestring = "0123456789+-"
                for each in removestring:
                    builder_name = builder_name.replace(each, "")
                l.info(f"new name {builder_name}")
                generateButtonFrame(
                    
                    
                    all_name=f"{builder_name}",
                    button_name=builder_name,
                    master=mainFrame,
                    text_color=feature["text_color"],
                    text_name=builder_name,
                    fg_color=feature["color"],
                    location=location,
                    db_entry=False
                )
    