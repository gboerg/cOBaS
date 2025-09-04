# src/GUI/loader.py
import customtkinter as ctk
from .frames import Frame
from .grid import Grid




def loadGUI(app_instance):
    """Loads all the GUI frames and widgets into the main app instance."""
    Grid.createGrid(app_instance)
    Frame.createFrame01(app_instance)
    Frame.createBackground(app_instance)
    Frame.createObsFrame(app_instance)
    Frame.createInnerFrame(app_instance)