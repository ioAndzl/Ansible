import requests

if __name__=="__main__":
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.content)