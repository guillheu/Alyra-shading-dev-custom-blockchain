import configparser

configFile = "config.ini"

config = configparser.ConfigParser()
config.read(configFile)

def getConfigVar(variable):
    return config['DEFAULT'][variable]
