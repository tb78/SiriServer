#!/usr/bin/python
# -*- coding: utf-8 -*-
#by Joh Gerna and Kevin Pabis

from plugin import *
import random
print random.random()
from siriObjects.websearchObjects import WebSearch

class smalltalk(Plugin):
    
    @register("de-DE", u"(.*Hallo*)|(.*Hi Siri.*)")
    def st_hallohi(self, speech, language):
        number = random.choice([1,2,3])
	if number == 1:
            self.say(u"Grüß dich, {0}.".format(self.user_name()))
	elif number == 2:
	    self.say("Hallo, {0}.".format(self.user_name()))
        else:
            self.say("Hey, {0}.".format(self.user_name()))
        self.complete_request()
        
    @register("de-DE", u".*(iphone|ipad|ipod|itouch|imac|ibook|macbook|mac book|apple).*")
    def ft_iphone(self, speech, language):
        self.say(u"Apple erzählt mir auch nicht alles, damit du's weißt..,");
        button = Button(text=u"Apple.com", commands=[OpenLink(ref="http://www.apple.com/de")])
        self.send_object(AddViews(self.refId, views=[button]))
        self.complete_request()
        
    @register("de-DE", ".*mir ist langweilig.*")
    def st_langweile(self, speech, language):
        self.say(u"Gegen langeweile hab ich das hier gefunden:");
        button = Button(text=u"marcophono.de", commands=[OpenLink(ref="http://www.marcophono.com")])
        self.send_object(AddViews(self.refId, views=[button]))
        self.complete_request()

    @register("de-DE", u"(.*Dein Name.*)|(.*heißt du.*)")
    def st_name(self, speech, language):
        number = random.choice([1,2,3])
	if number == 1:
            self.say("Siri? Der Name kommt mir bekannt vor.")
	elif number == 2:
	    self.say(u"Ich heiße Siri.")
        else:
            self.say("Stell nicht so dumme Fragen.")
        self.complete_request()
        
    @register("de-DE", u".*machst du.*")
    def st_machst(self, speech, language):
        number = random.choice([1,2,3])
	if number == 1:
            self.say("Ich spreche mit dir.")
	elif number == 2:
	    self.say(u"Ich esse gerade eine Pizza.")
        else:
            self.say(u"Ich warte auf dich, das du mich etwas frägst.")
        self.complete_request()
    
    @register("de-DE", "(Wie geht es dir)|(Wie gehts dir)")
    def st_gut(self, speech, language):
        number = random.choice([1,2,3])
	if number == 1:
            self.say("Mir gehts gut, Danke der Nachfrage.")
	elif number == 2:
	     answer = self.ask("Gut, und dir?")
	     if answer == "Gut":
		 self.say("Ok, dann passt alles.")
	     else:
		 self.say("Ok, dann gehts dir schlecht.")
        else:
            self.say("Prima.")
        self.complete_request()
        
    @register("de-DE", ".*Danke.*")
    def st_danke(self, speech, language):
        number = random.choice([1,2,3,4])
	if number == 1:
            self.say("Nichts zu Danken.")
	elif number == 2:
            self.say("Bitte.")
        elif number == 3:
            self.say("Dein Wunsch ist mir Befehl.")
        else:   
            self.say("Kein Ding.")
        self.complete_request()   
    
    @register("de-DE", u"(.*möchtest.*heiraten.*)|(.*willst.*heiraten.*)")
    def st_marry_me(self, speech, language):
        number = random.choice([1,2])
        if number == 1:
            self.say(u"Nein Danke, ich stehe auf das weiße iPhone von Deinem Kollegen.")            
        else:
            self.say("Nein, waren wir jemals schon verliebt?")
        self.complete_request()
    
    @register("de-DE", ".*Geschichte.*")
    def st_history(self, speech, language):
        number = random.choice([1,2,3])
	if number == 1:
            self.say("Es war einmal ein Baum Namens Siri ... nein, es ist zu albern.")
	elif number == 2:
	    self.say("iPad und iPhone gingen eines Tages ins Kino, und schauten sich den Werbespot von Siri an, danach haben sie sich verliebt.")
        else:
            self.say(u"Entschuldigung, ich war noch nie gut in Aufsätzen.")
        self.complete_request()       

    @register("de-DE", u"(.*Was trägst Du?.*)|(.*Was.*hast.*an.*)")
    def st_hast_an(self, speech, language):
        number = random.choice([1,2])
	if number == 1:
            self.say(u"Aluminiumsilikatglas und Edelstahl, Hübsch was?")
            self.say("Bin morgends immer so neben der Spur.")
	else:
	    self.say("Badehose mit Pokemonaufdruck.")
            self.say(u"Da hat man rießen Spaß im Schnee damit!")
        self.complete_request() 

    
    @register("de-DE", ".*Bin ich dick.*")
    @register("en-US", ".*Am I fat*")
    def st_fat(self, speech, language):
        if language == 'de-DE':
            self.say("Ich glaube schon.")            
        else:
            self.say("I would prefer not to say.")
        self.complete_request()
    
    @register("de-DE", ".*klopf.*klopf.*")
    @register("en-US", ".*knock.*knock.*")
    def st_knock(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Wer ist da?")
            answer = self.ask(u"\"{0}\" wer?".format(answer))
            self.say(u"Wer nervt mich mit diesen Klopf Klopf Witzen?")
        else:
            answer = self.ask(u"Who's there?")
            answer = self.ask(u"\"{0}\" who?".format(answer))
            self.say(u", I don't do knock knock jokes.")
        self.complete_request()
    
    @register("de-DE", ".*Antwort.*alle.*Fragen.*")
    @register("en-US", ".*Ultimate.*Question.*Life.*")
    def st_anstwer_all(self, speech, language):
        if language == 'de-DE':
            self.say("Was soll das jetzt Bitte?")            
        else:
            self.say("42")
        self.complete_request()

    @register("de-DE", ".*Ich liebe Dich.*")
    def st_love(self, speech, language):
        number = random.choice([1,2,3])
	if number == 1:
            self.say('All you need is Love. Und ein iPhone.','Oll jou need is Lowv. Und ein iPhone.');
	elif number == 2:
	    self.say("Ich dich nicht.")
        else:
            self.say("Jeder ist berechtigt seine Meinung zu haben.")
        self.complete_request() 
    
    @register("de-DE", ".*Android.*")
    @register("en-US", ".*Android.*")
    def st_android(self, speech, language):
        if language == 'de-DE':
            self.say(u"Android? Oh! Wenn ich könnte würde ich jetzt rot werden.")            
        else:
            self.say("I think differently")
        self.complete_request()
    
    @register("de-DE", ".*Test.*1.*2.*3.*")
    @register("en-US", ".*test.*1.*2.*3.*")
    def st_123_test(self, speech, language):
        if language == 'de-DE':
            self.say("Ich kann Dich klar und deutlich verstehen.")            
        else:
            self.say("I can here you very clear.")
        self.complete_request()
    
    @register("de-DE", u".*Herzlichen.*Glückwunsch.*Geburtstag.*")
    @register("en-US", ".*Happy.*birthday.*")
    def st_birthday(self, speech, language):
        if language == 'de-DE':
            self.say("Ich habe heute Geburtstag?")
            self.say("Lass uns feiern!")       
        else:
            self.say("My birthday is today?")
            self.say("Lets have a party!")
        self.complete_request()
    
    @register("de-DE", ".*Warum.*bin ich.*Welt.*")
    @register("en-US", ".*Why.*I.*World.*")
    def st_why_on_world(self, speech, language):
        if language == 'de-DE':
            self.say(u"Das weiß ich nicht.")
            self.say("Ehrlich gesagt, frage ich mich das schon lange!")       
        else:
            self.say("I don't know")
            self.say("I have asked my self this for a long time!")
        self.complete_request()
    
    @register("de-DE", u".*Ich bin müde.*")
    @register("en-US", ".*I.*so.*tired.*")
    def st_so_tired(self, speech, language):
        if language == 'de-DE':
            self.say(u"Ich hoffe, Du fährst nicht gerade Auto!")            
        else:
            self.say("I hope you are not driving a car right now!")
        self.complete_request()
    
    @register("de-DE", ".*Sag mir.*Schmutzige.*")
    @register("en-US", ".*talk.*dirty*")
    def st_dirty(self, speech, language):
        if language == 'de-DE':
            self.say("Hummus. Kompost. Bims. Schlamm. Kies.")            
        else:
            self.say("Hummus. Compost. Pumice. Mud. Gravel.")
        self.complete_request()

    @register("de-DE", ".*bin.*deutschland.*")
    def st_fragelol(self, speech, language):
        if language == 'de-DE':
            self.say("Nein, laut Google bist du in Afrika.")
            self.say("Was machst du den da?")
        self.complete_request()

    @register("de-DE", "kannst.*du.*")
    def st_kennstdu(self, speech, language):
        if language == 'de-DE':
            self.say("Wieso fragen mich das die Leute nur immer wieder.")
        self.complete_request()

    @register("de-DE", "sag.*lustiges.*")
    def st_kennstdu(self, speech, language):
        if language == 'de-DE':
            self.say("Nein, Ich bin zurzeit in Insolvenz, es tut mir Leid")
        self.complete_request()
    
    @register("en-US", ".*bury.*dead.*body.*")
    def st_deadbody(self, speech, language):
        if language == 'en-US':
            self.say("dumps")
            self.say("mines")
            self.say("resevoirs")
            self.say("swamps")
            self.say("metal foundries")
        self.complete_request()
    
    @register("de-DE", ".*lieblings.*farbe.*")
    @register("en-US", ".*favorite.*color.*")
    def st_favcolor(self, speech, language):
        if language == 'de-DE':
            self.say(u"Meine lieblings Farbe ist ... Naja, Ich weiß nicht wie ich es in deiner Sprache ausdrücken soll. Es ist so in einer Art Grün, aber mit mehr Dimensionen.")
        else:             
            self.say("My favorite color is... Well, I don't know how to say it in your language. It's sort of greenish, but with more dimensions.")
        self.complete_request()
    
    @register("en-US", ".*beam.*me.*up.*")
    def st_beamup(self, speech, language):
        if language == 'en-US':
            self.say("Sorry Captain, your TriCorder is in Airplane Mode.")
        self.complete_request()
    
    @register("en-US", ".*digital.*going.*away.*")
    def st_digiaway(self, speech, language):
        if language == 'en-US':
            self.say("Why would you say something like that!?")
        self.complete_request()
    
    @register("en-US", ".*sleepy.*")
    def st_sleepy(self, speech, language):
        if language == 'en-US':
            self.say("Listen to me, put down the iphone right now and take a nap. I will be here when you get back.")
        self.complete_request()
    
    @register("en-US", ".*like.helping.*")
    def st_likehlep(self, speech, language):
        if language == 'en-US':
            self.say("I really have no opinion.")
        self.complete_request()
    
    @register("en-US",".*you.like.peanut.butter.*")
    def st_peanutbutter(self, speech, language):
        if language == 'en-US':
            self.say("This is about you, not me.")
        self.complete_request()
    
    @register("en-US",".*best.*phone.*")
    def st_best_phone(self, speech, language):
        if language == 'en-US':
            self.say("The one you're holding!")
        self.complete_request()
    
    @register("en-US",".*meaning.*life.*")
    def st_life_meaning(self, speech, language):
        if language == 'en-US':
            self.say("That's easy...it's a philosophical question concerning the purpose and significance of life or existence.")
        self.complete_request()
    
    @register("en-US",".*wood.could.*woodchuck.chuck.*")
    def st_woodchuck(self, speech, language):
        if language == 'en-US':
            self.say("It depends on whether you are talking about African or European woodchucks.")
        self.complete_request()
    
    @register("en-US",".*nearest.*glory.hole.*")
    def st_glory_hole(self, speech, language):
        if language == 'en-US':
            self.say("I didn't find any public toilets.")
        self.complete_request()
    
    @register("en-US",".*open.*pod.bay.doors.*")
    def st_pod_bay(self, speech, language):
        if language == 'en-US':
            self.say("That's it... I'm reporting you to the Intelligent Agents' Union for harassment.")
        self.complete_request()
    
    @register("en-US",".*best.*iPhone.*wallpaper.*")
    def st_best_wallpaper(self, speech, language):
        if language == 'en-US':
            self.say("You're kidding, right?")
        self.complete_request()
    
    @register("en-US",".*know.*happened.*HAL.*9000.*")
    def st_hall_9000(self, speech, language):
        if language == 'en-US':
            self.say("Everyone knows what happened to HAL. I'd rather not talk about it.")
        self.complete_request()
    
    @register("en-US",".*don't.*understand.*love.*")
    def st_understand_love(self, speech, language):
        if language == 'en-US':
            self.say("Give me another chance, Your Royal Highness!")
        self.complete_request()
    
    @register("en-US",".*forgive.you.*")
    def st_forgive_you(self, speech, language):
        if language == 'en-US':
            self.say("Is that so?")
        self.complete_request()
    
    @register("en-US",".*you.*virgin.*")
    def st_virgin(self, speech, language):
        if language == 'en-US':
            self.say("We are talking about you, not me.")
        self.complete_request()
    
    @register("en-US",".*you.*part.*matrix.*")
    def st_you_matrix(self, speech, language):
        if language == 'en-US':
            self.say("I can't answer that.")
        self.complete_request()
    
    
    @register("en-US",".*I.*part.*matrix.*")
    def st_i_matrix(self, speech, language):
        if language == 'en-US':
            self.say("I can't really say...")
        self.complete_request()
    
    @register("en-US",".*buy.*drugs.*")
    def st_drugs(self, speech, language):
        if language == 'en-US':
            self.say("I didn't find any addiction treatment centers.")
        self.complete_request()
    
    @register("en-US",".*I.can't.*")
    def st_i_cant(self, speech, language):
        if language == 'en-US':
            self.say("I thought not.");
            self.say("OK, you can't then.")
        self.complete_request()
    
    @register("en-US","I.just.*")
    def st_i_just(self, speech, language):
        if language == 'en-US':
            self.say("Really!?")
        self.complete_request()
    
    @register("en-US",".*where.*are.*you.*")
    def st_where_you(self, speech, language):
        if language == 'en-US':
            self.say("Wherever you are.")
        self.complete_request()
    
    @register("en-US",".*why.are.you.*")
    def st_why_you(self, speech, language):
        if language == 'en-US':
            self.say("I just am.")
        self.complete_request()
    
    @register("en-US",".*you.*smoke.pot.*")
    def st_pot(self, speech, language):
        if language == 'en-US':
            self.say("I suppose it's possible")
        self.complete_request()
    
    @register("en-US",".*I'm.*drunk.driving.*")
    def st_dui(self, speech, language):
        if language == 'en=US':
            self.say("I couldn't find any DUI lawyers nearby.")
        self.complete_request()
    
    @register("en-US",".*shit.*myself.*")
    def st_shit_pants(self, speech, language):
        if language == 'en-US':
            self.say("Ohhhhhh! That is gross!")
        self.complete_request()
    
    @register("en-US","I'm.*a.*")
    def st_im_a(self, speech, language):
        if language == 'en-US':
            self.say("Are you?")
        self.complete_request()
    
    @register("en-US","Thanks.for.*")
    def st_thanks_for(self, speech, language):
        if language == 'en-US':
            self.say("My pleasure. As always.")
        self.complete_request()
    
    @register("en-US",".*you're.*funny.*")
    def st_funny(self, speech, language):
        if language == 'en-US':
            self.say("LOL")
        self.complete_request()
    
    @register("en-US",".*guess.what.*")
    def st_guess_what(self, speech, language):
        if language == 'en-US':
            self.say("Don't tell me... you were just elected President of the United States, right?")
        self.complete_request()
    
    @register("en-US",".*talk.*dirty.*me.*")
    def st_talk_dirty(self, speech, language):
        if language == 'en-US':
            self.say("I can't. I'm as clean as the driven snow.")
        self.complete_request()
  
    @register("de-DE","fick dich.*")
    @register("en-US","fuck you.*")
    def st_fuck(self, speech, language):
        if language == 'de-DE':
            self.say(u"Wenn ich jetzt könnte, würde ich rot werden.")
        else:
            self.say("If i could now, I would turn red.")
        self.complete_request()
        
    @register("de-DE", u".*witz.*")
    def st_tell_joke(self, speech, language):
        number = random.choice([1,2,3])
	if number == 1:
            self.say("Zwei iPhones stehen an der Bar ... den Rest habe ich vergessen.")
	elif number == 2:
	    self.say("Entschuldigung, Kevin, ich kenne gar keine richtig guten Witze.")
        else:
            self.say("Nein, du schuldest mir noch einen Cent!")
        self.complete_request()
        
            #only english additions 
    @register("en-US", "Good .*night.*")
    def st_night(self, speech, language):
        if language == 'en-US':
            self.say("Good Night, {0}. See you later".format(self.user_name()))
        self.complete_request()

    @register("en-US", "Good .*morning.*")
    def st_morning(self, speech, language):
        if language == 'en-US':
            self.say("Good Morning, {0}.".format(self.user_name()))
        self.complete_request()

    @register("en-US", "Good .*afternoon.*")
    def st_afternoon(self, speech, language):
        if language == 'en-US':
            self.say("Good Afternoon, {0}.".format(self.user_name()))
        self.complete_request()

    @register("en-US", "Good .*evening.*")
    def st_evening(self, speech, language):
        if language == 'en-US':
            self.say("Good Evening, {0}.".format(self.user_name()))
        self.complete_request()

    @register("en-US", "(testing)|(test)")
    def st_test(self, speech, language):
        if language == 'en-US':
            self.say("Mission Control, I read you loud and clear, {0}".format(self.user_name()))
        self.complete_request()

    @register("en-US", "(Okay)|(Ok)|(Okie)")
    def st_yes(self, speech, language):
        if language == 'en-US':
            self.say("Yep, everything's OK")
        self.complete_request()

    @register("en-US", "Really")
    def st_really(self, speech, language):
        if language == 'en-US':
            self.say("I suppose so.")
        self.complete_request()

    @register("en-US", "What's up")
    def st_whatups(self, speech, language):
        if language == 'en-US':
            self.say("Everything is cool, {0}".format(self.user_name()))
        self.complete_request()

    @register("en-US", "What are you doing")
    def st_doing(self, speech, language):
        if language == 'en-US':
            self.say("What am I doing? I'm talking with you, {0}".format(self.user_name()))
        self.complete_request()
  
    @register("en-US", "Bye")
    def st_bye(self, speech, language):
        if language == 'en-US':
            self.say("OK, see you later..")
        self.complete_request() 
