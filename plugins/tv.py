#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: Optikdev optikdev@googlemail.com
#todo: genaueres programm zu jeder tageszeit
#project: SiriServer
#commands: was kommt heute/morgen auf !Sender! z.B. pro7

from plugin import *
import urllib
import re
import xml.dom.minidom
from xml.dom.minidom import Node
import time

class epg(Plugin):

    res = {
        'setProg': {
            'de-DE': 'was kommt (heute|morgen) abend auf (.*)'
        }
    }
    @register("de-DE", res['setProg']['de-DE'])
    def heuteAbend(self, speech, language):
	ProgString = re.match(epg.res['setProg'][language], speech, re.IGNORECASE)	
	
	if (ProgString.group(2) == 'pro7'):
		url = "pro-7.de"
	elif (ProgString.group(2) == 'sat1'):
		url = "sat-1.de"
	elif (ProgString.group(2) == 'rtl'):
		url = "rtl.de.de"
	elif (ProgString.group(2) == 'ard'):
		url = "ard.de"
	elif (ProgString.group(2) == 'zdf'):
		url = "zdf.de"
	elif (ProgString.group(2) == 'vox'):
		url = "vox.de"
	elif (ProgString.group(2) == 'kabel1'):
		url = "kabel-1.de"
	else:
		url = None
	zeit = time.localtime()
	if (url == None):
		self.say("Da ist etwas falsch gelaufen!")
        	self.complete_request()
	else:
		if (ProgString.group(1) == 'heute'):
			zeits = str(zeit[0])+'%0.2d' %zeit[1]+str(zeit[2])+'201500'
		else:
			zeits = str(zeit[0])+'%0.2d' %zeit[1]+str(zeit[2]+1)+'201500'	
		html = urllib.urlopen("http://tvprofil.net/xmltv/data/"+url+"/weekly_"+url+"_tvprofil.net.xml").read()
		dom = xml.dom.minidom.parseString(html)
		for node in dom.getElementsByTagName('programme'):
			if (node.getAttribute('start') == zeits):
				Title = node.getElementsByTagName('title')
				self.say(Title[0].firstChild.data)
        			self.complete_request()