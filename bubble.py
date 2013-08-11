'''
Bubble
======

Test of the widget Bubble.
'''
#import main
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble

Builder.load_string('''
<cut_copy_paste>
    
    size_hint: (0.6, 0.6)
    #size: (260, 120)
    pos_hint: {'center_x': .5, 'y': .2}
    #pos_hint: {'center_x': 0, 'y': 0}
    #pos: 100,100
    background_image: 'pictures/white2.png'
    background_color: (1, 0, 0, 1)
    show_arrow: 'False'
    orientation: 'vertical'
    BubbleButton:
        text: 'Storno'
    BubbleButton:
        text: 'Anzahl'
    BubbleButton:
        text: 'Favorit'
    BubbleButton:
        text: 'X'
        
''')


class cut_copy_paste(Bubble):
    pass


class BubbleShowcase(FloatLayout):

    def __init__(self, **kwargs):
        #super(BubbleShowcase, self).__init__(**kwargs)
        #self.but_bubble = Button(text='Press to show bubble')
        #self.but_bubble.bind(on_release=self.show_bubble)
        #self.add_widget(self.but_bubble)
        pass

    def show_bubble(self, zielwidget ,widget_position, Hauptapp,*l):
        #print widget_position
        #global widget_position_global
        #widget_position_global = widget_position
        
        print zielwidget
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = cut_copy_paste()
            q=bubb.content.children
            #print q
            for i in range(len(q[:])):
                print 'buttonnummer', i, q[i].text
            print bubb.get_parent_window()
            #self.entfernen = zielwidget.remove_widget(bubb)
            #print dir()
            q[0].bind(on_release=Hauptapp.bubbleentfernen(zielwidget,bubb))
            #q[0].bind(on_press=zielwidget.remove_widget(bubb))
            #q.bind(on_release=zielwidget.remove_widget(bubb))
            #bubb.children[1].children[3].bind(on_press=bubb.clear_widgets())
            #App.bubb = bubb
            #self.add_widget(bubb)
            self.bubb.pos = widget_position 
            zielwidget.add_widget(bubb)
            #self.bubb.pos = widget_position
                   
        else:
            values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                'top_mid', 'top_right', 'right_top', 'right_mid',
                'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
            index = values.index(self.bubb.arrow_pos)
            self.bubb.arrow_pos = 'bottom_mid'#values[(index + 1) % len(values)]
            #self.bubb.background_image = 'pictures/white2.png'
            #self.bubb.background_color = (1, 0, 0, 1) 
            #self.bubb.border = [0.5, 0.5, 0.5, 0.5]
            #self.bubb.orientation = 'vertical'

        #def bubbleentfernen(self):
            #print ' testtestesttest'
            #a = App.bubb.get_parent_window()
            #a.remove_widget(App.bubb)

        
class TestBubbleApp(App):

    def build(self):
        return BubbleShowcase()

if __name__ == '__main__':
    TestBubbleApp().run()
