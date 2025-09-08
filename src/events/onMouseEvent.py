import logging as l
import customtkinter as ctk
from functions.getGuiElement import getGuiElement

def onDrag(event):
    widget = event.widget

    text = widget.cget("text")
    print(f"Das Widget '{text}' wird bewegt.")

    new_element = getGuiElement("main_frame")

    newLabel = ctk.CTkLabel(new_element, text=f"{text}", fg_color="blue", corner_radius=5, text_color="white")
    newLabel.pack(anchor="w")
    

    




