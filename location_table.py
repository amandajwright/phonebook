# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:15:47 2019

@author: amand
"""

import sqlite3
import json
import requests

conn = sqlite3.connect("phonebook.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS coordinate_mapping(postcode TEXT, x_coordinate REAL, y_coordinate REAL)")

def get_postcodes():
    c.execute("SELECT postcode FROM business")
    business_postcodes = c.fetchall()
    postcode_list = []
    for postcode in business_postcodes:
        postcode_list.append(postcode[0])
    c.execute("SELECT postcode FROM person")
    person_postcodes = c.fetchall()
    for postcode in person_postcodes:
        if postcode[0] not in postcode_list:
            postcode_list.append(postcode[0])
        else:
            pass
    return postcode_list
            
def remove_spaces():
    postcode_list = get_postcodes()
    spaceless_postcode_list = []
    for postcode in postcode_list:
        separated_postcode = postcode.split()
        spaceless_postcode_list.append(separated_postcode[0] + separated_postcode[1])
    return spaceless_postcode_list
        
def populate_location_table():
    postcode_list = ["GL25YB", "CB227PA", "WC2H0AE", "B401PB", "NE484DH"]
    endpoint = "https://api.postcodes.io/postcodes/"
    for postcode in postcode_list:
        postcode_response = requests.get(endpoint + postcode)
        print
        data_postcode = postcode_response.json()
        print(data_postcode)
        if data_postcode["status"] == 200:
            x_coordinate = data_postcode["result"]["latitude"]
            y_coordinate = data_postcode["result"]["longitude"]
            postcodefromapi = data_postcode["result"]["postcode"]
            c.execute("INSERT INTO coordinate_mapping(postcode, x_coordinate, y_coordinate) VALUES (?, ?, ?)", (postcodefromapi, x_coordinate, y_coordinate))
            conn.commit()

def identifying_missing_postcodes():
    postcode_list = get_postcodes()
    c.execute("SELECT postcode FROM coordinate_mapping")
    location_pc_list = c.fetchall()
    new_list = []
    for postcode in location_pc_list:
        new_list.append(postcode[0])
    missing_pc_list = []
    for postcode in postcode_list:
        if postcode not in new_list:
            missing_pc_list.append(postcode)
        else:
            pass
    print(missing_pc_list)