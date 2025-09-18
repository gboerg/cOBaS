import obsws_python as obs
from obsws_python.error import OBSSDKRequestError, OBSSDKError
from obsws_python.baseclient import ObsClient
from obsws_python.baseclient import websocket # Import the websocket module to catch its exceptions
import logging as l

def testObsWebSocketConnection(host, port, password):
    try:
        # The connection attempt that might fail
        cl = obs.ReqClient(host=host, port=port, password=password, timeout=3)
        get_version = cl.get_version()
        
        toResultString = str(get_version.obs_version)
        string = f"OBS: {toResultString}"
        
        l.info(f"[OBS]: {get_version.obs_version}")
        return string
        
    except websocket._exceptions.WebSocketAddressException as e:
        l.error(f"OBS connection failed: Invalid host or port. Error: {e}")
        # Return a specific value to indicate failure
        return "No Response from OBS"
    
    except Exception as e:
        l.error(f"OBS connection failed: {e}")
        # Return a specific value for other general errors
        return "No Response from OBS"