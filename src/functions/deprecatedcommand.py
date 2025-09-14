import customtkinter as ctk
import logging as l
import logging
from functions.getGuiElement import getGuiElement
from database.database import websockets, Features, Builder






def command_center(event: ctk.CTkButton):
    e_text = event.cget("text")
    e_text_color = event.cget("text_color")
    e_fg_color = event.cget("fg_color")
    fg_color = e_fg_color
    text_color = e_text_color
    
    text = e_text
    text = e_text.strip()
    mainFrame = getGuiElement("main_frame")
    asideFrame = getGuiElement("aside_frame")
    connectFrame =  getGuiElement("connect_frame")
    # getGuiElement("obs_features")
    # getGuiElement("misc_features")
    all_elements = mainFrame.winfo_children()
    # aside_elements = asideFrame.winfo_children()
    # l.info(f"aside elements: {aside_elements}")
    
    websocketsDB = websockets.select()
    featuresDB = Features.select()
    re_create = False
    misc_feature_dict = []
    amount_feature_dict = []
    obs_feature_dict = []
    socket_dict = []
    main_frame_features_dict = []
    main_frame_feature_frame_dict = []    
    main_frame_feature_entry_dict = []  
    for element in all_elements:
        
        try:
            content = ""
            content2 = ""
            if isinstance(element, (ctk.CTkLabel, ctk.CTkButton, ctk.CTkCheckBox, ctk.CTkComboBox, ctk.CTkRadioButton, ctk.CTkLabel)):
                content = element.cget("text")
            elif isinstance(element, (ctk.CTkFrame, ctk.CTkScrollableFrame)):
                content2 = element.winfo_children()

                for each in content2: 
                    # Holen Sie den Text aus Buttons und Labels
                    if isinstance(each, (ctk.CTkButton, ctk.CTkLabel, ctk.CTkCheckBox, ctk.CTkRadioButton)):
                        text_ = each.cget("text")
                        l.info(f"SUBFRAME TEXT: {text}")
                        main_frame_feature_frame_dict.append({"element": text_})
                    # Holen Sie den Wert aus Entry-Feldern
                    elif isinstance(each, ctk.CTkEntry):
                        l.warn(f"{each} ENNNNNNNNNNN")
                        main_frame_feature_entry_dict.append({"entry": each})

            if content: 
                main_frame_features_dict.append({
                    "element": content
                })
                
        except Exception as e: 
            l.warn(f"Error during mainFrame element fetch {e}")
    
    l.info(f"ROOT TEXT: {text}")
    for feature in featuresDB:
        if "obs" in feature.feature:
            new_name = feature.feature.replace("obs_", "")
            obs_feature_dict.append({
                "obs_feature": new_name,
                "allow_once": feature.allow_follow
            })
        elif "()" or () in feature.feature:
            amount_feature_dict.append({
                "amount_feature": feature.feature
            })
        else: 
            misc_feature_dict.append({
                "other_feature": feature.feature
            })
    
    for socket in websocketsDB:
        socket_dict.append({
            "websocket": { 
                "name": socket.name,
                "host": socket.host,
                "port": socket.port
            }
        })


        
    # l.info(f"Button Text: {text} : MISC: [{misc_feature_dict}] | AMOUNT: [{amount_feature_dict}] | OBS: {obs_feature_dict} | SOCKET: [{socket_dict}] MAINFRAME : [{main_frame_features_dict}]")
    if any(text == d.get("element") for d in main_frame_features_dict):

        if event.master is mainFrame: 
            eve = event.cget("text")
            l.info(f"eve: {eve}")
            event.destroy()
                
        elif any(text == d.get('other_feature') for d in misc_feature_dict):
            l.info(f"'{text}' Misc Funktion erkannt ddu")
            misc_function_button = ctk.CTkButton(mainFrame, text=f"{text}", fg_color=fg_color, text_color=text_color)
            misc_function_button.configure(command= lambda btn = misc_function_button: command_center(btn) )
            misc_function_button.pack(pady=(5,5))
        elif any(text == d.get('obs_feature') for d in obs_feature_dict):
            for d in obs_feature_dict:
                if d.get('obs_feature') == text:
                    # # Wenn 'allow_once' 1 ist, soll kein weiteres Element erstellt werden
                    # if d.get("allow_once") == 0:
                    #     l.info("no follow ups allowed - creating no further element")
                    #     # Mit 'break' beenden wir die Schleife und gehen nicht weiter
                    #     break
                    # else:
                        # 'allow_once' ist nicht 1, also erstellen wir den Button
                    obs_function_button = ctk.CTkButton(mainFrame, text=f"{text}", fg_color=fg_color, text_color=text_color)
                    obs_function_button.configure(command= lambda btn = obs_function_button: command_center(btn) )
                    obs_function_button.pack(pady=(5,5))
                    # Auch hier beenden wir die Schleife, da wir das Element gefunden haben
                    break
        
                
    elif any(text == d.get("element") for d in main_frame_feature_frame_dict):
        # TODO
        if event.master.master == mainFrame:
            event.master.destroy()
        else:
            
            
            
            
            
            if any(text == d.get('amount_feature') for d in amount_feature_dict):
                l.info(f"'{text}' Amount Funktion erkannt.")
                if "amount" in text: 
                    placeholder = "amount"
                if "times" in text:
                    placeholder ="times"
                amount_frame = ctk.CTkFrame(mainFrame)
                amount_entry = ctk.CTkEntry(amount_frame, placeholder_text=placeholder)
                
                amount_frame.pack(pady=(5,5))
                amount_entry.pack(side="right", padx=(5,5))
                
                amount_button = ctk.CTkButton(amount_frame, text=f"{text}", fg_color=fg_color, text_color=text_color)
                amount_button.pack(side="left", padx=(5,5))
                amount_button.configure( command= lambda btn = amount_button: command_center(btn) )
            
            elif any(text == d.get('other_feature') for d in misc_feature_dict):
                l.info(f"'{text}' Misc Funktion erkannt")

                misc_function_button = ctk.CTkButton(mainFrame, text=f"{text}", fg_color=fg_color, text_color=text_color)
                misc_function_button.configure(command= lambda btn = misc_function_button: command_center(btn) )
                misc_function_button.pack(pady=(5,5))
                
            elif any(text == d.get('obs_feature') for d in obs_feature_dict):
                l.info(f"'{text}' Obs Funktion erkannt ")
                if "switch" in text:
                    l.warn("Switch DROP DOWN CREATING NEW FRAME")
                    obs_switch_frame = ctk.CTkFrame(mainFrame)
                    obs_switch_frame.pack(pady=(5,5 ))

                    obs_switch_button = ctk.CTkButton(obs_switch_frame, text=f"{text}", fg_color=fg_color, text_color=text_color)
                    obs_switch_button.configure(command= lambda btn = obs_switch_button: command_center(btn) )
                    obs_switch_button.pack(side="left", padx=(5, 5))

                    obs_switch_from_label = ctk.CTkLabel(obs_switch_frame, text="Switch from: ")
                    obs_switch_from_label.pack(side="left")
                    
                    obs_switch_to_label = ctk.CTkLabel(obs_switch_frame, text="to ")
                    obs_switch_to_label.pack(side="left")
                    
                    obs_switch_from = ctk.CTkComboBox(obs_switch_frame, values=["CurrentScene"])
                    obs_switch_from.pack(side="left", padx=(5, 5))
                    
                    
                    obs_switch_to = ctk.CTkComboBox(obs_switch_frame, values=["Szene 1", "Szene2", "Stream"])
                    obs_switch_to.pack(side="left", padx=(5, 5))
                    # Pack the widgets in the desired order
                    
                else:   
                    obs_function_button = ctk.CTkButton(mainFrame, text=f"{text}", fg_color=fg_color, text_color=text_color)
                    obs_function_button.configure(command= lambda btn = obs_function_button: command_center(btn) )
                    obs_function_button.pack(pady=(5,5))
                    
            elif any(text == d['websocket']['name'] or d['websocket']['host'] or d['websocket']['port'] for d in socket_dict):
                l.info(f"'{text}'WebSocket Erkannt")
    else: 
        # Logik für die If/Elif-Anweisungen
        

            
        if any(text is not d.get("elements") for d in main_frame_features_dict):
            l.info("FIRST CHECK FAILED NOT SOCKET ")

        
        if any(text == d.get('amount_feature') for d in amount_feature_dict):
            l.info(f"'{text}' Amount Funktion erkannt.")
            if "amount" in text: 
                placeholder = "amount"
            if "times" in text:
                placeholder ="times"
            amount_frame = ctk.CTkFrame(mainFrame)
            amount_entry = ctk.CTkEntry(amount_frame, placeholder_text=placeholder)
            amount_frame.pack(pady=(5,5))
            amount_entry.pack(side="right", padx=(5,5))
            
            amount_button = ctk.CTkButton(amount_frame, text=f"{text}", fg_color=fg_color, text_color=text_color)
            amount_button.pack(side="left", padx=(5,5))
            amount_button.configure( command= lambda btn = amount_button: command_center(btn) )
            
        elif any(text == d.get('other_feature') for d in misc_feature_dict):
            l.info(f"'{text}' Misc Funktion erkannt1")
            
            

            misc_function_button = ctk.CTkButton(mainFrame, text=f"{text}", fg_color=fg_color, text_color=text_color)
            misc_function_button.configure(command= lambda btn = misc_function_button: command_center(btn) )
            misc_function_button.pack(pady=(5,5))
            
        elif any(text == d.get('obs_feature') for d in obs_feature_dict):
            l.info(f"'{text}' Obs Funktion erkannt")
            if "switch" in text:
                l.warn("Switch DROP DOWN CREATING NEW FRAME")
                obs_switch_frame = ctk.CTkFrame(mainFrame)
                obs_switch_frame.pack(pady=(5,5 ))

                obs_switch_button = ctk.CTkButton(obs_switch_frame, text=f"{text}", fg_color=fg_color, text_color=text_color)
                obs_switch_button.configure(command= lambda btn = obs_switch_button: command_center(btn) )

                obs_switch_from_label = ctk.CTkLabel(obs_switch_frame, text="Switch from: ")
                obs_switch_to_label = ctk.CTkLabel(obs_switch_frame, text="to ")
                
                obs_switch_from = ctk.CTkComboBox(obs_switch_frame, values=["CurrentScene"])
                obs_switch_to = ctk.CTkComboBox(obs_switch_frame, values=["Szene 1", "Szene2", "Stream"])
                obs_switch_button.pack(side="left", padx=(5, 5))
                # Pack the widgets in the desired order
                obs_switch_from_label.pack(side="left")
                obs_switch_from.pack(side="left", padx=(5, 5))
                obs_switch_to_label.pack(side="left")
                obs_switch_to.pack(side="left", padx=(5, 5))
            else: 
                obs_function_button = ctk.CTkButton(mainFrame, text=f"{text}", fg_color=fg_color, text_color=text_color)
                obs_function_button.configure(command= lambda btn = obs_function_button: command_center(btn) )
                obs_function_button.pack(pady=(5,5))
            
            
        elif any(text == d['websocket']['name'] or d['websocket']['host'] or d['websocket']['port'] for d in socket_dict):
            l.info(f"'{text}'WebSocket Erkannt")

            # Der Text, den der Button haben würde, wird im Vorfeld festgelegt.
            # So kann er mit den Werten im Dictionary verglichen werden.
            socket_button_text = f"WebSocket: {text},"

            # Prüfen, ob der Socket-Text bereits im Dictionary-Element 'element' existiert.
            # Hier wird eine List Comprehension verwendet, um die Überprüfung zu vereinfachen und zu beschleunigen.
            if not any(d['element'] == socket_button_text for d in main_frame_features_dict):
                # Wenn der WebSocket noch nicht da ist, wird der Button erstellt.
                websocket_button = ctk.CTkButton(mainFrame, text=socket_button_text, fg_color=fg_color, text_color=text_color)
                websocket_button.configure(command=lambda btn=websocket_button: command_center(btn))
                websocket_button.pack(pady=(5, 5))

                # Füge den neuen Eintrag zur Liste hinzu.
                main_frame_features_dict.append({
                    "element": socket_button_text
                })
                l.info(f"Socket text: {socket_button_text} | NEW FRAME DICT: {main_frame_features_dict}")
            else:
                # Wenn der WebSocket bereits existiert, wird nichts getan.
                l.info(f"Socket '{socket_button_text}' existiert bereits und wird nicht erneut hinzugefügt.")