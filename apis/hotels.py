import os
from dotenv import load_dotenv
import requests
import json
from langchain.tools import tool

load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")
RAPID_API_HOST = os.getenv("RAPID_API_HOST")

headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }

hotel_destination_data = {
  "status": True,
  "message": "Success",
  "timestamp": 1698310086738,
  "data": [
    {
      "dest_type": "district",
      "cc1": "us",
      "city_name": "New York",
      "label": "Manhattan, New York, New York State, United States",
      "longitude": -73.970894,
      "latitude": 40.776115,
      "type": "di",
      "region": "New York State",
      "city_ufi": 20088325,
      "name": "Manhattan",
      "roundtrip": "GgEwIAAoATICZW46A21hbkAASgBQAA==",
      "country": "United States",
      "image_url": "https://cf.bstatic.com/xdata/images/district/150x150/37931.jpg?k=aaab7e2d310b7db8e7ea0752b451880c93d664bb538331f843810ce6f1a37a82&o=",
      "dest_id": "929",
      "nr_hotels": 568,
      "lc": "en",
      "hotels": 568
    },
    {
      "dest_id": "-2437894",
      "nr_hotels": 4798,
      "country": "Philippines",
      "image_url": "https://cf.bstatic.com/xdata/images/city/150x150/685726.jpg?k=25b602b90c38b13fe9e858b62a9bbd3c773bf459b16e84b26642a8a056c9f524&o=",
      "hotels": 4798,
      "lc": "en",
      "city_ufi": None,
      "type": "ci",
      "region": "Luzon",
      "roundtrip": "GgEwIAEoATICZW46A21hbkAASgBQAA==",
      "name": "Manila",
      "longitude": 120.98368,
      "latitude": 14.5967655,
      "cc1": "ph",
      "dest_type": "city",
      "label": "Manila, Luzon, Philippines",
      "city_name": "Manila"
    },
    {
      "label": "Manchester, New Hampshire, United States",
      "city_name": "Manchester",
      "cc1": "us",
      "dest_type": "city",
      "latitude": 42.9956,
      "longitude": -71.4553,
      "roundtrip": "GgEwIAIoATICZW46A21hbkAASgBQAA==",
      "name": "Manchester",
      "city_ufi": None,
      "type": "ci",
      "region": "New Hampshire",
      "hotels": 21,
      "lc": "en",
      "nr_hotels": 21,
      "dest_id": "20079942",
      "country": "United States",
      "image_url": "https://cf.bstatic.com/xdata/images/city/150x150/957300.jpg?k=6c15d9e11351e7f2206489fdfa50308dc8f248aec7c3f378e73ea5cab182a5f6&o="
    },
    {
      "cc1": "gb",
      "dest_type": "city",
      "label": "Manchester, Greater Manchester, United Kingdom",
      "city_name": "Manchester",
      "longitude": -2.23615,
      "latitude": 53.4812,
      "city_ufi": None,
      "region": "Greater Manchester",
      "type": "ci",
      "roundtrip": "GgEwIAMoATICZW46A21hbkAASgBQAA==",
      "name": "Manchester",
      "dest_id": "-2602512",
      "nr_hotels": 1087,
      "image_url": "https://cf.bstatic.com/xdata/images/city/150x150/976977.jpg?k=8d13c94917fa00569d115c9123c7b5789ad41f7383b6fad32a1bda8e215e8936&o=",
      "country": "United Kingdom",
      "hotels": 1087,
      "lc": "en"
    },
    {
      "hotels": 208,
      "lc": "en",
      "nr_hotels": 208,
      "dest_id": "1077",
      "image_url": "https://cf.bstatic.com/xdata/images/district/150x150/56351.jpg?k=81acc465a1c7b3a58b068901ae18dd157da72b472a9753515b9801dfa1c1f832&o=",
      "country": "United Kingdom",
      "roundtrip": "GgEwIAQoATICZW46A21hbkAASgBQAA==",
      "name": "Manchester City Centre",
      "city_ufi": -2602512,
      "region": "Greater Manchester",
      "type": "di",
      "latitude": 53.47925,
      "longitude": -2.241755,
      "label": "Manchester City Centre, Manchester, Greater Manchester, United Kingdom",
      "city_name": "Manchester",
      "cc1": "gb",
      "dest_type": "district"
    }
  ]
}

