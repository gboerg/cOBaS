
import logging as l
from functions.getGuiElement import getGuiElement




def recording_checkbox():
    l.warning("Record Function ticked")

def connect():
    l.warning("connect function triggered")
    element = getGuiElement("connect_button")
    l.warning(f" element: {element}")
    if element:
        element.configure(text="Verbunden")
        l.warning("Button konfiguriert.")
    else: 
        l.error("No Element ")

def add_connect():
    l.warning("connect function triggered")
    element = getGuiElement("save_connect_button")
    l.warning(f" element: {element}")
    if element:
        element.configure(text="Hinzugefügt")
        l.warning("Button konfiguriert.")
    else: 
        l.error("No Element ")