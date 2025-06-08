import json
import os
from tinydb import TinyDB, Query

with open("server_config.json",encoding="utf-8") as sc:
    serverConfig = json.load(sc)

serverDatabase = TinyDB('serverDatabase.json')
table = serverDatabase.table("server_config")

Server = Query()

def getDbEntry(serverId: str, search: str):
    properties = serverDatabase.search(Server.id == serverId)
    if properties:
        result = properties[0].get(search)
    else:
        result = "404 - Not Found"
    return result


def updateDbEntry(serverId: str, key: str, value: any):
    serverDatabase.update({key:value}, Server.id == serverId)


def addServerToDb(serverId: str):
    entry = {
        "id": serverId,
        "logChannel": 0,
        "logForwarding": True,
        "onlyForwarding": False,
        "selfLogging": False,
        "logSendingToServerId": []
    }

    serverDatabase.upsert(entry, Server.id == serverId)


def removeServerFromDb(serverId: str):
    serverDatabase.remove(Server.id == serverId)


def convertJsonToDb():
    for key, value in serverConfig.items():
        value["id"] = key
        table.insert(value)

