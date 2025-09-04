from database import database
from obs.testConnection import testConnection
import logging as l

class Manager():
    async def obsConnect():
        # NOTE: Retrieve the value here when the button is clicked
        host = self.host_entry.get()
        port = self.port_entry.get()
        passw = self.password_entry.get()
        l.info(f"Password entry values: {host}, {port}, {passw}")
        self.button.configure(state="disabled", text="Connecting...")
        test_result, message = await testConnection(host, port, passw)

        l.info(f"Test Result during conn: {test_result}")

        if test_result: 
            self.button.configure(state="enabled", text="Verbunden")

        elif test_result == False: 
            self.button.configure(state="enabled", text="No entry")
        else: self.button.configure(state="enabled", text=f"Fehlgeschlagen: {message}")


        return test_result

    async def toggle_rec():
        host = self.host_entry.get()
        port = self.port_entry.get()
        passw = self.password_entry.get()
        l.info("before rec db")

        try: 
            entry = database.State.get()

            if entry.record == False:
                l.info("db is negativ")
                database.State.update(record=True).where(database.State.record == False).execute()
                l.info(f"updated entry is now {entry.record}")
                # await toggleRecording(host, port, passw)
                return
            
            elif entry.record == True:

                l.info("db is positiv")
                database.State.update(record=False).where(database.State.record == True).execute()
                l.info(f"updated entry is now {entry.record}")
                # await toggleRecording(host, port, passw)
                return
            
        except Exception as e: 
            l.info(f"Error druing toggle Rec db: {e}")

