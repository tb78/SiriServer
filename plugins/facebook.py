#!/usr/bin/python                                                                                                                                                                   
# -*- coding: utf-8 -*-    
#by Daniel "P4r4doX" Zaťovič

#This plugin is using "fbconsole" Python library by "pcardune". License :
# Copyright 2010-present Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.



from plugin import *
import fbconsole
import urllib2
import json


from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine




class facebook(Plugin): 	
    fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
    fbconsole.authenticate()
    @register("de-DE", "(.*facebook.*neuigkeiten.*)")
    def newsFeed(self, speech, language):
                statuses = 15 #how many statuses you want to fetch
                limit = 0
                error = 0          
		if (language == "de-DE"):
			statusString = ""			
			view = AddViews(self.refId, dialogPhase="Completion")
			self.say("Ich checke ...")
			for post in fbconsole.iter_pages(fbconsole.get('/me/home')):
				if(error == 1):
					error = 0
				else :
					limit = limit + 1
				try: 
					post['message']
					ansewer = post['from']['name'] + " schrieb : " + post['message'] 
					print "INFO Getting status : ", limit
					statusString = statusString + ansewer + "\n\n"
					
					#self.say(ansewer)
				except KeyError as (strerror):     
					#print "Key error({0})".format(strerror)
					error = 1
					continue			
				if(limit == statuses): 
					break
					
			facebookStatuses = AnswerObject(title='Statuses :',lines=[AnswerObjectLine(text=statusString)])
			view1 = 0
			view1 = AnswerSnippet(answers=[facebookStatuses])
			view.views = [view1]
			self.sendRequestWithoutAnswer(view) 	
			self.complete_request()		
        
          

					
            

