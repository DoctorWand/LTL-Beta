import os
import requests
import json
from bot import loggingFromExternal

with open("default_config.json",encoding="utf-8") as dc:
    defaultConfig = json.load(dc)

REPO = "DoctorWand/LogTheLogger"

def gettingUpdateMessage():
    if os.path.exists("update.txt"):
        updateFile = open("update.txt")
    updateFile = updateFile.read().split("\n")
    if updateFile[0][:4] == "None":
        return None
    
def getLatestRelease():
    url = f"https://api.github.com/repos/{REPO}/releases/latest"
    response = requests.get(url)
    if response.ok:
        return response.json()["tag_name"].lstrip("v")
    else:
        loggingFromExternal("error",f"Error occurred while fetching Github release: {response.status_code}")
        return None

def getCurrentVersion():
    return defaultConfig["botVersion"]
