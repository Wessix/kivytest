# -*- coding: utf-8 -*-
import kivy
kivy.require('1.1.3')

import os
import pickle


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


from kivy.uix.widget import Widget
from kivy.uix.carousel import Carousel

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown 

from kivy.graphics import Color, Rectangle


class LoginScreen(FloatLayout):
     

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        self.add_widget(Label(text= "Wilkommen [color=ff3333] [sub] bei der [/sub][/color][color=3333ff][b] Bonierungs[sup][color=#098125ff]App[/sup][/b][/color]", \
                              markup = True, pos_hint={'top': 1.2}, font_size='20sp'))

                             
        self.GridlayoutS1 = GridLayout(cols = 2, size_hint_y = 1/5, pos_hint={'top': 0.6})
        self.add_widget(self.GridlayoutS1)
        self.GridlayoutS1.add_widget(Label(text='User Name')) #, size_hint_x = 0.2, size_hint_y = 0.2))
        self.username = TextInput(multiline=False) #, size_hint_x = 0.2, size_hint_y = 0.2)
        self.username.bind(on_text_validate=self.on_enter)
        self.GridlayoutS1.add_widget(self.username)
        self.GridlayoutS1.add_widget(Label(text='password')) #,size_hint_x = 0.2, size_hint_y = 0.2))
        self.password = TextInput(password=True, multiline=False) #, size_hint_x = 0.2, size_hint_y = 0.2)
        self.GridlayoutS1.add_widget(self.password)
        self.BenutzerListe = {"": ""};
        
        self.add_widget(Button(text='Einloggen', size_hint_y= 1/5, pos_hint={'top': 0.4}, on_release = self.AbfrageLogin))

        self.LabelLoginanzeiger = Label(size_hint_y= 1/5)
        self.add_widget(self.LabelLoginanzeiger)

    def on_enter(self, instance):
        print('User pressed enter in', instance)
        self.password.focus = True

    

 
        
        
         
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
        ### First Page in MainCarousel atm with Product pictures
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
        ### 2 Page in MainCarousel with testbutton for creating /exporting to a file
        self.HauptCarousel2 = BoxLayout(orientation='vertical')
        self.HauptCarousel.add_widget(self.HauptCarousel2)
        self.HauptCarousel2.Texteingabe = TextInput(multiline=True)
        self.HauptCarousel2.add_widget(self.HauptCarousel2.Texteingabe)
        
        self.HauptCarousel2.ButtonSchreiben = Button(text="datei schreiben", on_release = self.datenpickeln)
        self.HauptCarousel2.add_widget(self.HauptCarousel2.ButtonSchreiben)
        #######################################################################
        ### 3 Seite im Hauptcarousel momentan mit Datei Auslesefunktion
        ### 3 Page in MainCarousel atm with functionality to read from file
        
        self.HauptCarousel3 = BoxLayout(orientation='vertical')
        self.HauptCarousel.add_widget(self.HauptCarousel3)
        self.HauptCarousel3.Textausgabe = TextInput(multiline=True, readonly = True)
        self.HauptCarousel3.add_widget(self.HauptCarousel3.Textausgabe)
        
        self.HauptCarousel3.ButtonLesen = Button(text="datei auslesen", on_release = self.datenentpickeln)
        self.HauptCarousel3.add_widget(self.HauptCarousel3.ButtonLesen)
        #######################################################################
        ### 4 Seite im Hauptcarousel momentan mit Tischmanager
        ### 4 Page in Maincarousel atm with some kind of Table Manager
        c = CustomLayout()
        self.HauptCarousel.add_widget(c)
        c.TopLabel = Label(text = 'Tisch[sup][color=#098125ff]Organizer[/sup][/b][/color]',  markup = True, \
                                             halign= 'left', valign= 'top', text_size= self.size, pos_hint={'x':0, 'y': 0})
        c.add_widget(c.TopLabel)
        cBoxLayout = BoxLayout (orientation = 'horizontal', size_hint = [0.8,0.1], pos_hint={'x':0.2, 'y': 0.9})
        c.add_widget(cBoxLayout)
        cBoxLayoutButton1 = Button(text = 'Menü1')
        cBoxLayoutButton2 = Button(text = 'Tisch+' , on_release = self.tischhinzufuegen)
        cBoxLayoutButton3 = Button(text = 'Spalte+', on_release = self.spaltehinzufuegen)
        cBoxLayoutButton4 = Button(text = 'Zeile+', on_release = self.zeilehinzufuegen)
        cBoxLayout.add_widget(cBoxLayoutButton1)
        cBoxLayout.add_widget(cBoxLayoutButton2)
        cBoxLayout.add_widget(cBoxLayoutButton3)
        cBoxLayout.add_widget(cBoxLayoutButton4)
        cGridLayout = GridLayout(cols = 3, rows = 4, padding = [20,20], spacing = [30,30], size_hint = [1,0.9], pos_hint={'x':0, 'y': 0})
        #cGridLayout = StackLayout(orientation = "tb-lr", padding = [20,20], spacing = [30,30], size_hint = [1,0.9], pos_hint={'x':0, 'y': 0})
              
        c.add_widget(cGridLayout)
        self.Tischliste = []

        #####################################################################
        ### Versuch eines Dropdown Buttons
        ### Try to implement a dropdown Button, probably better than a Spinner
        ### Creation of the Buttons representing the Tables
        #####################################################################
       
        Auswahlliste = ["Bestellung", "Abrechnung", "Best. Aendern", "Bennenen"]
        BackgroundcolorListe = [(1,0,0,1),(0,1,0,1),(0,0,1,1),(1,1,0,1)]
        
        for i in range(12):
            TischButtonText = "T " + str(i+1)
            DropdownObjekt = DropDown() 
            DropdownObjektButton = Button(text = TischButtonText, background_color = (201./255.,99./255.,23./255.,1))
            cGridLayout.add_widget(DropdownObjektButton)
            DropdownObjektButton.bind(on_release=DropdownObjekt.open)
            
            
            for x in range(len(Auswahlliste)):
                
                DropdownUnterbutton = Button(text=Auswahlliste[x], font_size = 15, size_hint_y=None, height=50, background_color = BackgroundcolorListe[x]) 
                DropdownObjekt.add_widget(DropdownUnterbutton)
              
                #print' button', i, 'unterbutton', x
            
            
            
            DropdownObjektButton.text= TischButtonText
            TischButtondict = {(i),DropdownObjektButton}
            self.Tischliste.append(TischButtondict)
            
        
        
