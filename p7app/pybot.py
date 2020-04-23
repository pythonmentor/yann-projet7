#!/usr/bin/python3
# -*- coding: Utf-8 -*
import requests

import json

from random import randint


from p7app import mediawiki



class PapyBot():
    "class that will send all the informartion to our webpage"
    def __init__(self):
        self.sending_gps_coordinate = {}
        self.data_treated = {}
        
        
        
    def transformed_gps_into_json_results(self, lat, lng):
        self.a = lat
        self.b = lng
        "we are going to encode our answers from others classes to an answers which can be treated by js"
        self.sending_gps_coordinate = {"latitude": self.a , "longitude": self.b}
        return self.sending_gps_coordinate


    def transformed_pageid_into_json(self, lat, lng):
        "method that will put our page id into json"
        self.lat = lat
        self.lng = lng
        ap = mediawiki.MediaWikiApi()
        ap.search_around(lat, lng)
        self.pageid_for_js = ap.pageid
    
    def transformed_info_js(self, pageid):
        self.pageidjs = pageid
        ab = mediawiki.MediaWikiApi()
        ab.search_pageid(self.pageidjs)
        self.info = ab.extract
        self.url = ab.fullurl


        
        
        

def main():
    re = PapyBot()
    re.transformed_pageid_into_json(45.6778,18.5443)
    print(re.pageid_for_js)
    re.transformed_info_js(re.pageid_for_js)
    print(re.info)
main()