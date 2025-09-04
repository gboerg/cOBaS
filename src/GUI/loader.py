# src/GUI/loader.py
import customtkinter as ctk
from .frames import Frame
from .grid import Grid
from .checkBox import checkBoxManager
from .buttons import ButtonManager



def loadGUI(app_instance):
    """Loads all the GUI frames and widgets into the main app instance."""

    # BE AWARE : ANY CHANGES TO ORDER WILL BREAK THE GUI

    Grid.createGrid(app_instance)
    Frame.createFrame01(app_instance)
    Frame.createBackground(app_instance)
    ButtonManager.runCurrentSelected(app_instance)
    Frame.createObsFrame(app_instance)
    ButtonManager.obsConnect(app_instance)
    Frame.createInnerFrame(app_instance)
    checkBoxManager.createCheckBoxToggleRecord(app_instance)
    # Frame.createCheckBoxToggleRecord(app_instance)