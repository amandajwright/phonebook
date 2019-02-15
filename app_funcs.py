# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:22:06 2019

@author: amand
"""

import sqlite3
import os
import json
import requests
from math import *

def check_db(db_path):
    if os.path.exists(db_path):
        return True
    else:
        return False
    
def get_db():
    try:
        conn = sqlite3.connect("phonebook.db")
        c = conn.cursor()
        return conn, c
    except:
        return None

def get_data_from_db(query, search_term):
    try:
        conn, c = get_db()
        c.execute(query, (search_term,))
        return c.fetchall()
    except:
        return None
        
def get_person_data(surname):
    person_data = get_data_from_db("SELECT * FROM person WHERE surname = ?", surname.title())
    return person_data

def get_businessName_data(businessName):
    businessName_data = get_data_from_db("SELECT * FROM business WHERE business_name = ?", businessName.title())
    return businessName_data

def get_businessCategory_data(businessCategory):
    businessCategory_data = get_data_from_db("SELECT * FROM business WHERE business_category = ?", businessCategory.title())
    return businessCategory_data

def postcode_validation(postcode):
    if ' ' not in postcode:
        return False
    elif ' ' in postcode:
        return True
    else:
        return 'postcode error of unknown description'

def get_postcode_location_from_db(postcode):
    location_of_postcode = get_data_from_db("SELECT * FROM coordinate_mapping WHERE postcode = ?", postcode)
    return location_of_postcode

def get_postcode_location_from_api(postcode):
    if " " not in postcode:
        spaceless_postcode = postcode
    else:
        separated_postcode = postcode.split()
        spaceless_postcode = separated_postcode[0] + separated_postcode[1]
    endpoint = "https://api.postcodes.io/postcodes/"
    postcode_response = requests.get(endpoint + spaceless_postcode)
    data_postcode = postcode_response.json()
    if data_postcode["status"] == 200:
            lat = data_postcode["result"]["latitude"]
            long = data_postcode["result"]["longitude"]
            postcode = data_postcode["result"]["postcode"]
            location_of_postcode = [(postcode, lat, long)]
            return location_of_postcode
    else:
        return "Postcode not recognised."

def person_search_results(surname, postcode):
     person_result = get_person_data(surname)
     if len(person_result) == 0:
         return "Sorry, your search produced no results."
     else:
         person_results_list = []
         for each_person in person_result:
             person_dict = {}
             person_dict["surname"] = each_person[0]
             person_dict["first_name"] = each_person[1]
             person_dict["street"] = each_person[2]
             person_dict["town"] = each_person[3]
             person_dict["postcode"] = each_person[5]
             person_dict["tel_number"] = each_person[6]
             if postcode == "":
                 person_dict["distance"] = ""
             elif calculate_distance(postcode, each_person[5]) == "no result":
                 return "Sorry, this phonebook does not cover that area. Please try another postcode - here are your options: WC2H 0AE, BS41 8JF & NE46 1AB :)."
             else:
                 person_dict["distance"] = calculate_distance(postcode, each_person[5])
             person_results_list.append(person_dict)
         return sort_by_distance(person_results_list)

def business_search_results(business_name_or_category, postcode, business_search_type):
    if business_search_type == "name":
        business_result = get_businessName_data(business_name_or_category)
    elif business_search_type == "category":
        business_result = get_businessCategory_data(business_name_or_category)
    else:
        return "Sorry, error"
    if len(business_result) == 0:
        return "Sorry, your search produced no results."
    else:
        business_results_list = []
        for each_business in business_result:
            business_dict = {}
            business_dict["name"] = each_business[0]
            business_dict["category"] = each_business[1]
            business_dict["street"] = each_business[2]
            business_dict["town"] = each_business[3]
            business_dict["postcode"] = each_business[5]
            business_dict["tel_number"] = each_business[6]
            if postcode == "":
                business_dict["distance"] = ""
            elif calculate_distance(postcode, each_business[5]) == "no result":
                return "Sorry, the postcode you entered was not recognised. Please try again."
            else:
                business_dict["distance"] = calculate_distance(postcode, each_business[5])
            business_results_list.append(business_dict)
    return sort_by_distance(business_results_list)

def calculate_distance(inputted_postcode, search_result_postcode):
    user_postcode_location = get_postcode_location_from_api(inputted_postcode.upper())
    db_postcode_location = get_postcode_location_from_db(search_result_postcode)
    if user_postcode_location == "Postcode not recognised.":
        return "no result"
    else:
        dist = distance_haversine(user_postcode_location[0][2], user_postcode_location[0][1], db_postcode_location[0][2], db_postcode_location[0][1])
#        dlon = db_postcode_location[0][1] - user_postcode_location[0][1]
#        dlat = db_postcode_location[0][2] - user_postcode_location[0][2]
        return dist

def sort_by_distance(results_list):
    results = sorted(results_list, key=lambda s:s["distance"])
    for dictionary in results:
        dictionary["distance"]=round(dictionary["distance"], 2)
    return results

def distance_haversine(lat1, lon1, lat2, lon2):
    radius = 3959 # miles
    lat = radians(lat2 - lat1)
    lon = radians(lon2 - lon1)
    sins_lat = sin(lat/2) * sin(lat/2)
    sins_lon = sin(lon/2) * sin(lon/2)
    cosinus = cos(radians(lat1)) * cos(radians(lat2))
    a = sins_lat + cosinus * sins_lon
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = radius * c
    return distance  