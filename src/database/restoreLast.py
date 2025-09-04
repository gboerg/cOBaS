from database import database
import logging as l
import customtkinter as ctk


# from ..GUI.frames
class restore():
    async def checkPreviousValues():
        l.info("Restore Prev vals")
        entry = database.State.get()

        # if entry.record == False:
        #     checkbox_var = ctk.StringVar(value="off") 
        #     self.connectFrame2_checkBox.configure(variable=checkbox_var)
        #     return
        
        # elif entry.record == True:
        #     checkbox_var = ctk.StringVar(value="on") 
        #     self.connectFrame2_checkBox.configure(variable=checkbox_var)
        #     return

    
