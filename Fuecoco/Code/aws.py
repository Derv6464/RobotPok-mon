import requests
import json

def read_json(dataType):
    with open("network.json") as f:
        data = json.load(f)
    return data[dataType]

def checkNetworkInfo():
    current = read_json("current")
    r = requests.get('your_aws_api.com/Prod/wifiInfo', headers={"id":"0"})
    response = r.json()
    if response["ssid"] == current["ssid"] and response["password"] == current["password"]:
        return True
    return False

def checkIP(ip):
    current = read_json("current")
    if ip == current["ip"]:
        return True
    return False
    
def getNetworkInfo():
    current = read_json("current")
    r = requests.get('your_aws_api.com/Prod/wifiInfo', headers={"id":"0"})
    response = r.json()
    return {'ssid' : response["ssid"], 'password' : response["password"], 'ip' : current['ip'], 'port' : current['port']}

def writeNew():
    if not checkNetworkInfo():
        current = read_json("current")
        new = getNetworkInfo()
        print(new)
        networkInfo = {"current" : new , "backup" : current}
    
        with open('network.json', 'w') as f:
            json.dump(networkInfo, f)
        return True

    return False


def pushIP(ip):
    if not checkIP(ip):
        r = requests.patch('your_aws_api.com/Prod/wifiInfo', headers={"id":"0", "ip":ip})
        print(r.text)
        
        current = read_json("current")
        backup = read_json("backup")
        new = {'ssid' : current["ssid"], 'password' : current["password"], 'ip' : ip, 'port' : current['port']}
        print(new)
        networkInfo = {"current" : new , "backup" : backup}
    
        with open('network.json', 'w') as f:
            json.dump(networkInfo, f)
        return True
    