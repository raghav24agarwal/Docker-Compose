import requests

def consume_data():
    url = "http://app-service:5001/"
    res = requests.request("GET", url)

    data = res.json()
    return(data)