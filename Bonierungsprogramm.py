# -*- coding: utf-8 -*-
import kivy
kivy.require('1.1.3')

import os
import pickle


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget
from kivy.uix.carousel import Carousel

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class LoginScreen(FloatLayout):
     

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        self.add_widget(Label(text= "Wilkommen [color=ff3333] [sub] bei der [/sub][/color][color=3333ff][b] Bonierungs[sup][color=#098125ff]App[/sup][/b][/color]", \
                              markup = True, pos_hint={'top': 1.2}, font_size='20sp'))

                             
        self.GridlayoutS1 = GridLayout(cols = 2, size_hint_y = 1/5, pos_hint={'top': 0.6})
        self.add_widget(self.GridlayoutS1)
        self.GridlayoutS1.add_widget(Label(text='User Name')) #, size_hint_x = 0.2, size_hint_y = 0.2))
        self.username = TextInput(multiline=False) #, size_hint_x = 0.2, size_hint_y = 0.2)
        self.GridlayoutS1.add_widget(self.username)
        self.GridlayoutS1.add_widget(Label(text='password')) #,size_hint_x = 0.2, size_hint_y = 0.2))
        self.password = TextInput(password=True, multiline=False) #, size_hint_x = 0.2, size_hint_y = 0.2)
        self.GridlayoutS1.add_widget(self.password)
        self.BenutzerListe = {"bruno": "essen"};
        
        self.add_widget(Button(text='Einloggen', size_hint_y= 1/5, pos_hint={'top': 0.4}, on_release = self.AbfrageLogin))

        self.LabelLoginanzeiger = Label(size_hint_y= 1/5)
        self.add_widget(self.LabelLoginanzeiger)

 
        
        
         
    def AbfrageLogin(self, widget):
         Username = self.username.text
         Passwort = self.password.text
         if Username in self.BenutzerListe and Passwort == self.BenutzerListe[Username]:
              self.LabelLoginanzeiger.text = 'Login korrekt'
              self.clear_widgets()
              self.HauptProgramm()
              
         else:
              self.LabelLoginanzeiger.text = 'Login inkorrekt'

    def HauptProgramm(self, *args):
        print 'das ist das Hauptprogramm'
        self.BilderListeVorlaeufer = []
        self.BilderListeVorlaeufer = os.listdir(os.getcwd() + '/pictures')
        self.Pfade = []
        for i in self.BilderListeVorlaeufer:
            Pfad = os.path.join('pictures', i)
            self.Pfade.append(Pfad)
        self.HauptCarousel = Carousel() 
        self.add_widget(self.HauptCarousel)
        ####################################################################################################
        ### Erste Seite im HauptCarousel momentan mit den produktbildern
        self.HauptCarousel.FloatLayout = FloatLayout()
        self.HauptCarousel.add_widget(self.HauptCarousel.FloatLayout)
        self.HauptCarousel.FloatLayout.GridLayout = GridLayout(cols=3, pos_hint={'x': 0,'y': 0}, size_hint=[1,0.9])
        self.HauptCarousel.FloatLayout.add_widget(self.HauptCarousel.FloatLayout.GridLayout)
##        self.HauptCarousel.FloatLayout.GridLayout.add_widget(Button(text='test'))
##        self.HauptCarousel.FloatLayout.GridLayout.add_widget(Button(text='test2'))
        for i in range(9):
            button = Button(background_normal = self.Pfade[i], background_down= 'pictures/bilder_oberflaeche/1361740537_Ball Green_mitHaken.png', mipmap= True)
            self.HauptCarousel.FloatLayout.GridLayout.add_widget(button)


        #####################################################################################################    
        ### 2 Seite im Hauptcarousel mit testbutton zur datei Erstellung
        self.HauptCarousel2 = BoxLayout(orientation='vertical')
        self.HauptCarousel.add_widget(self.HauptCarousel2)
        self.HauptCarousel2.Texteingabe = TextInput(multiline=True)
        self.HauptCarousel2.add_widget(self.HauptCarousel2.Texteingabe)
        
        self.HauptCarousel2.ButtonSchreiben = Button(text="datei schreiben", on_release = self.datenpickeln)
        self.HauptCarousel2.add_widget(self.HauptCarousel2.ButtonSchreiben)
        ### 3 Seite im Hauptcarousel momentan mit Datei Auslesefunktion
        self.HauptCarousel3 = BoxLayout(orientation='vertical')
        self.HauptCarousel.add_widget(self.HauptCarousel3)
        self.HauptCarousel3.Textausgabe = TextInput(multiline=True, readonly = True)
        self.HauptCarousel3.add_widget(self.HauptCarousel3.Textausgabe)
        
        self.HauptCarousel3.ButtonLesen = Button(text="datei auslesen", on_release = self.datenentpickeln)
        self.HauptCarousel3.add_widget(self.HauptCarousel3.ButtonLesen)

        

    def datenpickeln(self, widget):
        BonListe = self.HauptCarousel2.Texteingabe.text
        '''function to pickle data to make it ready for sending'''        
        try:
            with open('bonliste.txt', 'w+b') as BonListeDaten_File:
                pickle.dump(BonListe, BonListeDaten_File)
        except IOError as err:
            print('Dateifehler: ' + str(err))
        except pickle.PickleError as perr:
            print('Pickling Fehler: ' + str(perr))

    def datenentpickeln(self, widget):
        with open('bonliste.txt', 'rb') as BonListeDaten_File_entpickelt:
            BonListeWiederhergestellt = pickle.load(BonListeDaten_File_entpickelt)

        print 'die entpickelte BinListe ist: '
        print BonListeWiederhergestellt
        BonListe = BonListeWiederhergestellt
        self.HauptCarousel3.Textausgabe.text = BonListe
        
         


class BonierungsprogrammApp(App):

##    def __init__(self, **kwargs):
##         pass

    def build(self):
        return LoginScreen()

    


if __name__ == '__main__':
    BonierungsprogrammApp().run()
