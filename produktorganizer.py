#!/usr/bin/env python
# -*- coding: utf_8 -*-
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.spinner import Spinner

#from kivy.uix.popup import Popup

from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('produktorganizer.kv')

class ProduktOrganizer(BoxLayout):
    pass

class CustomScrollviewProduktOrganizer(BoxLayout):
    data  = ListProperty([])
     
    
    
    def on_data(self, instance, value):
        App.my_index2 = -1
        
        content_add = self.ids.content2.add_widget
        #print 'self.ids.content2', self.ids.content2
        #print 'self',self
        #print dir(self)
        #print 'self in on data', self
        
        #ProduktOrganizerInstanz.ids.custScrlInst.clear_widgets
        
        #self.data = [str(i) for i in range(3)]
        
        
        #import pdb; pdb.set_trace()
        #print 'vor der Schleife app.my_index',App.my_index
        #print 'len(app.Pfade)', len(App.Pfade) 
        
        for item in value:
            App.my_index2 = (App.my_index2 +1)
            print item
            print value
            #print self
            
            #print 'Es wurde die Schleife ausgefuert:  in der S app.my_index',App.my_index
            
            content_add(CustomScrollviewItem(size_hint= (1,None),height=25))
            #content_add(Button(text='test', height=50))
    pass
    

class CustomScrollviewItem(BoxLayout):
    pass

class PopupBildAuswaehlenProduktorganizer(Popup):
    pass

class PersonalOrganizer(BoxLayout):
    pass

class ZeitOrganizer(BoxLayout):
    pass

class PopupDateiAuswaehlenProduktorganizer(BoxLayout):
    pass
class SpinnerOptions(Spinner):
    pass
        
      
