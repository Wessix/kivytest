#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')

import os

import pickle
import gc

from kivy.lang import Builder
from kivy.app import App


from kivy.garden.filechooserthumbview import *
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout


from kivy.uix.widget import Widget
from kivy.uix.carousel import Carousel

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


from kivy.graphics import Color, Rectangle


from screenmanager import CustomScreenManager, CustomScreen
from customscrollviewpopup import CustomScrollviewPopupContent, CustomButton2, OptionenPopupBestellungen
from produktorganizer import ProduktOrganizer,PopupBildAuswaehlenProduktorganizer, CustomScrollviewItem, CustomScrollviewProduktOrganizer, PersonalOrganizer,ZeitOrganizer,PopupDateiAuswaehlenProduktorganizer
#from kivy.lang import Builder
#Builder.load_file('screenmanager.kv')



class LoginScreen(FloatLayout):
    
    #x = ListProperty([])
    
    #print x
    

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        #gc.disable()
        self.DropdownObjects = []

        self.add_widget(Label(text= "Wilkommen [color=ff3333] [sub] bei der [/sub][/color][color=3333ff][b] Bonierungs[sup][color=#098125ff]App[/sup][/b][/color]",
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
        self.SpinnerButtonZustand = 'Alle'
        App.AuswahlHauptlisteAlt = []
        print 'das ist das Hauptprogramm'
        self.BilderListeVorlaeufer = []
        self.BilderListeVorlaeufer = os.listdir(os.getcwd() + '/pictures')
        self.Pfade = []
        for i in self.BilderListeVorlaeufer:
            Pfad = os.path.join('pictures', i)
            if os.path.isfile(Pfad) == True:
                self.Pfade.append(Pfad)
        self.HauptCarousel = Carousel(scroll_timeout = 100)
        App.Pfade = self.Pfade
        self.add_widget(self.HauptCarousel)
        ####################################################################################################
        ### Erste Seite im HauptCarousel momentan mit den produktbildern
        self.HauptCarousel.FloatLayout = FloatLayout()
        self.HauptCarousel.add_widget(self.HauptCarousel.FloatLayout)
        self.HauptCarousel.FloatLayout.GridLayout = GridLayout(cols=3, pos_hint={'x': 0,'y': 0}, size_hint=[1,0.9])
        self.HauptCarousel.FloatLayout.add_widget(self.HauptCarousel.FloatLayout.GridLayout)
        for i in range(2):
            button = Button(background_normal = self.Pfade[i], background_down= 'bilder_oberflaeche/1361740537_Ball Green_mitHaken.png', mipmap= True)
            self.HauptCarousel.FloatLayout.GridLayout.add_widget(button)
##        self.HauptCarousel.FloatLayout.GridLayout.add_widget(Button(text='test'))
##        self.HauptCarousel.FloatLayout.GridLayout.add_widget(Button(text='test2'))

        #####################################################################################################
        ### 2 Seite im Hauptcarousel mit testbutton zur datei Erstellung
        ### 2 Page in MainCarousel with testbutton for creating /exporting to a file
        self.HauptCarousel2 = BoxLayout(orientation='vertical')
        ###self.HauptCarousel.add_widget(self.HauptCarousel2)
        self.HauptCarousel2.Texteingabe = TextInput(multiline=True)
        self.HauptCarousel2.add_widget(self.HauptCarousel2.Texteingabe)

        self.HauptCarousel2.ButtonSchreiben = Button(text="datei schreiben", on_release = self.datenpickeln)
        self.HauptCarousel2.add_widget(self.HauptCarousel2.ButtonSchreiben)
        #######################################################################
        ### 3 Seite im Hauptcarousel momentan mit Datei Auslesefunktion
        ### 3 Page in MainCarousel atm with functionality to read from file
        self.HauptCarousel3 = BoxLayout(orientation='vertical')
        ###self.HauptCarousel.add_widget(self.HauptCarousel3)
        self.HauptCarousel3.Textausgabe = TextInput(multiline=True, readonly = True)
        self.HauptCarousel3.add_widget(self.HauptCarousel3.Textausgabe)

        self.HauptCarousel3.ButtonLesen = Button(text="datei auslesen", on_release = self.datenentpickeln)
        self.HauptCarousel3.add_widget(self.HauptCarousel3.ButtonLesen)
        #######################################################################
        ### 4 Seite im Hauptcarousel momentan mit Tischmanager
	### 4 Page in Maincarousel atm with some kind of Table Manager
        BackgroundcolorListe = [(1,0,0,1),(0,1,0,1),(0,0,1,1),(1,1,0,1)]
        self.CustomLayout = CustomLayout()
        self.HauptCarousel.add_widget(self.CustomLayout)
        #self.CustomLayout.TopLabel = Label(text = 'Tisch[sup][color=#098125ff]Organizer[/sup][/b][/color]',  markup = True,
                                            #halign= 'left', valign= 'top', text_size= self.size, pos_hint={'x':0, 'y': 0}, font_size= '30sp')
        self.CustomLayout.TopLabel = Label(text = 'Tisch[sup][color=18ea1d]Organizer[/sup][/b][/color]',  markup = True,  # alte farbe: #098125ff
                                           halign= 'left',  font_size= '30sp')
        #self.CustomLayout.add_widget(self.CustomLayout.TopLabel)
        self.CustomLayout.BoxLayout = BoxLayout (orientation = 'horizontal', size_hint = [1,0.05], pos_hint={'x':0, 'y': 0.95})
        self.CustomLayout.add_widget(self.CustomLayout.BoxLayout)
        self.CustomLayout.BoxLayout.add_widget(self.CustomLayout.TopLabel)
        ButtonMenu1 = self.DropdownbuttonCreator()
        
        self.CustomLayout.BoxLayout.Button1 = ButtonMenu1
##        self.CustomLayout.BoxLayout.Button2 = Button(text = 'Tisch+' , on_release = self.tischhinzufuegen)
##        self.CustomLayout.BoxLayout.Button3 = Button(text = 'Spalte+', on_release = self.spaltehinzufuegen)
##        self.CustomLayout.BoxLayout.Button4 = Button(text = 'Zeile+', on_release = self.zeilehinzufuegen)
        self.CustomLayout.BoxLayout.add_widget(self.CustomLayout.BoxLayout.Button1)
##        self.CustomLayout.BoxLayout.add_widget(self.CustomLayout.BoxLayout.Button2)
##        self.CustomLayout.BoxLayout.add_widget(self.CustomLayout.BoxLayout.Button3)
##        self.CustomLayout.BoxLayout.add_widget(self.CustomLayout.BoxLayout.Button4)
        self.CustomLayoutGridLayout = GridLayout(cols = 3, rows = 4, padding = [20,20], spacing = [30,30], size_hint = [1,0.95], pos_hint={'x':0, 'y': 0})
        #cGridLayout = StackLayout(orientation = "tb-lr", padding = [20,20], spacing = [30,30], size_hint = [1,0.9], pos_hint={'x':0, 'y': 0})

        self.CustomLayout.add_widget(self.CustomLayoutGridLayout)
        self.Tischliste = []
        
        Auswahlliste = ["Bestellung", "Abrechnung", "Best. Aendern", "Bennenen"]
        
        AnzahlTische = 12
        Zielwidget = self.CustomLayoutGridLayout
        self.tischerstellung(Zielwidget,AnzahlTische, Auswahlliste, BackgroundcolorListe)
       
        self.Box=BoxLayout(oreintation='vertical')
        self.CustomScrollviewProduktOrganizerInstanz = CustomScrollviewProduktOrganizer()      #########
                                             #########
        self.ProduktOrganizerInstanz = ProduktOrganizer()
        self.ProduktOrganizerInstanz.ids.SpinnerProduktOrganizer.bind(text=self.produktorganizerfilter)
        self.Box.add_widget(self.ProduktOrganizerInstanz)
        self.ProduktOrganizerInstanz.ids.custScrlInst.data = App.HauptListeDictonaries
        self.HauptCarousel.add_widget(self.Box)
        #self.HauptCarousel.add_widget(self.ProduktOrganizerInstanz)
        self.ButtonHinzufuegen = self.ProduktOrganizerInstanz.ids.ProduktlisteButtonHinzufuegen
        self.ButtonHinzufuegen.on_release = self.produkthinzufuegen

        self.PopupDateiAuswaehlenInst= PopupDateiAuswaehlenProduktorganizer()
        PopupDateiauswahl = self.PopupDateiAuswaehlenInst.ids.b.ids.a
        self.LadeButton = self.ProduktOrganizerInstanz.ids.LadeButton
        self.LadeButton.on_release = PopupDateiauswahl.open
        self.PopupDateiAuswaehlenInst.ids.b.ids.OkButtonFilechooser.on_release = self.datenentpickeln
        self.PopupDateiAuswaehlenInst.ids.b.ids.LayoutPopup.add_widget(Label
                                                                       (text='[b][color=ff3333]Achtung, nicht gespeicherte Eingaben gehen verloren![/b][/color]',
                                                                        size_hint= (1,0.1),
                                                                        markup = True,
                                                                        font_size = 14))

        self.PopupDateiAuswaehlenSpeichernInst = PopupDateiAuswaehlenProduktorganizer()
        PopupDateiauswahlSpeichern = self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.a
        
        
        self.SpeicherButton = self.ProduktOrganizerInstanz.ids.SpeicherButton
        self.SpeicherButton.on_release = PopupDateiauswahlSpeichern.open
        self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.OkButtonFilechooser.on_release = self.datenpickeln
        
        
        
       
        
        
        

        #print 'tempChildernListe',TempChildrenList
        
        #self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.LayoutPopup.add_widget(TextInput(multiline=False, size_hint= (1,0.15)))
        self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.LayoutPopup.add_widget(Label
                                                                       (text='[b][color=ff3333]Achtung, der Inhalt der Datei wird ueberschrieben![/b][/color]',
                                                                        size_hint= (1,0.1),
                                                                        markup = True,
                                                                        font_size = 14))
        TempChildrenList = []
        for q in self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.LayoutPopup.children:
            TempChildrenList.append(q)
        
        
            
        self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.LayoutPopup.clear_widgets()
        
        FileSaveLabelTextInput = Label(text='Zur Erstellung einer neuen Datei,einen Namen angeben',size_hint= (1,0.15), font_size=16)
        self.FileSaveTextInput = TextInput(multiline=False,size_hint= (1,0.15))

        
        TempChildrenList.sort(reverse=True)

        print "vor dem Einfuegen"
        for index, item in enumerate(TempChildrenList):
                print index, item
        
        TempChildrenList.insert(2, FileSaveLabelTextInput)
        TempChildrenList.insert(3, self.FileSaveTextInput)
        
        for i in TempChildrenList:
            #i.parent = None
            self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.LayoutPopup.add_widget(i)

        print "nach dem Einfuegen und sortieren"
            
        for index, item in enumerate(TempChildrenList):
                print index, item
        
        
        
        #self.LadeButton.bind(on_release = self.datenentpickeln)
        Spinner =self.ProduktOrganizerInstanz.ids.SpinnerProduktOrganizer
        SpinnerText = Spinner.text
        self.LadeButton.bind(on_release = self.produktorganizerfilter)

        #self.ButtonHinzufuegen.on_release = self.inputdata

        #self.Box.add_widget(Button(size_hint= (1,0.1),text='inputdata', on_release=self.inputdata))

                                            

        
        self.PopupInst = PopupBildAuswaehlenProduktorganizer()
        popup = self.PopupInst.ids.a
        self.ProduktOrganizerInstanz.ids.ProduktBildAuswaehlen.on_release = popup.open


        self.PersonalOrganizerInstanz = PersonalOrganizer()
        self.HauptCarousel.add_widget(self.PersonalOrganizerInstanz)

        self.ZeitOrganizerInstanz = ZeitOrganizer()
        self.HauptCarousel.add_widget(self.ZeitOrganizerInstanz)

##    def inputdata(self):
##        print 'inputdadat runs'
##        #self.CustomScrollviewProduktOrganizerInstanz.data = [str(i) for i in range(5)]
##        self.ProduktOrganizerInstanz.ids.custScrlInst.data = [str(i) for i in range(5)]
      
        
   
        
    def produkthinzufuegen(self):
        #App.AuswahlHauptlisteAlt = App.AuswahlHauptliste
        NeuesDict ={}
    
        WertEingabeFeldBezeichnung = self.ProduktOrganizerInstanz.ids.EingabeFeldBezeichnung.text
        WertEingabeFeldPreis = self.ProduktOrganizerInstanz.ids.EingabeFeldPreis.text
##        StatusCheckBoxVerkauf = self.ProduktOrganizerInstanz.ids.CheckBoxVerkauf.active
        WertSpinnerKategorie = str(self.ProduktOrganizerInstanz.ids.SpinnerKategorie.text)
        filechooser = self.PopupInst.ids.filechooser
        DateiAuswahl = (str(filechooser.selection))[((str(filechooser.selection)).find('pictures')):-2]
        #print 'hallo', WertEingabeFeldBezeichnung, WertEingabeFeldPreis,DateiAuswahl,WertSpinnerKategorie
        ID = len(App.HauptListeDictonaries)
        NeuesDict = {'ID': ID,
                     'Bezeichnung':WertEingabeFeldBezeichnung,
                     'Preis':WertEingabeFeldPreis,
                     'Bild':DateiAuswahl,
                     'Kategorie':WertSpinnerKategorie}

        #print 'len(App.HauptListeDictonaries)', (len(App.HauptListeDictonaries))
##        if len(App.HauptListeDictonaries)<1:
##            App.HauptListeDictonaries.append(NeuesDict)
##            print 'Fall 1'
##        else:
        Treffer = False
        for i in range(len(App.HauptListeDictonaries[:])):
            print 'App.HauptListeDictonaries[i][Bezeichnung] ist', App.HauptListeDictonaries[i]['Bezeichnung']
            Bezeichnungdict = str(App.HauptListeDictonaries[i]['Bezeichnung'])
            Bezeichnungneuesdict = str(NeuesDict['Bezeichnung'])
            if Bezeichnungdict  == Bezeichnungneuesdict:
               
                Treffer = True
                break
            else:
                Treffer = False
        if Treffer == True:
            #print 'Dieses Produkt existiert schon'
            ButtonVerstanden = Button(text='Verstanden')
            popup = Popup(title='Dieses Produkt existiert bereits ',
                          size_hint = (0.5, 0.25),
                          content= ButtonVerstanden)
            popup.open()
            ButtonVerstanden.on_release = popup.dismiss
        else:
            App.HauptListeDictonaries.append(NeuesDict)
            
            #self.ProduktOrganizerInstanz.ids.custScrlInst.ids.content2.clear_widgets()
##            print len(App.HauptListeDictonaries)
##            for index, item in enumerate(App.HauptListeDictonaries):
##                print index, item

                


            #self.ProduktOrganizerInstanz.ids.custScrlInst.data = App.HauptListeDictonaries
            #self.ProduktOrganizerInstanz.ids.custScrlInst.data  = App.AuswahlHauptliste
            #AktuelleWidgetsInDerListe = self.ProduktOrganizerInstanz.ids.custScrlInst.ids.content2.children
            #print 'App.AuswahlHauptlisteAlt', App.AuswahlHauptlisteAlt
            #AktuelleWidgetsInDerListe = self.CustomScrollviewProduktOrganizerInstanz.ids.content2.children
            #print AktuelleWidgetsInDerListe
            
            #self.ProduktOrganizerInstanz.ids.custScrlInst.ids.content2.add_widget(Button(text='testmanuellereinfuegung'))
            
            AktuellerSpinnerWert = self.ProduktOrganizerInstanz.ids.SpinnerProduktOrganizer.text
            self.ProduktOrganizerInstanz.ids.custScrlInst.ids.content2.clear_widgets()
            
            App.AuswahlHauptliste = []    
            if AktuellerSpinnerWert == 'Alle':
                #self.CustomScrollviewProduktOrganizerInstanz.ids.content2.clear_widgets()
                print 'haha'
                App.AuswahlHauptliste = []
                for i in App.HauptListeDictonaries:
                    if i not in App.AuswahlHauptlisteAlt:
                        pass
                        
                        App.AuswahlHauptliste = App.HauptListeDictonaries
                        App.AuswahlHauptlisteAlt = []
                
            else:
                if self.SpinnerButtonZustand == 'Alle':
                    App.AuswahlHauptlisteAlt = []
                else:
                    pass
                
                for i in App.HauptListeDictonaries:
                    if i not in App.AuswahlHauptlisteAlt:
                        if i['Kategorie'] == AktuellerSpinnerWert:
                             
                            App.AuswahlHauptliste.append(i)
                        else:
                            continue
                    else:
                        continue

            self.ProduktOrganizerInstanz.ids.custScrlInst.data  = App.AuswahlHauptliste

    def produktorganizerfilter(self,  spinner, text='Alle'):
        spinner =self.ProduktOrganizerInstanz.ids.SpinnerProduktOrganizer
        
        text = spinner.text
        
        self.ProduktOrganizerInstanz.ids.custScrlInst.data = []
        #print 'produktorganizerfilter, App.AuswahlHauptlisteAlt', App.AuswahlHauptlisteAlt
        
        if self.SpinnerButtonZustand == 'Alle':
            App.AuswahlHauptlisteAlt = []
        else:
            App.AuswahlHauptlisteAlt = App.AuswahlHauptliste

        #custScrlInst
        self.ProduktOrganizerInstanz.ids.custScrlInst.ids.content2.clear_widgets()
        #self.CustomScrollviewProduktOrganizerInstanz.ids.content2.clear_widgets()
        App.AuswahlHauptliste=[]
        if text == 'Alle':
            
           App.AuswahlHauptliste = App.HauptListeDictonaries
           self.SpinnerButtonZustand = 'Alle'
           if self.ProduktOrganizerInstanz.ids.custScrlInst.data == App.AuswahlHauptliste:
               self.ProduktOrganizerInstanz.ids.custScrlInst.data = []
           
           
        else:
            self.SpinnerButtonZustand = 'Anders'
            for i in App.HauptListeDictonaries:
                if i not in App.AuswahlHauptlisteAlt: 
                    #print i['Kategorie']
                    if i['Kategorie'] == text:
                        App.AuswahlHauptliste.append(i)
                    else:
                        continue
                else:
                    continue

            
                

        #print 'Auswahl Hauptliste ist nun', App.AuswahlHauptliste
        self.ProduktOrganizerInstanz.ids.custScrlInst.data = App.AuswahlHauptliste

                
                
            

       
                    
   

        
        
        
        




    def DropdownbuttonCreator(self):
        Auswahlliste = ["Tisch +", "Tisch -", "Spalte + ", "Spalte -", "Reihe + ", "Reihe -"]
        BackgroundcolorListe = [(0,1,0,1),(1,0,0,1),(0,1,0,1),(1,0,0,1),(0,1,0,1),(1,0,0,1)]
        Aktionsliste = [self.tischhinzufuegen, self.tischentfernen, self.spaltehinzufuegen, self.spalteentfernen, self.zeilehinzufuegen, self.zeileentfernen]
        DropdownObjekt = CustomDropDown()
        DropdownObjektButton = CustomButton(text = "Menue",
        #DropdownObjektButton = ToggleButton(text="Menue",
                                            size_hint=[1,1],
                                            background_color = (0.8, 0.8, 0.00, 1),
                                            background_normal='bilder_oberflaeche/white2.png',
                                            background_down='bilder_oberflaeche/white3.png')
        #self.CustomLayout.add_widget(DropdownObjektButton)
        DropdownObjektButton.bind(on_release=DropdownObjekt.open)
        self.DropdownObjects.append(DropdownObjekt)
        for x in range(len(Auswahlliste)):

                DropdownUnterbutton = Button(text=Auswahlliste[x], font_size = 15, size_hint_y=None, height=60,
                                             background_color = BackgroundcolorListe[x],
                                             background_normal='bilder_oberflaeche/white2.png',
                                             background_down='bilder_oberflaeche/white3.png',
                                             opacity = 0.8,
                                             on_release = Aktionsliste[x])
                DropdownObjekt.add_widget(DropdownUnterbutton)

        
        ButtonMenu1 = DropdownObjektButton
        return ButtonMenu1 


        
    def tischerstellung (self, Zielwidget, AnzahlTische, Auswahlliste, BackgroundcolorListe):
        Auswahlliste = ["Bestellung", "Abrechnung", "Best. Aendern", "Bennenen"]
        BackgroundcolorListe = [(1,0,0,1),(0,1,0,1),(0,0,1,1),(1,1,0,1)]
        Aktionsliste = [self.bestellung, self.abrechnung, self.bestellungaendern, self.tischbenennen]
        
        #self.DropdownObjects = []
        for i in range(AnzahlTische):
            if self.Tischliste != []:
                LetzterTisch = self.Tischliste[-1]['Nummer']
##                print LetzterTisch + 1
            else:
                LetzterTisch = 0
            
            TischNr = str(LetzterTisch+1)
            TischButtonText = "T " + TischNr
            DropdownObjekt = CustomDropDown() #von kovak hinzugefuegt
            #DropdownObjektButton = CustomButton(text = TischButtonText,
            DropdownObjektButton = ToggleButton(text = TischButtonText,
                                                group='Tische',
                                                #background_normal='bilder_oberflaeche/white2.png',
                                                background_normal='bilder_oberflaeche/buttonbackground_normal_gruenrandaussenbraun.png',
                                                background_down='bilder_oberflaeche/buttonbackground_normal_weissrandaussenbraun.png',
                                                #background_down='bilder_oberflaeche/white4.png',
                                                #background_color = (0.79, 0.39, 0.09, 1))#0.6))
                                                background_color = (1, 1, 1, 1))#0.6))
            Zielwidget.add_widget(DropdownObjektButton)
            DropdownObjektButton.bind(on_release=DropdownObjekt.open)
            self.DropdownObjects.append(DropdownObjekt) #von kovak hinzugefuegt

            for x in range(len(Auswahlliste)):

                DropdownUnterbutton = Button(text=Auswahlliste[x],
                                             id = TischNr,
                                             #auto_width='False',
                                             #width = '200sp',
                                             font_size = 15,
                                             size_hint_y=None,
                                             height=60,
                                             background_normal='bilder_oberflaeche/white2.png',
                                             background_down='bilder_oberflaeche/white3.png',
                                             background_color = BackgroundcolorListe[x],
                                             on_release = Aktionsliste[x])
                DropdownObjekt.add_widget(DropdownUnterbutton)

                #print' button', i, 'unterbutton', x



            DropdownObjektButton.text= TischButtonText
            self.TischButtondict = {'Nummer':(LetzterTisch + 1),'Objekt':DropdownObjektButton}
            self.Tischliste.append(self.TischButtondict)
            
        
    def garbagecollectortracking(self, widget):
        for i in self.Tischliste:
            a = i
            print gc.is_tracked(a)
        
        
### function for Editing a Table#######################################
    #def tischmanipulieren(self, widget):
     #   widget.text = 'mein text'
        
#### function for adding an extra table to layout ##########################

    def tischhinzufuegen(self, widget):
        
        if len(self.Tischliste) >= 1:
            if hasattr(self, 'CustomLayoutBottomLabel'):
                self.CustomLayout.remove_widget(self.CustomLayoutBottomLabel)
               
            
        AnzahlTische = 1
        Zielwidget = self.CustomLayoutGridLayout
        Auswahlliste = ["Bestellung", "Abrechnung", "Best. Aendern", "Bennenen"]
        BackgroundcolorListe = [(1,0,0,1),(0,1,0,1),(0,0,1,1),(1,1,0,1)]
        LetzterTisch = self.Tischliste[-1]['Nummer']
        if (self.CustomLayoutGridLayout.cols * self.CustomLayoutGridLayout.rows) <= (LetzterTisch +1):
            self.CustomLayoutGridLayout.rows = self.CustomLayoutGridLayout.rows + 1
        self.tischerstellung(Zielwidget, AnzahlTische, Auswahlliste, BackgroundcolorListe)

    def tischentfernen(self, widget):
        self.Warnlabel = 0 
        if len(self.Tischliste) <= 1:
            if hasattr(self, 'CustomLayoutBottomLabel'):
                # obj.attr_name exists.
                
                if self.CustomLayoutBottomLabel in self.CustomLayout.children:
                    self.Warnlabel=1    
            print 'das ist der Letzte Tisch, der kann nicht entfernt werden'
            if self.Warnlabel == 0:
                
                self.CustomLayoutBottomLabel= Label(text='Das ist der Letzte Tisch,\n der kann nicht \n entfernt werden', text_size = self.size)
                self.CustomLayout.add_widget(self.CustomLayoutBottomLabel)
            
        else:
            Zielwidget = self.CustomLayoutGridLayout
            Zielwidget.remove_widget(self.Tischliste[-1]['Objekt'])
            
            del self.Tischliste[-1]
            LetzterTisch = self.Tischliste[-1]['Nummer']
            print 'die anzahl der Tische ist nun:', LetzterTisch
        
        

        
        pass
#### function for adding a column to layout ####################################

    def spaltehinzufuegen(self, widget):
        if self.CustomLayoutGridLayout.cols >= 1:
            if hasattr(self, 'CustomLayoutBottomLabel'):
                self.CustomLayout.remove_widget(self.CustomLayoutBottomLabel)
                self.WarnLabel = 0 
        self.CustomLayoutGridLayout.cols = self.CustomLayoutGridLayout.cols + 1
        print 'Zeile hinzufuegen'
        

    def spalteentfernen(self, widget):
        self.Warnlabel = 0
        if self.CustomLayoutGridLayout.cols <= 1:
            if hasattr(self, 'CustomLayoutBottomLabel'):
                # obj.attr_name exists.
                if self.CustomLayoutBottomLabel in self.CustomLayout.children:
                    self.Warnlabel=1    
            print 'das ist die letzte Tischreihe, sie kann nicht entfernt werden'
            if self.Warnlabel == 0:
                
                self.CustomLayoutBottomLabel= Label(text='Das ist die letzte Tischreihe,\n sie kann nicht \n entfernt werden', text_size = self.size)
                self.CustomLayout.add_widget(self.CustomLayoutBottomLabel)

        else:
            TischanzahlVerbleibend = (self.CustomLayoutGridLayout.cols -1) * self.CustomLayoutGridLayout.rows
                           
            for i in range(len(self.Tischliste[TischanzahlVerbleibend:])):
                self.CustomLayoutGridLayout.remove_widget(self.Tischliste[TischanzahlVerbleibend+ i]['Objekt'])
                
            del self.Tischliste[TischanzahlVerbleibend:]
            self.CustomLayoutGridLayout.cols = self.CustomLayoutGridLayout.cols - 1

       
#### function for adding a row to layout ####################################

    def zeilehinzufuegen(self, widget):
        if self.CustomLayoutGridLayout.rows >= 1:
            if hasattr(self, 'CustomLayoutBottomLabel'):
                self.CustomLayout.remove_widget(self.CustomLayoutBottomLabel)
                self.WarnLabel = 0 
        self.CustomLayoutGridLayout.rows = self.CustomLayoutGridLayout.rows + 1
        print 'Zeile hinzufuegen'
        

        

    def zeileentfernen(self, widget=None):
        self.Warnlabel = 0
        if self.CustomLayoutGridLayout.rows <= 1:
            if hasattr(self, 'CustomLayoutBottomLabel'):
                # obj.attr_name exists.
                if self.CustomLayoutBottomLabel in self.CustomLayout.children:
                    self.Warnlabel=1    
            print 'das ist die letzte Tischreihe, sie kann nicht entfernt werden'
            if self.Warnlabel == 0:
                
                self.CustomLayoutBottomLabel= Label(text='Das ist die letzte Tischreihe,\n sie kann nicht \n entfernt werden', text_size = self.size)
                self.CustomLayout.add_widget(self.CustomLayoutBottomLabel)

        else:
            TischanzahlVerbleibend = (self.CustomLayoutGridLayout.rows -1) * self.CustomLayoutGridLayout.cols
                           
            for i in range(len(self.Tischliste[TischanzahlVerbleibend:])):
                self.CustomLayoutGridLayout.remove_widget(self.Tischliste[TischanzahlVerbleibend+ i]['Objekt'])
                
            del self.Tischliste[TischanzahlVerbleibend:]
            self.CustomLayoutGridLayout.rows = self.CustomLayoutGridLayout.rows - 1

    
        
    def bestellung(self, widget):
        App.my_index = -1
        
        TischNr = widget.id
        PopupFloatLayout = FloatLayout(size_hint=(1, 1))
        
        self.PopupScrollview = CustomScrollviewPopupContent()
        self.PopupScrollviewItem = CustomButton2()
        
        App.AuswahlHauptliste = App.HauptListeDictonaries
        self.PopupScrollview.data = App.AuswahlHauptliste
        
        
        #content = self.PopupScrollview.ids.content
        #item = self.PopupScrollviewItem
               
        popup = Popup(title='Bestellung für Tisch ' + str(TischNr),
                      content= PopupFloatLayout)
       
             

        BoxTop = BoxLayout(size_hint= [0.52,0.065],pos_hint={'x': 0.5, 'y': 1.005}, spacing = 5)
        ButtonExit = Button(text="Exit",
                            #pos_hint={'x': 0.825, 'y': 1.005},
                            #size_hint = [0.2,0.065],
                            size_hint = [0.3,1],
                            #on_release = self.zeromyindex,
                            
                            on_release = popup.dismiss)
        #myindexzero = 0
        #ButtonExit.bind(on_release=ButtonExit.setter('myindexzero'))
        #print App.my_index

        self.ButtonSpinner =Spinner(text= "Alle",
                               values= ("Mittag-Essen", "Getraenke", "AlcGetraenke", "Essen Alltime", "Alle"),
                               size_hint= [0.7,1],
                               #pos_hint={'x': 0.625, 'y': 1.005}
                               )
        self.ButtonSpinner.bind(text=self.show_selected_value)        
        #halign: 'right'
        #valign: 'top'

        #PopupFloatLayout.add_widget(ButtonExit)
        #PopupFloatLayout.add_widget(ButtonSpinner)
        
        BoxTop.add_widget(self.ButtonSpinner)
        BoxTop.add_widget(ButtonExit)
        PopupFloatLayout.add_widget(BoxTop)
        
        self.PopupScrollview.size_hint = [1.05,1.017]
        self.PopupScrollview.center = popup.center
        PopupFloatLayout.add_widget(self.PopupScrollview)
        for i in App.ScrollviewButtons:
            i.ids.customID.on_release = self.Optionsfenster
        
       
        popup.open()
        print App.ScrollviewButtons
    
        

##        
##    def on_data(self, instance, value):
##        content_add = self.PopupScrollview.ids.content.add_widget
##        for item in value:
##            print item
##            content_add(CustomButton2(text=item))

        #return CustomScrollviewPopupContent()

        
    def show_selected_value(self, spinner, text):
        print 'The spinner', spinner, 'have text', text
        App.AuswahlHauptliste=[]
        if text == 'Alle':
            App.AuswahlHauptliste = App.HauptListeDictonaries
            self.PopupScrollview.data = App.AuswahlHauptliste
        else:
            for i in App.HauptListeDictonaries:
                if i['Kategorie'] == text:
                    App.AuswahlHauptliste.append(i)
                else:
                    continue

            self.PopupScrollview.data = App.AuswahlHauptliste
        
            
    

   


        
    def zeromyindex(self, widget):
        App.my_index = (-1)
        

    def Optionsfenster(self):
        self.OptionenPopupBestellungen = OptionenPopupBestellungen()
        
        print 'App.AktuelleBestellungProduktAnzahlzaehler', App.AktuelleBestellungProduktAnzahlzaehler
        for i in range(App.AktuelleBestellungProduktAnzahlzaehler):
            self.OptionenPopupBestellungen.ids.OptionsPopupContent.add_widget(ToggleButton(text=i))

        self.OptionenPopupBestellungen.open()
        
        
            
            
               

        

    def groesse(self,widget):
        print 'die buttongroesse ist:', widget.size

    

    def abrechnung(self, widget):
        TischNr = widget.id
        PopupFloatLayout = FloatLayout()       
        self.ScreenmanagerPopup = CustomScreenManager()
        self.ScreenPopup = CustomScreen
        
        for x in xrange(4):
            self.ScreenmanagerPopup.add_widget(self.ScreenPopup(name='Screen %d' % x))
        #popup = Popup(title='Abrechnung für ' + str(TischNr),
        #              content=self.ScreenmanagerPopup,size_hint=(1, 1) )
        popup = Popup(title='Abrechnung für Tisch' + str(TischNr),
                      content=PopupFloatLayout)#,
                      #size_hint=(1, 1),
                      #pos_hint={'x': 0.5, 'y': 0.5} )

        self.ScreenmanagerPopup.pos_hint = {'x': 0, 'y': 0} 
        PopupFloatLayout.add_widget(self.ScreenmanagerPopup)

        ButtonExit = Button(text="Exit",
                            pos_hint={'x': 0.8, 'y': 1.005},
                            size_hint = [0.2,0.065],
                            on_release = popup.dismiss)
        PopupFloatLayout.add_widget(ButtonExit)

        popup.open()
        

    def bestellungaendern(self, widget):
        pass

    def tischbenennen(self, widget):
        TischNr = widget.id
        PopupBox1LayoutTischBennenen = BoxLayout(orientation = 'vertical')
        popup = Popup(title='Tisch Nr. ' + str(TischNr) + 'benennen',
                      content=PopupBox1LayoutTischBennenen,
                      size_hint=(0.75, 0.5))
        EingabeTextfeld = TextInput(text='hier Tischbezeichnung eintragen - Funktion muss noch eingebaut werden')            
        PopupBox1LayoutTischBennenen.add_widget(EingabeTextfeld)
        PopupBoxLayoutTischBenennen = BoxLayout(orientation = 'horizontal', size_hint=(1,1))
        ButtonAbbrechenTischBenennen = Button(text="Abbrechen", size_hint=(0.5, 0.5))
        ButtonAbbrechenTischBenennen.bind(on_press=popup.dismiss)
        ButtonOkTischBenennen = Button(text="OK", size_hint=(0.5, 0.5))
        ButtonOkTischBenennen.bind(on_press=popup.dismiss)
        PopupBox1LayoutTischBennenen.add_widget(PopupBoxLayoutTischBenennen)
        PopupBoxLayoutTischBenennen.add_widget(ButtonAbbrechenTischBenennen)
        PopupBoxLayoutTischBenennen.add_widget(ButtonOkTischBenennen)
        #popup.add_widget
        popup.open()
        
        pass

      



#### function for exporting Data to file ####################################

    def datenpickeln(self):
        
        filechooser = self.PopupDateiAuswaehlenSpeichernInst.ids.b.ids.filechooser
        AusgewaehlteDatei = str(filechooser.selection)
        AusgewaehlteDatei = (AusgewaehlteDatei)[AusgewaehlteDatei.find('Produktlisten'):-2]
        if self.FileSaveTextInput.text != '':
            print 'Du hast einen Dateinamen eingegeben'
            AusgewaehlteDatei = 'Produktlisten/'+(str(self.FileSaveTextInput.text))
        print 'Daten Speichern ausgefuehrt'
        print AusgewaehlteDatei
        SicherungsItem1 = self.HauptCarousel2.Texteingabe.text
        SicherungsItem2 = App.HauptListeDictonaries
        Sicherungsliste = [SicherungsItem1, SicherungsItem2]
        
        '''function to pickle data to make it ready for sending'''
        try:
            with open(AusgewaehlteDatei, 'w+b') as SicherungslisteDaten_File:
                pickle.dump(Sicherungsliste, SicherungslisteDaten_File)
        except IOError as err:
            print('Dateifehler: ' + str(err))
        except pickle.PickleError as perr:
            print('Pickling Fehler: ' + str(perr))

	#### function for importing Data to file ####################################

    def datenentpickeln(self):
        filechooser = self.PopupDateiAuswaehlenInst.ids.b.ids.filechooser
        AusgewaehlteDatei = str(filechooser.selection)
        print 'Daten Laden ausgefuehrt'
        print AusgewaehlteDatei
        AusgewaehlteDatei = (AusgewaehlteDatei)[AusgewaehlteDatei.find('Produktlisten'):-2]
        #App.datenentpickeln = self(datenentpickeln(widget = None))
        with open(AusgewaehlteDatei, 'rb') as SicherungslisteDaten_File_entpickelt:
            SicherungslisteWiederhergestellt = pickle.load(SicherungslisteDaten_File_entpickelt)
            #self.HauptCarousel3.Textausgabe.text = SicherungslisteWiederhergestellt[0]
            App.HauptListeDictonaries = SicherungslisteWiederhergestellt[1]
##            App.AuswahlHauptListe = App.HauptListeDictonaries
##            self.ProduktOrganizerInstanz.ids.custScrlInst.data = App.AuswahlHauptListe
        self.produktorganizerfilter(self) 
        print 'die daten wurden wieder hergestellt'

       

class CustomDropDown(DropDown):
    def open(self, instance):
        print 'opening dropdown', instance
        super(CustomDropDown, self).open(instance)

class CustomButton(Button):
    def on_release(self):
        print 'button release'
        super(CustomButton, self).on_release()


class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1,0,0,0.2) # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(
                            source='bilder_oberflaeche/tischmanagerboden1024_768.jpg',
                            size=self.size,
                            pos=self.pos)
            

        self.bind(
                    size=self._update_rect,
                    pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size




class BonierungsprogrammApp(App):
    print '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    App.my_index = -1
    App.my_index2 = -1
##    App.Pfade = 0
##    App.Namensliste = ['Cola','Wasser','Bier','Wein']
    
    #App.HauptListeDictonaries  = ListProperty([])
    App.AuswahlHauptliste = []
    App.HauptListeDictonaries = []
    App.BestellungslistenListe = []
    App.Bestellungsliste = [{'ProduktID':'plathalter'}]
    App.AktuelleBestellungsZaehler = 0
    App.AktuelleBestellungProduktAnzahlzaehler = 0
    
    #App.AktuelleBestellungProduktAnzahlzaehler = App.AktuelleBestellungProduktAnzahlzaehler    
    
    App.ScrollviewButtons = []
    App.AktuelleAuswahlBestellungsliste = ''
    
##    x = LoginScreen()
##    x2 = x.datenentpickeln(widget = None)
##    App.datenentpickeln = x2
##    TestDict = {'Bezeichnung':'testitem','Preis':'testpreis','Bild':'testpildbfad','Kategorie':'Testkategorie'}
##    App.HauptListeDictonaries.append(TestDict)
##    TestDict = {'Bezeichnung':'testitem2','Preis':'testpreis2','Bild':'testpildbfad2','Kategorie':'Testkategorie2'}
##    App.HauptListeDictonaries.append(TestDict)
##    TestDict = {'Bezeichnung':'testitem3','Preis':'testpreis3','Bild':'testpildbfad3','Kategorie':'Testkategorie3'}
##    App.HauptListeDictonaries.append(TestDict)
##    TestDict = {'Bezeichnung':'testitem4','Preis':'testpreis4','Bild':'testpildbfad4','Kategorie':'Testkategorie4'}
##    App.HauptListeDictonaries.append(TestDict)
    

##    def __init__(self, **kwargs):
##        pass
    

    def build(self):
        
        return LoginScreen()




if __name__ == '__main__':
    BonierungsprogrammApp().run()
