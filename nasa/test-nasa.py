import requests
import json
from pprint import pprint


url = "https://api.nasa.gov/planetary/apod"
date = "date=2020-03-22"
count = "count=3"
start_date = "start_date=2025-03-17"

def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/.nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "?api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    key = returncreds()
    resp1 = requests.get(url+key+"&"+date)
    resp2 = requests.get(url+key+"&"+count)
    resp3 = requests.get(url+key+"&"+start_date)
    a = resp1.json()
    b = resp2.json()
    c = resp3.json()

    print("birthday url: ", a["url"])

    i=0
    for fotos in b:
        print(f"random url {i+1}: {b[i]['url']}")
        i+=1

    j=0
    for fotos in c:
        print(f"17-19 mars 2025 url {j+1}: {c[j]['url']}")
        j+=1 

if __name__ == "__main__":
    main()