##        for i in range(12):
##            TischButtonText = "T " + str(i+1)
##            #TischButton = Button(text=(''), on_release = self.tischmanipulieren)
##            TischButton = Spinner(text='', values = ("Bestellung", "Abrechnung", "Best. Aendern", "Bennenen")) 
##            cGridLayout.add_widget(TischButton)
##            TischButton.text= TischButtonText
##            TischButtondict = {(i),TischButton}
##            self.Tischliste.append(TischButtondict)

        print self.Tischliste


### function for Editing a Table#######################################
        
    def tischmanipulieren(self, widget):
         widget.text = 'mein text'
         
#### function for adding an extra  table to layout ##########################
         
    def tischhinzufuegen(self, widget):
        print 'Tisch hinzufuegen'
        print self.Tischliste[-1]
        LetzterTisch = self.Tischliste[-1]
        pass

#### function for adding a column to layout ####################################

    def spaltehinzufuegen(self, widget):
        print 'Spalte hinzufuegen'
        pass

#### function for adding a row to layout ####################################

    def zeilehinzufuegen(self, widget):
        print 'Zeile hinzufuegen'
        pass

   

#### function for exporting Data to file ####################################        

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


#### function for importing Data to file ####################################        
            

    def datenentpickeln(self, widget):
        with open('bonliste.txt', 'rb') as BonListeDaten_File_entpickelt:
            BonListeWiederhergestellt = pickle.load(BonListeDaten_File_entpickelt)

        print 'die entpickelte BinListe ist: '
        print BonListeWiederhergestellt
        BonListe = BonListeWiederhergestellt
        self.HauptCarousel3.Textausgabe.text = BonListe

### Custom Layout with background ###########################################

class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1,0,0,0.3) # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(
                            size=self.size,
                            pos=self.pos)

        self.bind(
                    size=self._update_rect,
                    pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
         


class BonierungsprogrammApp(App):

##    def __init__(self, **kwargs):
##         pass

    def build(self):
        return LoginScreen()

    


if __name__ == '__main__':
    BonierungsprogrammApp().run()
