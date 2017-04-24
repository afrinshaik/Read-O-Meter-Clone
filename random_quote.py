#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib, json

class Quote:
       
    def __init__(self):
        self.url = 'http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en&json=?'
    #Function to get quote from json
    def get_quote(self):
        #Open url using urllib and decode it
        req = urllib.request.Request(self.url, headers={'User-Agent' : "Magic Browser"}) 
        data = urllib.request.urlopen(req).read().decode('utf-8')
        #Replace special characters ' with \'
        data = data.replace(r"\'", "'")
        #Load data from json
        json_data = json.loads(data)
        if json_data['quoteAuthor'] == "":
            json_data['quoteAuthor'] = "Unknown"
        self.quote = json_data['quoteText'] + "\n\n\t\t-" + json_data['quoteAuthor']
        return self.quote
    



               
               
