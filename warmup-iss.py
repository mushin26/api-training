#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
from pprint import pprint 
from datetime import datetime
from geopy.geocoders import Nominatim


URL= "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(URL).json()
    pprint(resp)
    
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="geoapp_1.0")    
    #CURRENT LOCATION OF THE ISS:
    #Timestamp: 2021-08-09 14:08:29
    #Lon: -52.7658
    #Lat: 37.1268
    #City/Country: New Delhi, IN
    lon = resp['iss_position']['longitude']
    lat = resp['iss_position']['latitude']
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {datetime.fromtimestamp(resp['timestamp'])}")
    print(f"Lon:  {lon}")
    print(f"Lat: {lat}")
    location = geolocator.reverse((lat,lon), language = 'en')
    print(f"City/Country: {location.address}")

if __name__ == "__main__":
    main()
