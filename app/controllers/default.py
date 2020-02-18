import os
from app import app
from flask import Flask, render_template, redirect, flash
import requests 
import json
import urllib
from app.models.forms import GetLead

@app.route('/index-confirmation')
@app.route('/index-confirmation.html')
def landing_lead_index_confirmation():
    """Serve homepage template."""
    return render_template("/index-confirmation.html")


@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def landing_lead_index():
    """Serve homepage template."""
    form = GetLead()
    if form.validate_on_submit():
    	print(form.email.data)
    	headers ={}
    	headers["Content-Type"]='application/x-www-form-urlencoded'
    	endpoint = 'https://forms.hubspot.com/uploads/form/v2/3381861/514286cf-77d3-4338-8498-0b39394c3235?&'
    	#Convert the hs_context dictionary to a string
    	hs_context = json.dumps({
    		"hutk": "514286cf-77d3-4338-8498-0b39394c3235", 
    		"ipAddress": "192.168.1.12", 
    		"pageUrl": "http://demo.hubapi.com/contact/", 
    		"pageName": "Contact Us", 
    		"redirectUrl": "http://127.0.0.1:5000/index-confirmation"
    		})
    	#Build your request body
    	data = urllib.parse.urlencode({
    		'email':form.email.data,
    		'hs_context': hs_context
    		})

    	r = requests.post( url = endpoint, data = data, headers = headers)
    	return redirect('/index-confirmation')
    else:
        print(form.errors)
    return render_template("index.html", form=form)