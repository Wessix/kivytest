# -*- coding: utf-8 -*-
import kivy
kivy.require('1.1.3')

import random
import os
import bubble


from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import Metrics
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scatter import Scatter
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.widget import Widget
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory




class Page(GridLayout):
    pass

class Showcase(FloatLayout):
    pass


class StandardWidgets(FloatLayout):

    value = NumericProperty(0)

    def __init__(self, **kwargs):
        super(StandardWidgets, self).__init__(**kwargs)
        Clock.schedule_interval(self.increment_value, 1 / 30.)

    def increment_value(self, dt):
        self.value += dt


class ComplexWidgets(FloatLayout):
    pass

class GridWidget(FloatLayout):
    ############################################################
    def testfunction(self):
        #print ShowcaseApp.BilderlisteVorlaeufer
        #print App.Pfade
        pass

##class testgridlayout(GridLayout):
##    pass


class ShowcaseApp(App):

##    def on_select_node(self, instance, value):
##        # ensure that any keybaord is released
##        self.content.get_parent_window().release_keyboard()
##
##        self.content.clear_widgets()
##        try:
##            w = getattr(self, 'show_%s' %
##                        value.text.lower().replace(' ', '_'))()
##            self.content.add_widget(w)
##        except Exception, e:
##            print e

    def on_pause(self):
        return True

    
    
    def build(self):
        App.BilderlisteVorlaeufer = []
        App.BilderlisteVorlaeufer = os.listdir(os.getcwd() + '/pictures')
        App.Pfade = []
        for i in App.BilderlisteVorlaeufer:
            pfad = os.path.join('pictures', i)
            App.Pfade.append(pfad)
        
        self.load_kv('showcase.kv') 
        root = self.root #= Carousel()
        test_grid_layout = root.ids.testgridlayout
        App.box_layout_s2 = root.ids.boxlayouts2
        App.test_grid_layout = test_grid_layout
        App.haupt_box_layout = root.ids.hauptboxlayout
        App.haupt_float_layout = root.ids.hauptfloatlayout
        
        #self.root.content = BoxLayout()
        
        #sc = Showcase()
        #sc.content.add_widget(root)
        
        root.add_widget(GridWidget())
        root.add_widget(StandardWidgets())
        root.add_widget(ComplexWidgets())

        
        self.BubbleShowcase_instance = bubble.BubbleShowcase()
        print 'huihuuhuhhuhuuhhu', root.children 
        
        #root.add_widget(button_inst) # that worked only wrong position
        #XPosition = 100
        #YPosition = 100
        for i in range(9):
            button = Button(background_normal = App.Pfade[i], background_down= 'pictures/bilder_oberflaeche/1361740537_Ball Green_mitHaken.png', mipmap= True)
            #button.bind(on_release=bubble.BubbleShowcase.show_bubble)
            
            test_grid_layout.add_widget(button)
            button.bind(on_release=self.bubble_anzeigen)
        
            
            
            #button_to_window = button.to_window(button.x,button.y, initial=True, relative=False)
            #button_to_parent = button.to_window(button.x,button.y, relative=False)
            #button_to_widget = button.to_widget(button.x,button.y, relative=False)
            #button_to_local = button.to_local(button.x,button.y, relative=False)
            #print button.pos
            #print button_to_window
            #print button_to_parent
            #print button_to_widget
            #print button_to_local
            
            #button_inst = Button()
            #button_inst = Factory.ImageButton()
            #button_inst.source = App.Pfade[i]
            #test_grid_layout.add_widget(button_inst))
            

        #test_grid_layout2.add_widget(button_inst)
        
        
          #########  This is what i tried, but it is not working yet
        # should now work, you passed your App class, the App instance here is self (because we are in the class :D) 
        #root.content.ids.testgridlayout.add_widget(button_inst)
        #return sc
        
        
        #return root
##    def testfunction(self):
##        print 'ahahah'
##        
##        
##        return root

    def bubble_anzeigen(self, widget):
        #print dir(ShowcaseApp.build)
        window = widget.get_root_window()
        #print window.uid
        print dir(App)
        #print App.get_running_app()
        Hauptapp = ShowcaseApp()
        bubble.BubbleShowcase.show_bubble(self.BubbleShowcase_instance, App.haupt_float_layout, widget.pos, Hauptapp)
        #App.button_position = widget.pos
        
    def show_standard_widgets(self):
        return StandardWidgets()

    def show_complex_widgets_1(self):
        return ComplexWidgets()

    def show_gridwidget(self):
        return GridWidget()
    
    def bubbleentfernen(self, zielwidget,bubb):
        print 'bubblentfernen wird ausgefuert'
        print zielwidget.children[0].children[0].children[0].children
        print 'parent1',bubb.get_parent_window()
        bubb.parent = None
        bubb.parent = zielwidget
        print 'parent2',bubb.get_parent_window()
        #remove_widget(bubb)
        #zielwidget.remove_widget(bubb)
        #zielwidget.clear_widgets()
        

       


if __name__ == '__main__':
    ShowcaseApp().run()
