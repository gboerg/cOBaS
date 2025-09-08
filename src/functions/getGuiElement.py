# functions/guiElement.py
# Modul zum Speichern und Abrufen von GUI-Elementen.
import logging as l
# Globale Variable, die ein Dictionary sein wird
gui_element_storage = {}


def getGuiElement(name, element=None):
    """
    Diese Funktion speichert ein Element unter einem eindeutigen Namen (Setter)
    oder gibt das gespeicherte Element mit diesem Namen zurück (Getter).
    
    Args:
        name (str): Der eindeutige Name des Elements.
        element (any, optional): Das Element, das gespeichert werden soll.
    """
    global gui_element_storage
    l.warning(f"ELEMENT STORAGE: {gui_element_storage}")
    if element is not None:
        gui_element_storage[name] = element
    return gui_element_storage.get(name)