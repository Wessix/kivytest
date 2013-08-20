from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
Builder.load_file('screenmanager.kv')

class CustomScreenManager(ScreenManager):
	pass

class CustomScreen(Screen):
	hue = NumericProperty(1.0)
