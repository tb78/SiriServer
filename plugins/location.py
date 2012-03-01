#!/usr/bin/python
# -*- coding: utf-8 -*-

# Based on the WhereAmI plugins

import re
import urllib2, urllib
import json
import math
from plugin import *

from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.mapObjects import SiriMapItemSnippet,SiriLocation, SiriMapItem
from siriObjects.systemObjects import GetRequestOrigin,Location

APIKEY = APIKeyForAPI("googleplaces")

class location(Plugin):

    @register("de-DE", "(Wo bin ich.*)")     
    @register("en-US", "(Where am I.*)")
    @register("fr-FR", u"((ou|où).*suis.*je.*)")
    def whereAmI(self, speech, language):
        location = self.getCurrentLocation(force_reload=True,accuracy=GetRequestOrigin.desiredAccuracyBest)
        url = "http://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&sensor=false&language={2}".format(str(location.latitude),str(location.longitude), language)
        jsonString = None
        city = ""
        country = ""
        state = ""
        stateLong = ""
        countryCode = ""
        result = ""
        street = ""
        postal_code = ""
        try:
	        jsonString = urllib2.urlopen(url, timeout=3).read()
	        response = json.loads(jsonString)
	        components = response['results'][0]['address_components']
	        result = response['results'][0]['formatted_address'];
        except:
	        pass
        if components != None:
            city = filter(lambda x: True if "locality" in x['types'] or "administrative_area_level_1" in x['types'] else False, components)[0]['long_name']
            country = filter(lambda x: True if "country" in x['types'] else False, components)[0]['long_name']
            state = filter(lambda x: True if "administrative_area_level_1" in x['types'] or "country" in x['types'] else False, components)[0]['short_name']
            stateLong = filter(lambda x: True if "administrative_area_level_1" in x['types'] or "country" in x['types'] else False, components)[0]['long_name']
            countryCode = filter(lambda x: True if "country" in x['types'] else False, components)[0]['short_name']
            street = filter(lambda x: True if "route" in x['types'] else False, components)[0]['short_name']
            street_number = filter(lambda x: True if "street_number" in x['types'] else False, components)[0]['short_name']
            street = street + " " + street_number
            postal_code = filter(lambda x: True if "postal_code" in x['types'] else False, components)[0]['short_name']

        view = AddViews(self.refId, dialogPhase="Completion")
        mapsnippet = SiriMapItemSnippet(items=[SiriMapItem(result, SiriLocation(result, street, city, state, countryCode, postal_code, location.latitude, location.longitude))])
        view.views = [AssistantUtteranceView(text="Du bist mit mir hier...", dialogIdentifier="Map#test"), mapsnippet]
        self.sendRequestWithoutAnswer(view)
        self.say(u"Du bist mit mir bei, "+result)
        self.complete_request()

    @register("de-DE", "(Wo liegt.*)")    
    @register("en-US", "(Where is.*)")
    @register("fr-FR", u".*o(ù|u) (est |se trouve |ce trouve |se situe |ce situe )(.*)")
    def whereIs(self, speech, language, regex):
        the_location = None
        if language == "de-DE":
            the_location = re.match("(?u).* liegt ([\w ]+)$", speech, re.IGNORECASE)
            the_location = the_location.group(1).strip()
        elif language == 'fr-FR':
            the_location = regex.group(regex.lastindex).strip()
        else:
            the_location = re.match("(?u).* is ([\w ]+)$", speech, re.IGNORECASE)
            the_location = the_location.group(1).strip()
        
        print the_location
        if the_location != None:
            the_location = the_location[0].upper()+the_location[1:]
        else:
            if language == "de-DE":
                self.say('Ich habe keinen Ort gefunden!',None)
            elif language == 'fr-FR':
                self.say(u"Désolé, je n'arrive pas à trouver cet endroit !")
            else:
                self.say('No location found!',None)
            self.complete_request() 
            return
        url = u"http://maps.googleapis.com/maps/api/geocode/json?address={0}&sensor=false&language={1}".format(urllib.quote_plus(the_location.encode("utf-8")), language)
        jsonString=None
        try:
            jsonString = urllib2.urlopen(url, timeout=3).read()
        except:
            pass
        if jsonString != None:
            response = json.loads(jsonString)
            if response['status'] == 'OK':
                location = response['results'][0]['geometry']['location']
                city=response['results'][0]['address_components'][0]['long_name']
                try:
                    country=response['results'][0]['address_components'][2]['long_name']
                    countryCode=response['results'][0]['address_components'][2]['short_name']
                except:
                    country=the_location
                    countryCode=the_location
                if language=="de-DE":
                    the_header=u"Hier liegt {0}".format(the_location)
                elif language =="fr-FR":
                    the_header=u"Voici l'emplacement de {0} :".format(the_location)
                else:
                    the_header=u"Here is {0}".format(the_location)
                view = AddViews(self.refId, dialogPhase="Completion")
                s_Location=Location(the_header, city, city, "", countryCode, "", str(location['lat']), str(location['lng']))
                mapsnippet = SiriMapItemSnippet(items=[SiriMapItem(the_header, s_Location, "BUSINESS_ITEM")])
                view.views = [AssistantUtteranceView(text=the_header, dialogIdentifier="Map"), mapsnippet]
                self.sendRequestWithoutAnswer(view)
            else:
                if language=="de-DE":
                    self.say('Die Googlemaps informationen waren ungenügend!','Fehler')
                elif language == "fr-FR":
                    self.say(u"Les informations demandées ne sont pas sur Google Maps !", u'Erreur')
                else:
                    self.say('The Googlemaps response did not hold the information i need!','Error')
        else:
            if language=="de-DE":
                self.say('Ich konnte keine Verbindung zu Googlemaps aufbauen','Fehler')
            elif language == 'fr-FR':
                self.say(u"Je n'arrive pas à joindre Google Maps.", 'Erreur')
            else:
                self.say('Could not establish a conenction to Googlemaps','Error');
        self.complete_request()        

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        RAD_PER_DEG = 0.017453293
        Rkm = 6371        
        dlon = lon2-lon1
        dlat = lat2-lat1
        dlon_rad = dlon*RAD_PER_DEG
        dlat_rad = dlat*RAD_PER_DEG
        lat1_rad = lat1*RAD_PER_DEG
        lon1_rad = lon1*RAD_PER_DEG
        lat2_rad = lat2*RAD_PER_DEG
        lon2_rad = lon2*RAD_PER_DEG
        
        a = (math.sin(dlat_rad/2))**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * (math.sin(dlon_rad/2))**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return round(Rkm * c,2)