hotels_data = {'status': True, 'message': 'Success', 'timestamp': 1715315918913, 'data': {'hotels': [{'hotel_id': 11740607, 'accessibilityLabel': 'Super Collection O Kalyan West.\n3 out of 5 stars.\n9.1 Wonderful 17 reviews.\n\u200e31 km from center\u202c.\n Hotel room : 1\xa0bed.\nOriginal price 11663 INR. Current price 5715 INR..\n+839 INR taxes and charges.\nFree cancellation.\nNo prepayment needed.', 'property': {'latitude': 19.235956, 'checkin': {'untilTime': '00:00', 'fromTime': '12:00'}, 'isPreferred': True, 'optOutFromGalleryChanges': 1, 'blockIds': ['1174060702_389987094_3_0_0'], 'reviewCount': 17, 'name': 'Super Collection O Kalyan West', 'position': 0, 'reviewScore': 9.1, 'mainPhotoId': 544045594, 'rankingPosition': 0, 'id': 11740607, 'checkinDate': '2024-09-16', 'checkoutDate': '2024-09-19', 'reviewScoreWord': 'Wonderful', 'countryCode': 'in', 'qualityClass': 0, 'photoUrls': ['https://cf.bstatic.com/xdata/images/hotel/square60/544045594.jpg?k=ada9a97918d0c43724216e4d52133e20bac3b3bdc3163af5631cd7594839f70a&o='], 'checkout': {'fromTime': '00:00', 'untilTime': '11:00'}, 'longitude': 73.11965, 'wishlistName': 'Mumbai', 'isFirstPage': True, 'currency': 'INR', 'propertyClass': 3, 'accuratePropertyClass': 3, 'ufi': -2092174, 'priceBreakdown': {'benefitBadges': [{'text': 'Getaway Deal', 'explanation': 'Getaway Deal', 'variant': 'constructive', 'identifier': 'Getaway 2021 Deals'}], 'taxExceptions': [], 'strikethroughPrice': {'currency': 'INR', 'value': 11662.5}, 'grossPrice': {'value': 5714.63, 'currency': 'INR'}, 'excludedPrice': {'currency': 'INR', 'value': 838.755584672168}}}}, {'hotel_id': 10684742, 'accessibilityLabel': 'Arts International.\n3 out of 5 for property rating.\n7.5 Good 405 reviews.\n\u200eSantacruz\u202c • \u200e4.5 km from center\u202c\n\u200e1 km from beach\u202c\n\u200eThis property has cribs available\u202c.\n Private room : 1\xa0bed.\nOriginal price 9900 INR. Current price 8415 INR..\n+1010 INR taxes and charges.\nFree cancellation.', 'property': {'ufi': -2092174, 'priceBreakdown': {'benefitBadges': [{'identifier': 'Mobile Rate', 'variant': 'constructive', 'explanation': 'Mobile-only price', 'text': 'Mobile-only price'}], 'taxExceptions': [], 'strikethroughPrice': {'currency': 'INR', 'value': 9900}, 'excludedPrice': {'currency': 'INR', 'value': 1009.79997742921}, 'grossPrice': {'currency': 'INR', 'value': 8415}}, 'photoUrls': ['https://cf.bstatic.com/xdata/images/hotel/square60/489416079.jpg?k=5451d14fec77b36a51d80c2ccd1b118827b93676f263db0abb781e82554bdfcf&o='], 'checkout': {'untilTime': '11:00', 'fromTime': '11:00'}, 'longitude': 72.8361314, 'wishlistName': 'Mumbai', 'isFirstPage': True, 'propertyClass': 0, 'currency': 'INR', 'accuratePropertyClass': 0, 'checkoutDate': '2024-09-19', 'reviewScoreWord': 'Good', 'countryCode': 'in', 'qualityClass': 3, 'position': 1, 'reviewScore': 7.5, 'rankingPosition': 1, 'id': 10684742, 'mainPhotoId': 489416079, 'checkinDate': '2024-09-16', 'name': 'Arts International', 'blockIds': ['1068474201_383079883_3_2_0'], 'reviewCount': 405, 'checkin': {'untilTime': '12:00', 'fromTime': '12:00'}, 'optOutFromGalleryChanges': 0, 'isPreferred': True, 'latitude': 19.0862384}}, {'hotel_id': 266426, 'accessibilityLabel': 'Bloom Hotel - Juhu.\n4 out of 5 stars.\n7.4 Good 781 reviews.\n\u200eJuhu\u202c • \u200e6 km from center\u202c\n\u200e100 m from beach\u202c.\n Hotel room : 1\xa0bed.\n18960 INR.\n+2275 INR taxes and charges.\nFree cancellation.', 'property': {'checkin': {'untilTime': '00:00', 'fromTime': '14:00'}, 'optOutFromGalleryChanges': 0, 'isPreferred': True, 'latitude': 19.0894544731556, 'name': 'Bloom Hotel - Juhu', 'blockIds': ['26642604_367744574_2_42_0'], 'reviewCount': 781, 'checkoutDate': '2024-09-19', 'reviewScoreWord': 'Good', 'qualityClass': 0, 'countryCode': 'in', 'position': 2, 'reviewScore': 7.4, 'rankingPosition': 2, 'id': 266426, 'mainPhotoId': 312794371, 'checkinDate': '2024-09-16', 'priceBreakdown': {'grossPrice': {'value': 18960, 'currency': 'INR'}, 'excludedPrice': {'currency': 'INR', 'value': 2275.19994914532}, 'benefitBadges': [], 'taxExceptions': []}, 'ufi': -2092174, 'checkout': {'fromTime': '00:00', 'untilTime': '11:00'}, 'photoUrls': ['https://cf.bstatic.com/xdata/images/hotel/square60/312794371.jpg?k=d7d7b3dcc9a972039c3b3944ee625d71e0f1fcaf2d8a90bf35e5bc34caad549b&o='], 'wishlistName': 'Mumbai', 'isFirstPage': True, 'longitude': 72.8276100754738, 'accuratePropertyClass': 4, 'currency': 'INR', 'propertyClass': 4}}]}}

@tool
def get_hotel_destination(location):
    "Get the destination ID and city name for a location."
    
    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
    
    querystring = {"query":location}
    #response = requests.get(url, headers=headers, params=querystring, timeout=10)
    response = hotel_destination_data
    dest_id = response['data'][0]['dest_id']
    dest_type = response['data'][0]['dest_type']
    return dest_id, dest_type

@tool
def get_hotels(location):
    "Get the hotels for a location."
    
    dest_id, dest_type = get_hotel_destination(location)
    
    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"
    
    querystring = {
        "dest_id":dest_id,
        "search_type":dest_type,
        "arrival_date":"2024-09-16",
        "departure_date":"2024-09-19",
        "adults":"1",
        "children_age":"0,17",
        "room_qty":"1",
        "page_number":"1",
        "languagecode":"en-us",
        "currency_code":"INR"
    }
    
    #response = requests.get(url, headers=headers, params=querystring, timeout=10)
    
    response = hotels_data
    return response