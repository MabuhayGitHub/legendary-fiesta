import requests

def getLocation(ip):
    url = "http://ip-api.com/json/" + ip
    response = requests.get(url)
    return response.json()
