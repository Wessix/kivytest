from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.factory import Factory
#from kivy.uix.popup import Popup

from kivy.uix.button import Button
from kivy.lang import Builder
Builder.load_file('scrollview.kv')

class CustomScrollviewPopupContent(BoxLayout):
        
    data = ListProperty([])
    
    
    def on_data(self, instance, value):
        content_add = self.ids.content.add_widget
        for item in value:
            
            content_add(CustomButton2(height=25))
class CustomButton2(BoxLayout):
        pass
