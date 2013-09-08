# -*- coding: utf-8 -*-
import kivy
kivy.require('1.1.3')



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget


from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.scrollview import ScrollView



from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView

#from kivy.uix.popup import Popup

from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from test2 import CustomScrollviewProduktOrganizer, ProduktOrganizer




class LoginScreen(FloatLayout):
     

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        self.add_widget(Label(text= "Test [color=ff3333] [sub] kv [/sub][/color][color=3333ff][b] file[sup][color=#098125ff]andPy[/sup][/b][/color]", \
                              markup = True, pos_hint={'top': 1.2}, font_size='20sp'))

        self.CustomScrollviewProduktOrganizerInstanz = CustomScrollviewProduktOrganizer()
        self.Box = BoxLayout(orientation = 'vertical')
        self.add_widget(self.Box)



        self.Box.add_widget(Button(text='inputdata',on_release=self.inputdata, size_hint = (1,0.1)))

        self.ProduktOrganizerInstanz = ProduktOrganizer()
        self.ButtonHinzufuegen = self.ProduktOrganizerInstanz.ids.ProduktlisteButtonHinzufuegen
        self.ButtonHinzufuegen.on_release = self.inputdata2

        self.Box.add_widget(self.ProduktOrganizerInstanz)                   ########## recomment this in
        #self.Box.add_widget(self.CustomScrollviewProduktOrganizerInstanz)    #################  comment this out
        

    def inputdata(self, widget):
        self.CustomScrollviewProduktOrganizerInstanz.data = [str(i) for i in range(5)]

    def inputdata2(self):
        self.CustomScrollviewProduktOrganizerInstanz.data = [str(i) for i in range(5)]
        
   
   

class testApp(App):

##    def __init__(self, **kwargs):
##         pass

    def build(self):
        return LoginScreen()

    


if __name__ == '__main__':
    testApp().run()