#class facebookStatus(Plugin): 



    fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
    fbconsole.authenticate()
    @register("de-DE", "(update status.*)|(facebook status.*)|(poste status.*)")
    def updateStatus(self, speech, language):
        if (language == "de-DE"):
            if (speech.find('Update status') == 0):
                speech = speech.replace('Update status', ' ',1)
            elif (speech.find('Facebook status') == 0):
                speech = speech.replace('Facebook status',' ',1)
            elif (speech.find('Post status') == 0):
                speech = speech.replace('Post status',' ',1)            
            speech = speech.strip()
            if speech == "":
                speech = self.ask("Was willst du posten?")
        self.say("Dein Status lautet:")
        self.say(speech);
        ansewer =  self.ask("Fertig zu senden?")
        if (ansewer == "Ja"):
	  fbconsole.post('/me/feed', {'message': speech})
	  self.say ("Dein Status wurde gesendet !")
	  self.complete_request()
	else :
	  self.say("Ok, ich werde es nicht senden.")
	  self.complete_request()

    @register("de-DE", u"(.*facebook.*informationen.*)|(.*über.*mich.*)|(.*facebook.*information.*)")
    def facebookName(self, speech, language):
        if (language == "de-DE"):  
	  def getFBPicture():
		fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
		fbconsole.authenticate()
		file = urllib2.urlopen('https://graph.facebook.com/%s?access_token=%s&fields=picture' % (fbconsole.get('/me')['id'], fbconsole.ACCESS_TOKEN))
		data = json.load(file)
		return data["picture"]
	
	  self.say("Ich checke ...")
          view = AddViews(self.refId, dialogPhase="Completion")         
          AnswerString =""
	  AnswerString = u"Du heißt: " + fbconsole.get('/me')['name']
	  AnswerString = AnswerString + "\nDu bist: " + fbconsole.get('/me')['gender']
	  AnswerString = AnswerString + "\nDeine Sprache : " + fbconsole.get('/me')['locale']
	  AnswerString = AnswerString + "\nDeine Uhrzeit ist : " + fbconsole.get('/me')['updated_time']
	  
	  FacebookImage = AnswerObject(title="Profile photo",lines=[AnswerObjectLine(image=getFBPicture())])	  
          FacebookInfo = AnswerObject(title='Your info',lines=[AnswerObjectLine(text=AnswerString)])

          
          view1 = 0
          view1 = AnswerSnippet(answers=[FacebookImage, FacebookInfo])
          view.views = [view1]
          self.say("Hier ist deine Info :")
          self.sendRequestWithoutAnswer(view)               
          self.complete_request()
          
    @register("de-DE", "(.*facebook.*nachrichten.*)")
    def facebookNotifications(self, speech, language):
        if (language == "de-DE"):   
	  AnswerString = "" 
	  fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
	  fbconsole.authenticate()
	   
	  view = AddViews(self.refId, dialogPhase="Completion")
	  file = urllib2.urlopen('https://api.facebook.com/method/notifications.getList?access_token=%s&format=json' % (fbconsole.ACCESS_TOKEN))
	  data = json.load(file)
	  error = 0
	  number = 0
	  while (error != 1):
	    try :
		AnswerString = AnswerString + data["notifications"][number]["title_text"] + "\n\n"
                number = number + 1
	    except IndexError :
                error = 1
                
          if (number == 0):
	     self.say("Du hast keine neue Nachrichten!")
	     self.complete_request()
	     
          if (number == 0):
	     self.say("Du hast eine neue Nachricht!")
	     FacebookNotifications = AnswerObject(title='Your notification :',lines=[AnswerObjectLine(text=AnswerString)])
	     view1 = 0
	     view1 = AnswerSnippet(answers=[FacebookNotifications])
	     view.views = [view1]
	     self.sendRequestWithoutAnswer(view)               
	     self.complete_request()
	     
          self.say("Du hast %s neue Nachrichten!" % (number))
          FacebookNotifications = AnswerObject(title='Your notifications :',lines=[AnswerObjectLine(text=AnswerString)])
          view1 = 0
          view1 = AnswerSnippet(answers=[FacebookNotifications])
          view.views = [view1]
          self.sendRequestWithoutAnswer(view)               
          self.complete_request()
       
    @register("de-DE", "(.*facebook.*anfragen.*)|(.*freundschafts.*anfragen.*)")
    def facebookFriendRequests(self, speech, language):
        if (language == "de-DE"):   
	    fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access', 'manage_notifications', 'read_requests']
	    fbconsole.authenticate()
	    self.say("Ich checke ...")
	    AnswerString = "" 
	    view = AddViews(self.refId, dialogPhase="Completion")          
	    error = 0
	    number = 0
	    while (error != 1):
	      try:
		  AnswerString = AnswerString + fbconsole.get('/me/friendrequests')['data'][number]['from']['name'] + "\n"
		  number = number + 1
	      except IndexError:
		  error = 1
                
	    if (number == 0):
	     self.say("Du hast keine Freundschaftsanfragen!")
	     self.complete_request()
	  
	    if (number == 1):
	     self.say("Du hast eine neue Freundschaftsanfrage!")
	     FacebookRequests = AnswerObject(title='Friend request from :',lines=[AnswerObjectLine(text=AnswerString)])
	     view1 = 0
	     view1 = AnswerSnippet(answers=[FacebookRequests])
	     view.views = [view1]
	     self.sendRequestWithoutAnswer(view)               
	     self.complete_request()
	  
	    self.say("Du hast %s neue Freundschaftsanfragen!" % (number))
	    FacebookRequests = AnswerObject(title='Friend requests from :',lines=[AnswerObjectLine(text=AnswerString)])
	    view1 = 0
	    view1 = AnswerSnippet(answers=[FacebookRequests])
	    view.views = [view1]
	    self.sendRequestWithoutAnswer(view)               
	    self.complete_request()
	    
	    
	   

         
    @register("de-DE", "(.*facebook.*freunde.*)")
    def facebookFriends(self, speech, language):
        if (language == "de-DE"):   
           AnswerString = "" 
           view = AddViews(self.refId, dialogPhase="Completion")
           fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
	   fbconsole.authenticate()

	   for post in fbconsole.iter_pages(fbconsole.get('/me/friends')):
	     AnswerString = AnswerString + post['name'] + "\n"

	   self.say("Das sind deine Freunde:")
           FacebookFriends = AnswerObject(title='Deine Freunde :',lines=[AnswerObjectLine(text=AnswerString)])
           view1 = 0
           view1 = AnswerSnippet(answers=[FacebookFriends])
           view.views = [view1]
           self.sendRequestWithoutAnswer(view)               
           self.complete_request()
         

     
        
        
        
        
        
        
        
