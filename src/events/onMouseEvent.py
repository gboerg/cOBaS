import customtkinter as ctk
from tkinter import Event
from functions.getGuiElement import getGuiElement
import logging as l
from database.database import Builder



# Globale Maus-Flags
mouse_inside = False
mouser_hover = None

def MouseMotion(event):
    global mouse_inside, mouser_hover
    mouse_inside = True
    mouser_hover = event.widget

def MouseLeave(event):
    global mouse_inside
    mouse_inside = False

def onDrag(event):
    pass

def onDrop(event):
    pass
    # widget = event.widget.master
    # l.warn(f"WIDGET: {event.widget}")
    # l.warn(f"WIDGET: {widget}")
    # get_main_frame = getGuiElement("main_frame")
    # get_content_frame = getGuiElement("content_frame")
    # get_misc_frame = getGuiElement("misc_features")

    # try:
    #     text = widget.cget("text")
    #     fg_color = widget.cget("fg_color")
    #     text_color = widget.cget("text_color")
    # except AttributeError:
    #     text = "Unknown Widget"
    #     fg_color = "red"
    #     text_color = "black"

    # x_root, y_root = event.x_root, event.y_root

    # cx = get_content_frame.winfo_rootx()
    # cy = get_content_frame.winfo_rooty()
    # cw = get_content_frame.winfo_width()
    # ch = get_content_frame.winfo_height()

    # # Die Position des Mausloslassens wird relativ zum main_frame berechnet
    # rel_x = x_root - get_main_frame.winfo_rootx()
    # rel_y = y_root - get_main_frame.winfo_rooty()
    
    # # Der folgende Codeblock wird nur ausgeführt, wenn die Maus im content_frame losgelassen wird.
    # # Die Platzierung der Widgets findet jedoch im main_frame statt.
    # if cx <= x_root <= cx + cw and cy <= y_root <= cy + ch:
        
    #     # Zerstöre das ursprüngliche Widget
    #     if widget.master == get_main_frame:
    #         widget.destroy()

    #     if "(" in text:
    #         # Extrahiere den korrekten Namen
    #         entry_name = text.split('(')[0].strip()

    #         # Erstelle Label und Entry direkt im main_frame
    #         newLabel = ctk.CTkLabel(get_main_frame,
    #                                 text=text,
    #                                 fg_color=fg_color,
    #                                 corner_radius=5,
    #                                 text_color=text_color)
            
    #         entry_widget = ctk.CTkEntry(get_main_frame, placeholder_text=entry_name)
            
    #         # Positioniere Label und Entry relativ zum main_frame
    #         newLabel.place(x=rel_x, y=rel_y)
    #         entry_widget.place(x=rel_x + newLabel.winfo_width() + 5, y=rel_y)

    #         # Leite das Widget unter seinem korrekten Namen weiter
    #         getGuiElement(entry_name, entry_widget)

    #         # Update idletasks wird benötigt, um die Widget-Größe zu aktualisieren
    #         # und die korrekte Position des Entrys zu berechnen.
    #         newLabel.update_idletasks()

    #         newLabel.bind('<B1-Motion>', onDrag)
    #         newLabel.bind("<ButtonRelease-1>", onDrop)
    #     else:
    #         # Erstelle das neue Label direkt im main_frame
    #         newLabel = ctk.CTkLabel(get_main_frame,
    #                                 text=text,
    #                                 fg_color=fg_color,
    #                                 corner_radius=5,
    #                                 text_color=text_color)
    #         newLabel.place(x=rel_x, y=rel_y)
            
    #         newLabel.bind('<B1-Motion>', onDrag)
    #         newLabel.bind("<ButtonRelease-1>", onDrop)
    # else:
    #     l.warning("ERROR: Maus nicht über content_frame beim Loslassen")

def onMouseButton01(event: Event):
    widget = event.widget
    text = widget.cget("text")
    
    l.warn(f"Linksklick erkannt auf Widget: {widget} and Text: {text}")

def onMouseButton02(event): 
    pass
def onMouseButton03(event):
    pass