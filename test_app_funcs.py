# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:22:06 2019

@author: amand
"""

import sqlite3
import os


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
    person_data = get_data_from_db("SELECT * FROM person WHERE surname = ?", surname)
    return person_data

def get_businessName_data(businessName):
    businessName_data = get_data_from_db("SELECT * FROM business WHERE business_name = ?", businessName)
    return businessName_data

def get_businessCategory_data(businessCategory):
    businessCategory_data = get_data_from_db("SELECT * FROM business WHERE business_category = ?", businessCategory)
    return businessCategory_data

def get_postcode_location(postcode):
    location_of_postcode = get_data_from_db("SELECT * FROM coordinate_mapping WHERE postcode = ?", postcode)
    return location_of_postcode

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
                 return "Sorry, postcode not recognised."
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
        return "error"
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
                return "Sorry, postcode not recognised."
            else:
                business_dict["distance"] = calculate_distance(postcode, each_business[5])
            business_results_list.append(business_dict)
    return sort_by_distance(business_results_list)

def calculate_distance(inputted_postcode, search_result_postcode):
    user_postcode_location = get_postcode_location(inputted_postcode)
    db_postcode_location = get_postcode_location(search_result_postcode)
    if user_postcode_location == 0:
        return "no result"
    else:
        dlon = db_postcode_location[0][1] - user_postcode_location[0][1]
        dlat = db_postcode_location[0][2] - user_postcode_location[0][2]
        dist = (dlon**2 + dlat**2)**0.5
        return dist

def sort_by_distance(results_list):
    results = sorted(results_list, key=lambda s:s["distance"])
    for dictionary in results:
        dictionary["distance"]=round(dictionary["distance"], 2)
    return results

    