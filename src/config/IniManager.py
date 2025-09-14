import configparser

def generateConfig():
    config = configparser.ConfigParser()
    # NOTE: MAINCAT
    config['cOBaS'] = {'user_name' : 'user'}
    config['WebSocket'] = {}
    config['OBS'] = {}
    config['MISC']= {}

    # NOTE: SUBCAT
    config['WebSocket.Colors'] = {}
    config['OBS.Colors']= {} 
    config['MISC.Colors'] = {}
    

    # NOTE: FILL SUB CAT
    config['WebSocket.Colors']['default_websocket_color'] = 'red'
    config['WebSocket.Colors']['default_websocket_text_color'] = 'black'


    config['OBS.Colors']['obs_function_default_color'] = 'blue'
    config['OBS.Colors']['obs_function_text_default_color'] = 'white'


    config['MISC.Colors']['misc_function_default_color'] = 'green'
    config['MISC.Colors']['misc_function_text_default_color'] = 'white'

    

    
    with open('src/config/config.ini', 'w') as configfile:
        config.write(configfile)

# generateConfig()