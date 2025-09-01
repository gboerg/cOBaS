# obs/testConnection.py
import logging as l
import obsws_python as obs
from obsws_python.error import OBSSDKRequestError, OBSSDKError

def testConnection(host: str, port: str, password: str):
    """
    Tests the connection to OBS synchronously. This function will block.
    Returns a tuple (success, message).
    """
    l.info("Attempting to connect to OBS at %s:%s", host, port)
    
    try:
        int_port = int(port)
    except ValueError:
        return False, "Invalid port number. Port must be an integer."

    try:
        # Erstellt den WebSocket-Client
        cl = obs.ReqClient(host=host, port=int_port, password=password, timeout=3)
        l.info("Successfully identified ReqClient with the server.")
        
        # Ruft die Versionsinformationen ab
        stats = cl.get_version()
        obs_version = stats.obs_version

        # ⭐ Hier wird der Profilname abgefragt ⭐

        
        l.info(f"OBS Version: {obs_version}")

        # Rückgabe des konsistenten Tupels (Erfolg, Nachricht)
        message = f"Successfully connected to OBS.\nOBS Version: {obs_version}\n"
        return True, message

    except OBSSDKRequestError as e:
        l.error(f"OBS request failed with code {e.code}: {e}")
        return False, f"Connection failed with an OBS error. Error: {e}"

    except OBSSDKError as e:
        l.error("Connection failed: %s", e)
        return False, f"Connection failed: {e}"
        
    except Exception as e:
        l.error("An unexpected error occurred: %s", e)
        return False, f"An unexpected error occurred: {e}"