from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.factory import Factory
#from kivy.uix.popup import Popup

from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('scrollview.kv')

class CustomScrollviewPopupContent(BoxLayout):
        
    data = ListProperty([])
    
    
    def on_data(self, instance, value):
        
        content_add = self.ids.content.add_widget
        self.ids.content.clear_widgets()
        print 'vor der Schleife app.my_index',App.my_index
        print 'len(app.Pfade)', len(App.Pfade) 
        
        for item in value:
            App.my_index = item
            print 'in der S app.my_index',App.my_index
            
            content_add(CustomButton2(height=25))
            
class CustomButton2(BoxLayout):
        pass
