# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:49:03 2019

@author: gracy
"""

from flask import Flask, render_template, request
from app_funcs import *
app=Flask("MyApp")
      
@app.route("/", methods=["GET", "POST"])
def business():      
      if request.method =='GET':
          return render_template("index.html")
      elif request.method=='POST':
          form_data = request.form
          postcode = form_data["postcode"]
          if postcode == '':
                result = 'please enter a postcode'
          else: 
                if "surname" in form_data:
                      if form_data["surname"]=='':
                            result = 'please enter a search term'
                      else: 
                            surname = form_data["surname"]
                            result = person_search_results(surname, postcode)
                      do_not_hide_surname = True
                elif "name" in form_data:
                      if form_data["name"]=='':
                            result = 'please enter a search term'
                      else: 
                            name = form_data["name"]
                            result = business_search_results(name, postcode, "name")
                      do_not_hide_name = True
                      do_not_hide_buttons = True
                else:
                      if form_data["category"] == '':
                            result = 'please enter a search term'
                      else: 
                            business_category = form_data["category"]
                            result = business_search_results(business_category, postcode, "category")
                      do_not_hide_category = True
                      do_not_hide_buttons = True
          return render_template ("index.html", title="results_page", **locals())
      else:
          print("Eh?")

app.run(debug=True)