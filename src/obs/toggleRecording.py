# obs/testConnection.py
import logging as l
import obsws_python as obs
from obsws_python.error import OBSSDKRequestError, OBSSDKError

async def toggleRecording(host: str, port: int, password: str):
    """
    Tests the connection to OBS synchronously. This function will block.
    Returns a tuple (success, message).
    """
    l.info("Attempting to connect to OBS at %s:%s", host, port)
    l.info("OBS TOGGLE REC", host, port)
    try:
        # Erstellt den WebSocket-Client
        cl = obs.ReqClient(host=host, port=port, password=password, timeout=3)
        l.info("Successfully identified ReqClient with the server.")
        
        # Ruft die Versionsinformationen ab
        test = cl.toggle_record()
        l.info(f"{test} result of toggleRec")


    except OBSSDKRequestError as e:
        l.error(f"OBS request failed with code {e.code}: {e}")
        return False, f"Connection failed with an OBS error. Error: {e}"

    except OBSSDKError as e:
        l.error("Connection failed: %s", e)
        return False, f"Connection failed: {e}"
        
    except Exception as e:
        l.error("An unexpected error occurred: %s", e)
        return False, f"An unexpected error occurred: {e}"